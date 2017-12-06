# Video Object Recognition
Using YOLO9000, classify objects in a video (made to support a wider range of computers than YOLO-9000 supports)

### Dependencies
* Python >= 3.5
* [Yolo-9000](https://github.com/philipperemy/yolo-9000)
* FFMPEG

### Usage
1. Run `ffmpeg -i video.mp4 "frames/out-%08d.jpg"` on your desired video
1. Put the frames folder into YOLO-9000's folder
1. Put `strain.py` into `darknet/` and run the script
1. Concatenate the frames back into a video with `ffmpeg -framerate 25 -i out_%08d.jpg output.mp4` (framerate will need adjusting)

### Known issues
* The script takes a long time to run. This is because the nueral network is running on the CPU for compatability reasons. Machine learning is much faster on a GPU but very few GPUs fully support NN/ML. To remedy, run overnight.

### Example
I collected clips of Sydney and fed it through the classifier and paired it with music to produce this result.
<a href="http://www.youtube.com/watch?feature=player_embedded&v=gAtmly-lAPs" target="_blank"><img src="http://img.youtube.com/vi/gAtmly-lAPs/0.jpg" width="400" height="300"/></a>
