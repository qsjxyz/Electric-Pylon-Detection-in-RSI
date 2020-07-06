import os
import random
import math
fo1=open('data/VOCdevkit/VOC2007/ImageSets/Main/test.txt', 'w')
fo2=open('data/VOCdevkit/VOC2007/ImageSets/Main/trainval.txt', 'w')
fo3=open('data/VOCdevkit/VOC2007/ImageSets/Main/train.txt', 'w')
fo4=open('data/VOCdevkit/VOC2007/ImageSets/Main/val.txt', 'w')
filepath='data/VOCdevkit/VOC2007/Annotations'
filelist=os.listdir(filepath)
file_name=[]
for w in filelist:
    file_name.append(w.replace('.xml',''))
file_num=len(file_name)
trainval_num=0.9
train_num=0.9
#trainval
trainval_list=random.sample(range(file_num),math.floor(trainval_num*file_num))
#test
test_list=(list(set(range(file_num)).difference(set(trainval_list))))
random.shuffle(test_list)
#train
train_list=random.sample(trainval_list,math.floor(train_num*len(trainval_list)))
#val
val_list=list(set(trainval_list).difference(set(train_list)))
random.shuffle(val_list)
#put in txt
for i in trainval_list:
    fo2.write(file_name[i]+'\n')
for i in test_list:
    fo1.write(file_name[i]+'\n')
for i in train_list:
    fo3.write(file_name[i]+'\n')
for i in val_list:
    fo4.write(file_name[i]+'\n')
fo1.close()
fo2.close()
fo3.close()
fo4.close()