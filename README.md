# Small Applicatin of YOLOv8 from Ultralytics!

The code uses the YOLOv8 from [Ultralytics](https://github.com/ultralytics/ultralytics) to detect objects in images and track objects in videos.

## Follow this steps
1. Create a virtual environment with [venv](https://docs.python.org/3/library/venv.html) or [conda](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf).
2. Install the requirements.txt inside the virtual environment with 
```pip install -r requirements.txt```.
3. Install ffmpeg from this [link](https://www.ffmpeg.org/) and add its PATH to the system variables (I think it is necessary to restart the computer after this step).

The first comment block identified as **Object Detection** runs the object detection from YOLOv8 in different input formats (this [page](https://docs.ultralytics.com/modes/predict/#inference-sources) contains all possible formats). The url parameter is a Star Wars image from the Internet :) and the result is being saved under runs\detect\predict directory as default.

The second comment block identified as **Object Tracking** runs the object tracking model in a youtube video, but also accepts more input formats. I am using ffmpegcv, hence the importance of downloading ffmpeg, to rebuild the video from youtube. But I also left the code to rebuild the video using cv2. The reason to use ffmpegcv is because it produces lighter videos (also, be carefull with ling videos as it takes time to rebuild them).

Finally, for more information on YOLOv8, check [Ultraytics](https://docs.ultralytics.com/) as they have a lot of nice stuff to do! :)


