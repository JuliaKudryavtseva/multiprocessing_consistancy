import numpy as np


# functions for IOUs calculations
def calculate_iou(gt_mask, pred_mask):
    overlap = pred_mask * gt_mask  # Logical AND
    union = (pred_mask + gt_mask) > 0  # Logical OR
    iou = overlap.sum() / float(union.sum())
    return iou

def multi_get_IOU(curr_masks, next_masks):
    '''
    Create process for every IOU(mask_1, mask_2) and gather all results into matrix of IOUs

    Input: list of np.arrays
    Output: np.array (len(curr_masks) * len(next_masks))
    '''
    IOUs = np.zeros((len(curr_masks), len(next_masks)))

    return IOUs
