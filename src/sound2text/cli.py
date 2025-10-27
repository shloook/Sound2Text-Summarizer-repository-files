"""Simple CLI for transcribing and summarizing audio files."""
import json
import click
from .pipeline import transcribe_and_summarize


@click.group()
def cli():
pass


@cli.command()
@click.option("--audio", required=True, help="Path to audio file (wav/mp3)")
@click.option("--backend", default="local_whisper", help="STT backend to use")
@click.option("--model", default=None, help="Model name for STT or summarizer depending on backend")
@click.option("--out", default=None, help="Output JSON file to write results")
def transcribe(audio, backend, model, out):
stt_options = {}
if backend == "local_whisper" and model:
stt_options["model_name"] = model
result = transcribe_and_summarize(audio, stt_backend=backend, stt_options=stt_options, summarizer_model=model)
if out:
with open(out, "w", encoding="utf-8") as f:
json.dump(result, f, ensure_ascii=False, indent=2)
click.echo(f"Saved output to {out}")
else:
click.echo(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
cli()
