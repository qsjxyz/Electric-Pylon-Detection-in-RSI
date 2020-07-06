from mmdet.apis import init_detector, inference_detector, show_result
import mmcv

config_root = 'configs/my_configs/'
config_name_list = ['faster_rcnn_r101_fpn_1x.py', 'cascade_rcnn_r101_fpn_1x.py', 'grid_rcnn_gn_head_r101_fpn_2x.py',
                    'libra_faster_rcnn_r101_fpn_1x.py', 'retinanet_r101_fpn_1x.py', 'retinanet_free_anchor_r101_fpn_1x.py',
                    'fsaf_retinanet_r101_fpn_1x.py',  'fcos_mstrain_640_800_r101_fpn_gn_2x.py']

img_name_list = ['1_2.jpg', '2_2.jpg']  #put the image in root directory
for config_name in config_name_list:
    work_dir_root = 'work_dirs/' + config_name[:-3] + '/'

    config_file = config_root + config_name

    checkpoint_file = 'pth/' + config_name[:-3] + '/0.pth'  #use the weight trained by the first round

    # build the model from a config file and a checkpoint file
    model = init_detector(config_file, checkpoint_file, device='cuda:0')

    # test a single image and show the results

    for image_name in img_name_list:
        img = mmcv.imread(image_name) # which will only load it once
        result = inference_detector(model, img)
        # visualize the results in a new window
        # show_result(img, result, model.CLASSES)
        # or save the visualization results to image files
        show_result(img, result, model.CLASSES, show=False, out_file='img_look/'+config_name[:-3]+image_name)