24hourvideo
===========

A copy of [24 Hour Psycho](https://en.wikipedia.org/wiki/24_Hour_Psycho) by Douglas Gordon. It takes a video file and plays it frame by frame that it takes 24 hours. So each frame show its piece of art or something.

It depends on [opencv](http://opencv.org/) and [ffmpeg](https://www.ffmpeg.org/). You can install everything with `sudo apt-get install python-opencv ffmpeg`. Run `make install` for getting everything ready. It will create an virtualenv and copy some opencv python modules to get it running inside an virtualenv.

```
Usage: 24hourvideo [OPTIONS] INPUT

  Plays a video.

Options:
  --help  Show this message and exit.
```
