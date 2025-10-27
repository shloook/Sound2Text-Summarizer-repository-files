"""Example usage outside the package."""
from sound2text.pipeline import transcribe_and_summarize

if __name__ == '__main__':
audio = "examples/sample_audio.wav"
out = transcribe_and_summarize(audio_path=audio, stt_backend="local_whisper", stt_options={"model_name": "small"}, summarizer_model="sshleifer/distilbart-cnn-12-6")
print("Transcription:")
print(out['transcription']['text'])
print("\nSummary:\n")
print(out['summary']['summary_text'])
