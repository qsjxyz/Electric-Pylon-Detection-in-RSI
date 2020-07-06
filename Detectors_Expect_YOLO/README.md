# Detectors Expect YOLO

We built our detectors based on the MMDetection (https://github.com/open-mmlab/mmdetection) toolbox, an open source object detection toolbox based on PyTorch developed by Multimedia Laboratory, The Chinese University of Hong Kong. We used v1.2.0 to built all detectors expect YOLOv3 and YOLOv4.


## Introduction

The master branch works with **PyTorch 1.1 to 1.4**.

mmdetection is an open source object detection toolbox based on PyTorch. It isa part of the open-mmlab project developed by [Multimedia Laboratory, CUHK](http://mmlab.ie.cuhk.edu.hk/).

![demo image](demo/demo.jpg)
![demo result (by Cascade R-CNN)](demo/demo_result.jpg)

## Installation

Please refer to [INSTALL.md](docs/INSTALL.md) for installation and dataset preparation.

## Get Started

Please see [GETTING_STARTED.md](docs/GETTING_STARTED.md) for the basic usage of MMDetection.

## Pretrained Weight

If you use our code for pylon detection, you should download pretrained weight of ResNet-101 of PyTorch from https://download.pytorch.org/models/resnet101-5d3b4d8f.pth.

## Use MMDetection to Detect Pylons

### Prepare

Download pretrained weight and put it in 'checkpoints' folder.  
 create a standard VOC2007 data set folder in the 'data' folder and put the data you want to use into the corresponding folder.Run Voc_divide.py to partition the data set.

### Train

If you use our modified code for pylon detection, you can just train detectors follow [GETTING_STARTED.md](docs/GETTING_STARTED.md).  
If you have already got a MMDetection (v1.x) in your computer, you can also repeat our experiment by following the steps below:  
1.Change CLASSES in [mmdet/dataset/voc.py](mmdet/dataset/voc.py) to ['pylon', ].  
2.Change voc_classes in [mmdet/core/evaluation/class_names.py](mmdet/core/evaluation/class_names.py) to ['pylon', ].  
3.Put [our config files](configs/my_configs) into 'configs' folder.  
Then you can train detectors follow [GETTING_STARTED.md](docs/GETTING_STARTED.md).  

### Test

You can just test performance of detectors follow [GETTING_STARTED.md](docs/GETTING_STARTED.md).  

### Special Instructions

If you want to test Retinanet-FSAF, you should change code follow https://github.com/open-mmlab/mmdetection/pull/675, a post from MMDetection community.
If you want to do 10 random repetitions, you can run [experiment_10_times.py](experiment_10_times.py), get trained weight and performance indicators. If you want to test detectors on EPC-C Dataset, you can run [test_10_times.py](test_10_times.py). If you want to get visualization results, you can run [visualization.py](visualization.py).