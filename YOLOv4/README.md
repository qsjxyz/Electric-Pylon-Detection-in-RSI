# YOLOv4

We utilize the code provided on the author's website https://github.com/AlexeyAB/darknet. Here is the complete code we used and modification compared to the original code.
To compile the code, please refer  the instruction provided by author of YOLO [USE_YOLOv4.md](USE_YOLOv4.md).  
To use our code, you should first download pretrained weight from https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137 and put it in 'backup' folder.You should also download dataset and put it in [data/data](data/data) folder.
If you want to use our code firsthand, you can run```train.sh''' for train and '''test.sh''' for test. Details please refer YOLO [USE_YOLOv4.md](USE_YOLOv4.md).  
If you want to start from the original code, you can follow the steps below:  
1.Copy or replace the following files into the 'cfg' folder: [cfg/voc.data](cfg/voc.data), [cfg/yolov4-voc.cfg](cfg/yolov4-voc.cfg), [cfg/yolov4-voc-mu.cfg](cfg/yolov4-voc-mu.cfg), [cfg/yolov4-test.cfg](cfg/yolov4-test.cfg).
2.Replace the following files into the 'data' folder: [cfg/voc.names](cfg/voc.names).
