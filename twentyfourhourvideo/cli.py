import click

from twentyfourhourvideo import video


@click.command(help='Plays a video.')
@click.argument('input', type=click.Path())
def main(input):
    video.play(input)
