# !pip install ultralytics # if running in google colab
# !pip install ffmpegcv # if running in google colab

from ultralytics import YOLO
# import cv2  # only need if using cv2 instead of ffmpegcv
# from google.colab.patches import cv2_imshow  # use only in google colab
import torch
from pathlib import Path
import numpy as np
import sys
import ffmpegcv

print(torch.__version__)

# Check available GPU devices.
print(f"GPU? {torch.cuda.is_available()}" )

# Object Detection on Image
# model = YOLO("yolov8s.pt")  # loading yolov8 small model
# url = r"https://cdn.mos.cms.futurecdn.net/7KVFwQMr2bLPRtRsUUAFLe-1024-80.jpg.webp"  # url of the image to use
# image_name = Path(url).name
# results = model.predict(source=url, save=True, imgsz=2400)

# image_path = str(Path(results[0].save_dir).joinpath(image_name))
# print(image_path)
# cv2_imshow(cv2.imread(image_path))  # if running in google colab, shows te image as output

# Tracking Youtube Video
url = "https://www.youtube.com/watch?v=KBsqQez-O4w"  # url of a youtube video
model = YOLO('yolov8s.pt')
results = model.track(url, stream=True)

# if using cv2, run the code below
# cv2.VideoWriter_fourcc('M','J','P','G')
# video = cv2.VideoWriter('rebuilt-video-tests.avi', fourcc=-1, fps=25, frameSize=(1280, 720))
# for i, r in enumerate(results):
#     frame = r.plot(conf=False, line_width=2)
#     video.write(frame)
#     if i==1100:
#         video.release()
#         cv2.destroyAllWindows()
#         sys.exit()

# if using ffmpegcv, run the code below
with ffmpegcv.VideoWriter('rebuild-video-test-with-ffmpegcv.avi', None, fps=25, frameSize=(1280, 720)) as video:
    for i, r in enumerate(results):
        frame = r.plot(conf=False, line_width=2)
        video.write(frame)
        if i==1100:
            sys.exit()

# TODO: commit and push to github, BUT IGNORE THE VIRTUAL ENVIRONMENT!!!