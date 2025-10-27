"""Text utilities: cleaning and normalization."""
import re


def clean_text(text: str) -> str:
# simple normalizations
text = text.replace("\n", " ")
text = re.sub(r"\s+", " ", text).strip()
return text


def split_sentences(text: str):
# naive sentence splitter
import re
sents = re.split(r'(?<=[.!?])\s+', text)
return [s.strip() for s in sents if s.strip()]
