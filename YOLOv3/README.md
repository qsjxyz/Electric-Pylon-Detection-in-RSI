# YOLOv3

We utilize the code provided on the author's website https://github.com/ultralytics/yolov3. Here is the complete code we used and modification compared to the original code.

## Compile

To compile the code, please refer  the instruction provided by author of YOLO [USE_YOLOv3.md](USE_YOLOv3.md).  

## Use

To use our code, you should first download pretrained weight from https://pjreddie.com/media/files/yolov3.weights and put it in 'weights' folder. You should also download dataset and put it in“data”folder.  
If you want to use our code firsthand, you can follow the steps below：
1.Put our dataset into the 'data' folder: [data/Annotations](data/Annotations),[data/JPEGImages](data/JPEGImages),and [data/images](data/images) is a copy of [data/JPEGImages](data/JPEGImages).
2.Use maketxt.py and voc_label.py to preprocess the dataset.
3.Run train.py, test.py or detect.py to train a model, test its performance or get visualized results. RUN_CODE provides the command lines to run. The validation set and test set can be adjusted in [data/pylon.data](data/pylon.data) .

If you want to start from the original code, you should note the steps below:  
1.Copy or replace the following files into the 'cfg' folder:  [cfg/yolov3.cfg](cfg/yolov3.cfg)
2.Replace the following files into the 'data' folder: pylon.data, pylon.names.
More details please refer YOLO [USE_YOLOv3.md](USE_YOLOv3.md). 
