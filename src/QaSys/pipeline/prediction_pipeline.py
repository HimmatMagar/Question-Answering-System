import torch
from peft import PeftModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class PredictionPipeline:

      def __init__(self):
            self.base_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
            self.model = PeftModel.from_pretrained(self.base_model, "artifact/model/flan-new-t5-lora-adapter")
            self.tokenizer = AutoTokenizer.from_pretrained("artifact/model/flan-new-t5-lora-adapter")
            
      
      def ask(self, question):
            self.model.eval()
            prompt = "answer the question: " + question
            inputs = self.tokenizer(prompt, return_tensors="pt", max_length=128, truncation=True)

            with torch.no_grad():
                  outputs = self.model.generate(
                        **inputs,
                        max_new_tokens=64,
                        num_beams=4,              # beam search = better answers
                        early_stopping=True
                  )

            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)