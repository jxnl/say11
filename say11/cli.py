import typer
import elevenlabs
import os
import sys
from typing import Optional
from rich.progress import track


app = typer.Typer(
    name="say11",
)


@app.command()
def say11(
    voice: str = typer.Option("Nicole", "-v", "--voice", help="Specify the voice"),
):
    elevenlabs.set_api_key(os.environ.get("ELEVENLABS_API_KEY"))

    elevenlabs.stream(
        track(
            elevenlabs.generate(text=sys.stdin, voice=voice, stream=True),
            description="Generating Audio...",
        )
    )


if __name__ == "__main__":
    app()
