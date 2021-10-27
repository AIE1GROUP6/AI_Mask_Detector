# AIE1 Group6 - Computer Vision - AI Mask Detector



## Before you run the tracker

1. Clone the repository recursively:

`git clone --recurse-submodules https://github.com/AIE1GROUP6/AI_Mask_Detector.git`

If you already cloned and forgot to use `--recurse-submodules` you can run `git submodule update --init`

2. Make sure that you fulfill all the requirements: Python 3.8 or later with all [requirements.txt](https://github.com/mikel-brostrom/Yolov5_DeepSort_Pytorch/blob/master/requirements.txt) dependencies installed, including torch>=1.7. To install, run:

`pip install -r requirements.txt`


## Example command for detect mask 

python track.py --source tokyo.mp4 --output output_folder --yolo_weights yolov5\weights\mask.pt
