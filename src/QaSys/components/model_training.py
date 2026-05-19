import os
import torch
from datasets import Dataset
from transformers import (
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments,
    DataCollatorForSeq2Seq,
    EarlyStoppingCallback
)
from QaSys import logger
from datasets import load_dataset
from QaSys.entity import ModelTrainingConfig


class ModelTraining:

      def __init__(self, model_process, config: ModelTrainingConfig):
            self.model_process = model_process
            self.config = config

      def prepare_data(self):
            datasets = load_dataset("csv", data_files=self.config.data_path)
            dataset = datasets['train'].train_test_split(test_size=0.2, seed=42)
            logger.info(f"Train: {len(dataset['train'])} | Eval: {len(dataset['test'])}")

            tokenized = dataset.map(
                              lambda examples: self.model_process.preprocess(examples),
                              batched=True,
                              remove_columns=["question", "answer"]
                        )
            logger.info(tokenized)

            return tokenized


      def training_args(self):
            return Seq2SeqTrainingArguments(
                  output_dir="./flan-t5-lora-qa",
                  num_train_epochs=20,
                  per_device_train_batch_size=8,
                  per_device_eval_batch_size=8,
                  gradient_accumulation_steps=2,
                  learning_rate=3e-4,
                  lr_scheduler_type="cosine",
                  warmup_steps=0,
                  weight_decay=0.01,
                  predict_with_generate=True,
                  eval_strategy="epoch",
                  save_strategy="epoch",
                  logging_steps=10,
                  load_best_model_at_end=True,
                  metric_for_best_model="eval_loss",
                  greater_is_better=False,
                  fp16=False,                                              # ✅ disable fp16
                  bf16=torch.cuda.is_bf16_supported(),
                  report_to="none"
            )
      

      def DataCollector(self):
            return DataCollatorForSeq2Seq(
                  self.model_process.load_tokenizer(),
                  model=self.model_process.lora_config(),
                  label_pad_token_id=-100,
                  pad_to_multiple_of=8,
                  padding=True
            )

      def train_model(self):
            tokenized = self.prepare_data()
            tokenizer = self.model_process.load_tokenizer()
            model = self.model_process.lora_config()
            trainer = Seq2SeqTrainer(
                  model=model,                    # ✅ PEFT model, not base_model
                  args=self.training_args(),
                  train_dataset=tokenized["train"],
                  eval_dataset=tokenized["test"],
                  processing_class=tokenizer,
                  data_collator=self.DataCollector(),
                  callbacks=[EarlyStoppingCallback(early_stopping_patience=3)]
            )
            trainer.train()


            model.save_pretrained("artifact/model_training/flan-new-t5-lora-adapter")
            tokenizer.save_pretrained("artifact/model_training/flan-new-t5-lora-adapter")
            logger.info("Adapter saved!")
