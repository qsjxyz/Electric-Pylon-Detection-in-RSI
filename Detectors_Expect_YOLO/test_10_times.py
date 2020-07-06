import os

config_root = 'configs/my_configs/'

config_name_list = ['faster_rcnn_r101_fpn_1x.py', 'cascade_rcnn_r101_fpn_1x.py', 'grid_rcnn_gn_head_r101_fpn_2x.py',
                    'libra_faster_rcnn_r101_fpn_1x.py', 'retinanet_r101_fpn_1x.py', 'retinanet_free_anchor_r101_fpn_1x.py',
                    'fsaf_retinanet_r101_fpn_1x.py',  'fcos_mstrain_640_800_r101_fpn_gn_2x.py']

#config_name_list = ['fsaf_retinanet_r101_fpn_1x.py']
for config_name in config_name_list:
    work_dir_root = 'work_dirs/' + config_name[:-3] + '/'

    config_dir = config_root + config_name

    pth_dir = 'pth/old/' + config_name[:-3] + '/'

    print(config_name)
    for i in range(10):
        print('----------experiment' + str(i) + '----------')
        os.system('python tools/test.py ' + config_dir + ' ' + pth_dir + str(i) + '.pth --eval mAP')