<table style="width:100%">
  <tr>
    <td>
      <img src="https://user-images.githubusercontent.com/26833433/61591130-f7beea00-abc2-11e9-9dc0-d6abcf41d713.jpg">
    </td>
    <td align="center">
    <a href="https://www.ultralytics.com" target="_blank">
    <img src="https://storage.googleapis.com/ultralytics/logo/logoname1000.png" width="160"></a>
      <img src="https://user-images.githubusercontent.com/26833433/61591093-2b4d4480-abc2-11e9-8b46-d88eb1dabba1.jpg">
          <a href="https://itunes.apple.com/app/id1452689527" target="_blank">
    <img src="https://user-images.githubusercontent.com/26833433/50044365-9b22ac00-0082-11e9-862f-e77aee7aa7b0.png" width="180"></a>
    </td>
    <td>
      <img src="https://user-images.githubusercontent.com/26833433/61591100-55066b80-abc2-11e9-9647-52c0e045b288.jpg">
    </td>
  </tr>
</table>

# Introduction

This directory contains PyTorch YOLOv3 software developed by Ultralytics LLC, and **is freely available for redistribution under the GPL-3.0 license**. For more information please visit https://www.ultralytics.com.

# Description

The https://github.com/ultralytics/yolov3 repo contains inference and training code for YOLOv3 in PyTorch. The code works on Linux, MacOS and Windows. Training is done on the COCO dataset by default: https://cocodataset.org/#home. **Credit to Joseph Redmon for YOLO:** https://pjreddie.com/darknet/yolo/.

# Requirements

Python 3.7 or later with the following `pip3 install -U -r requirements.txt` packages:

- `numpy`
- `torch >= 1.1.0`
- `opencv-python`
- `tqdm`

# Tutorials

* [GCP Quickstart](https://github.com/ultralytics/yolov3/wiki/GCP-Quickstart)
* [Transfer Learning](https://github.com/ultralytics/yolov3/wiki/Example:-Transfer-Learning)
* [Train Single Image](https://github.com/ultralytics/yolov3/wiki/Example:-Train-Single-Image)
* [Train Single Class](https://github.com/ultralytics/yolov3/wiki/Example:-Train-Single-Class)
* [Train Custom Data](https://github.com/ultralytics/yolov3/wiki/Train-Custom-Data)

# Jupyter Notebook

Our Jupyter [notebook](https://colab.research.google.com/github/ultralytics/yolov3/blob/master/examples.ipynb) provides quick training, inference and testing examples.

# Training

**Start Training:** `python3 train.py` to begin training after downloading COCO data with `data/get_coco_dataset.sh`. Each epoch trains on 117,263 images from the train and validate COCO sets, and tests on 5000 images from the COCO validate set.

**Resume Training:** `python3 train.py --resume` to resume training from `weights/last.pt`.

**Plot Training:** `from utils import utils; utils.plot_results()` plots training results from `coco_16img.data`, `coco_64img.data`, 2 example datasets available in the `data/` folder, which train and test on the first 16 and 64 images of the COCO2014-trainval dataset.

<img src="https://user-images.githubusercontent.com/26833433/63258271-fe9d5300-c27b-11e9-9a15-95038daf4438.png" width="900">

## Image Augmentation

`datasets.py` applies random OpenCV-powered (https://opencv.org/) augmentation to the input images in accordance with the following specifications. Augmentation is applied **only** during training, not during inference. Bounding boxes are automatically tracked and updated with the images. 416 x 416 examples pictured below.

Augmentation | Description
--- | ---
Translation | +/- 10% (vertical and horizontal)
Rotation | +/- 5 degrees
Shear | +/- 2 degrees (vertical and horizontal)
Scale | +/- 10%
Reflection | 50% probability (horizontal-only)
H**S**V Saturation | +/- 50%
HS**V** Intensity | +/- 50%

<img src="https://user-images.githubusercontent.com/26833433/66699231-27beea80-ece5-11e9-9cad-bdf9d82c500a.jpg" width="900">

## Speed

https://cloud.google.com/deep-learning-vm/  
**Machine type:** n1-standard-8 (8 vCPUs, 30 GB memory)  
**CPU platform:** Intel Skylake  
**GPUs:** K80 ($0.20/hr), T4 ($0.35/hr), V100 ($0.83/hr) CUDA with [Nvidia Apex](https://github.com/NVIDIA/apex) FP16/32  
**HDD:** 100 GB SSD  
**Dataset:** COCO train 2014 (117,263 images)

GPUs | `batch_size` | images/sec | epoch time | epoch cost
--- |---| --- | --- | --- 
K80 | 64 (32x2) | 11  | 175 min  | $0.58
T4 | 64 (32x2) | 40  | 49 min  | $0.29
T4 x2 | 64 (64x1) | 61  | 32 min  | $0.36
V100 | 64 (32x2) | 115 | 17 min | $0.24
V100 x2 | 64 (64x1) | 150 | 13 min | $0.36
2080Ti | 64 (32x2) | 81  | 24 min  | - 
2080Ti x2 | 64 (64x1) | 140  | 14 min  | - 

# Inference

`detect.py` runs inference on any sources:

```bash
python3 detect.py --source ...
```

- Image:  `--source file.jpg`
- Video:  `--source file.mp4`
- Directory:  `--source dir/`
- Webcam:  `--source 0`
- RTSP stream:  `--source rtsp://170.93.143.139/rtplive/470011e600ef003a004ee33696235daa`
- HTTP stream:  `--source http://wmccpinetop.axiscam.net/mjpg/video.mjpg`

To run a specific models:

**YOLOv3:** `python3 detect.py --cfg cfg/yolov3.cfg --weights weights/yolov3.weights`
<img src="https://user-images.githubusercontent.com/26833433/64067835-51d5b500-cc2f-11e9-982e-843f7f9a6ea2.jpg" width="500">

**YOLOv3-tiny:** `python3 detect.py --cfg cfg/yolov3-tiny.cfg --weights weights/yolov3-tiny.weights`
<img src="https://user-images.githubusercontent.com/26833433/64067834-51d5b500-cc2f-11e9-9357-c485b159a20b.jpg" width="500">

**YOLOv3-SPP:** `python3 detect.py --cfg cfg/yolov3-spp.cfg --weights weights/yolov3-spp.weights`
<img src="https://user-images.githubusercontent.com/26833433/64067833-51d5b500-cc2f-11e9-8208-6fe197809131.jpg" width="500">


# Pretrained Weights

- Darknet `*.weights` format: https://pjreddie.com/media/files/yolov3.weights
- PyTorch `*.pt` format: https://drive.google.com/drive/folders/1uxgUBemJVw9wZsdpboYbzUN4bcRhsuAI

## Darknet Conversion

```bash
$ git clone https://github.com/ultralytics/yolov3 && cd yolov3

# convert darknet cfg/weights to pytorch model
$ python3  -c "from models import *; convert('cfg/yolov3-spp.cfg', 'weights/yolov3-spp.weights')"
Success: converted 'weights/yolov3-spp.weights' to 'converted.pt'

# convert cfg/pytorch model to darknet weights
$ python3  -c "from models import *; convert('cfg/yolov3-spp.cfg', 'weights/yolov3-spp.pt')"
Success: converted 'weights/yolov3-spp.pt' to 'converted.weights'
```

# mAP

- `test.py --weights weights/yolov3.weights` tests official YOLOv3 weights.
- `test.py --weights weights/last.pt` tests most recent checkpoint.
- `test.py --weights weights/best.pt` tests best checkpoint.
- Compare to darknet published results https://arxiv.org/abs/1804.02767.

[ultralytics/yolov3](https://github.com/ultralytics/yolov3) mAP@0.5 ([darknet](https://arxiv.org/abs/1804.02767)-reported mAP@0.5)

<i></i>         | 320         | 416         | 608
---             | ---         | ---         | ---
`YOLOv3`        | 51.8 (51.5) | 55.4 (55.3) | 58.2 (57.9)
`YOLOv3-SPP`    | 53.7        | 57.7        | 60.7 (60.6)
`YOLOv3-tiny`   | 29.0        | 32.9 (33.1) | 35.5

```bash
$ python3 test.py --save-json --img-size 608
Namespace(batch_size=16, cfg='cfg/yolov3-spp.cfg', conf_thres=0.001, data='data/coco.data', img_size=608, iou_thres=0.5, nms_thres=0.5, save_json=True, weights='weights/yolov3-spp.weights')
Using CUDA device0 _CudaDeviceProperties(name='Tesla T4', total_memory=15079MB)
                Class    Images   Targets         P         R       mAP        F1: 100% 313/313 [07:40<00:00,  2.34s/it]
                  all     5e+03  3.58e+04     0.119     0.788     0.594     0.201
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.367 <---
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.607 <---
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.387
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.208
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.392
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.487
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.297
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.465
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.495
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.332
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.518
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.621

$ python3 test.py --save-json --img-size 416
Namespace(batch_size=16, cfg='cfg/yolov3-spp.cfg', conf_thres=0.001, data='data/coco.data', img_size=416, iou_thres=0.5, nms_thres=0.5, save_json=True, weights='weights/yolov3s-ultralytics.pt')
Using CUDA device0 _CudaDeviceProperties(name='Tesla T4', total_memory=15079MB)
                Class    Images   Targets         P         R       mAP        F1: 100% 313/313 [07:01<00:00,  1.41s/it]
                  all     5e+03  3.58e+04      0.11     0.739     0.569     0.185
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.373
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.577
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.392
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.175
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.403
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.537
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.313
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.482
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.501
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.266
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.541
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.693
```

# Citation

[![DOI](https://zenodo.org/badge/146165888.svg)](https://zenodo.org/badge/latestdoi/146165888)

# Contact

Issues should be raised directly in the repository. For additional questions or comments please email Glenn Jocher at glenn.jocher@ultralytics.com or visit us at https://contact.ultralytics.com.
