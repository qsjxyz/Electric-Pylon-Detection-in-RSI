import os
import json
import shutil
import sys

config_root = 'configs/my_configs/'
config_name = 'fcos_mstrain_640_800_r101_fpn_gn_2x.py'

work_dir_root = 'work_dirs/' + config_name[:-3] + '/'

config_dir = config_root + config_name
result_root = 'result/'

result_name = config_name[:-2] + 'log'
result_dir = result_root + result_name

pth_dir = 'pth/' + config_name[:-3] + '/'

class Logger(object):
    def __init__(self, filename='result/last.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

sys.stdout = Logger(result_dir, sys.stdout)

for i in range(10):  #divide_train_test for 10 times
    print('----------experiment' + str(i) + '----------')
    os.system('python VOC_divide.py')  #divide dataset
    os.system('./tools/dist_train.sh ' + config_dir + ' 1 --validate')  #train

    #find json files of the newest training process
    file_list = os.listdir(work_dir_root[:-1])
    json_list = []
    for name in file_list:
        if name[-4:] == 'json':
            json_list.append(name)
    length = len(json_list)
    newest_json = json_list[0]
    for j in range(length - 1):
        if json_list[j + 1] > newest_json:
            newest_json = json_list[j + 1]
    json_dir = work_dir_root + newest_json

    real_max_map = 0
    max_map = 0
    s = 0

    f_json = open(json_dir, encoding='utf-8')
    
    #find the best AP
    j = 0
    for line in f_json.readlines():
        if j == 0:
            j = 1
            continue
        w = json.loads(line)
        if w['mode'] == 'val':
            if w['mAP'] >= real_max_map:
                real_max_map = w['mAP']
            if w['mAP'] >= (real_max_map - 0.005):
                max_map = w['mAP']
                s = w['epoch']
                
    print('val:max_mAP = ' + str(max_map))
    print('val:max_mAP_epoch:' + str(s))
    result = os.popen('python tools/test.py ' + config_dir + ' ' + work_dir_root + 'epoch_' + str(s) + '.pth --eval mAP')  #test and print result
    print(result.read()[-400:])
    print('\n')
    
    #save the best weight file
    pth_name = pth_dir + str(i) + '.pth'
    shutil.copyfile(work_dir_root + 'epoch_' + str(s) + '.pth', pth_name)
