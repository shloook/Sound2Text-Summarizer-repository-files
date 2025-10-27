"""High-level pipeline that wires transcription -> summarization."""
from pathlib import Path
from .transcribe import transcribe
from .summarize import Summarizer


def transcribe_and_summarize(audio_path: str, stt_backend: str = "local_whisper", stt_options: dict = None, summarizer_model: str = None):
stt_options = stt_options or {}
transcribed = transcribe(audio_path, backend=stt_backend, **stt_options)
text = transcribed.get("text", "")

summarizer_model = summarizer_model or "sshleifer/distilbart-cnn-12-6"
summarizer = Summarizer(model=summarizer_model)
summary = summarizer.summarize(text)

return {
"transcription": transcribed,
"summary": summary
}
