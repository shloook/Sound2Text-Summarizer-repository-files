"""Speech-to-text: pluggable backends.

Supported backends:
- local_whisper: uses `whisper` package (openai-whisper)
- remote_api: placeholder for cloud STT (e.g., OpenAI, AssemblyAI, etc.)

"""
from typing import Dict, Any
from pathlib import Path
from .utils.audio import load_audio
from .utils.text import clean_text


def transcribe_local_whisper(audio_path: str, model_name: str = "small") -> Dict[str, Any]:
"""Transcribe using local whisper package. Returns dict with `text` and metadata."""
try:
import whisper
except Exception as e:
raise RuntimeError("whisper is required for local_whisper backend. Install openai-whisper") from e

model = whisper.load_model(model_name)
audio = str(Path(audio_path))
result = model.transcribe(audio)
text = result.get("text", "")
return {"text": clean_text(text), "raw": result}


def transcribe_remote_api(audio_path: str, api_url: str, api_key: str = None) -> Dict[str, Any]:
"""Placeholder for remote API transcription. Implement as required for your provider."""
import requests
files = {"file": open(audio_path, "rb")}
headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
resp = requests.post(api_url, files=files, headers=headers)
resp.raise_for_status()
data = resp.json()
text = data.get("text") or data.get("transcript") or ""
return {"text": clean_text(text), "raw": data}


def transcribe(audio_path: str, backend: str = "local_whisper", **kwargs):
if backend == "local_whisper":
return transcribe_local_whisper(audio_path, **kwargs)
elif backend == "remote_api":
return transcribe_remote_api(audio_path, **kwargs)
else:
raise ValueError(f"Unknown backend {backend}")
