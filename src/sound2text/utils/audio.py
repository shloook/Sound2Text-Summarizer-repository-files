"""Audio utilities: loading, resampling, simple preprocessing."""
from pathlib import Path
import numpy as np
import soundfile as sf
import librosa


def load_audio(path, sr=16000, mono=True):
path = Path(path)
data, file_sr = sf.read(str(path))
if mono and data.ndim > 1:
data = np.mean(data, axis=1)
if file_sr != sr:
data = librosa.resample(data.astype(float), orig_sr=file_sr, target_sr=sr)
return data, sr


def save_audio(path, audio, sr=16000):
sf.write(str(path), audio, sr)
