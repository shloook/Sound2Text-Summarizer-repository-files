"""Summarization utilities using Hugging Face transformers pipeline."""
from typing import Dict
from transformers import pipeline


class Summarizer:
def __init__(self, model: str = "sshleifer/distilbart-cnn-12-6", device: int = -1):
# device=-1 means CPU; set to 0 for GPU
self.model_name = model
self.pipe = pipeline("summarization", model=model, device=device)

def summarize(self, text: str, max_length: int = 150, min_length: int = 30) -> Dict[str, str]:
outputs = self.pipe(text, max_length=max_length, min_length=min_length, truncation=True)
summary = outputs[0].get("summary_text", outputs[0].get("summary_text") if outputs else "")
return {"summary_text": summary}
