import torch
import torch.nn.functional as F
from ...ops import sigmoid_focal_loss

def select_iou_loss(pred,
                    target,
                    weight,
                    avg_factor=None):
    if avg_factor is None:
        avg_factor = pred.size()[0]
    assert pred.size()[0] == target.size()[0]

    target = target.clamp(min=0.)
    area_pred = (pred[:, 0] + pred[:, 2]) * (pred[:, 1] + pred[:, 3])
    area_gt = (target[:, 0] + target[:, 2]) * (target[:, 1] + target[:, 3])
    area_i = (torch.min(pred[:, 0], target[:, 0]) + torch.min(pred[:, 2], target[:, 2])) * \
             (torch.min(pred[:, 1], target[:, 1]) + torch.min(pred[:, 3], target[:, 3]))
    area_u = area_pred + area_gt - area_i
    iou = area_i / area_u
    loc_losses = - torch.log(iou.clamp(min=1e-7))
    return torch.sum(weight * loc_losses) / avg_factor