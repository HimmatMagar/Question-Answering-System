from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)
from peft import LoraConfig, get_peft_model, TaskType
from QaSys import logger


class ModelProcess:

      def __init__(self, model_name: str):
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
      
      def load_tokenizer(self):
            return AutoTokenizer.from_pretrained("google/flan-t5-base")
      
      def load_model(self):
            return AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
      
      def preprocess(self, examples):
            MAX_INPUT = 25
            MAX_TARGET = 16

            inputs = ["answer the question: " + q for q in examples["question"]]

            model_inputs = self.tokenizer(
                  inputs,
                  max_length=MAX_INPUT,
                  truncation=True,
                  padding="max_length",
                  return_tensors=None
            )

            labels = self.tokenizer(
                  examples["answer"],
                  max_length=MAX_TARGET,
                  truncation=True,
                  padding="max_length",
                  return_tensors=None
            )

            label_ids = labels["input_ids"]

            model_inputs["labels"] = label_ids

            return model_inputs
      
      def lora_config(self):
            lora_config = LoraConfig(
                  r=16,
                  lora_alpha=32,
                  target_modules=["q", "v"],
                  lora_dropout=0.1,
                  bias="none",
                  task_type=TaskType.SEQ_2_SEQ_LM
            )
            model = get_peft_model(self.model, lora_config)
            logger.info(f"Lora config successful: {model.print_trainable_parameters()}")

            trainable = [p for p in self.model.parameters() if p.requires_grad]
            logger.info(f"Trainable param groups: {len(trainable)}")

            logger.info(type(self.model))

            return model  