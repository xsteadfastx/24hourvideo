import click

from twentyfourhourvideo import video


@click.group()
def cli():
    pass


@cli.command(help='Plays a video.')
@click.argument('input', type=click.Path())
def play(input):
    video.play(input)


@cli.command(help='Save a video.')
@click.argument('input', type=click.Path())
@click.argument('output', type=click.Path())
def save(input, output):
    video.save(input, output)
