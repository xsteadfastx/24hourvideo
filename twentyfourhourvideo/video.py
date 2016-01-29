import sys

import click
import cv2


def calc_length(fps, frames):
    return (frames / fps) * 1000.0


def calc_wait_time(fps, frames):
    length = calc_length(fps, frames)
    wait = (1 / fps * 1000.0) * frames
    complete = ((length / wait) * 86400000.0) / frames

    return int(complete)


def calc_fps(frames):
    return frames / 86400.0


def play(input):
    cap = cv2.VideoCapture(input)

    frames = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)

    wait_time = calc_wait_time(fps, frames)

    with click.progressbar(length=int(frames), show_pos=True) as bar:

        while(cap.isOpened()):
            ret, frame = cap.read()

            cv2.imshow('frame', frame)

            bar.update(1)
            cv2.waitKey(wait_time)

    cap.release()
    cv2.destroyAllWindows()


def save(input, output):
    cap = cv2.VideoCapture(input)

    width = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    frames = cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)

    fps = calc_fps(frames)
    click.echo(frames)
    click.echo(fps)

    # abort if fps is too low
    if fps < 0.1:
        click.echo('Video too small.')
        sys.exit(1)

    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter(output, fourcc, fps, (width, height))

    with click.progressbar(length=int(frames), show_pos=True) as bar:

        while(cap.isOpened()):
            ret, frame = cap.read()

            if ret is True:
                out.write(frame)
                bar.update(1)

            else:
                break

    cap.release()
    cv2.destroyAllWindows()
