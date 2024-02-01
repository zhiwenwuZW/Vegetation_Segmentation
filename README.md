# Vegetation Segmenation

## Getting Started

### Install SAM
The segmentation model we are using is SAM from Meta. To install and use SAM refer to 
https://github.com/facebookresearch/segment-anything

### Loading dataset 
DashCam Videos - https://drive.google.com/drive/folders/1FIAwqCqO7iyCryNIi9_KOXSiyYSeY77R?usp=sharing
VideoCap.py is a simple tool to cut videos into frames of pictures.


### SAM model 
Pretrained Model - https://huggingface.co/spaces/abhishek/StableSAM/blob/main/sam_vit_h_4b8939.pth

## TODO

### Train a Detect model

Base Model Yolov8 - https://github.com/ultralytics/ultralytics

Dataset - To be found

### Apply Detect model to the pictures, record the bounding boxes

### Load bounding boxes from local to guide SAM segmentation
