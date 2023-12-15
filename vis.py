import colorsys
import os
import json
import numpy as np
from tqdm import tqdm
from PIL import Image


def generate_color():
    N = 50
    i = 0
    brightness = 1
    saturation = 0.7
    while True:
        yield tuple(round(i * 255) for i in colorsys.hsv_to_rgb(i/N, saturation, brightness)) 
        i += 1

def visualise_frame_masks(masks):
    final_mask = np.zeros_like(masks[0]).astype(float)
    final_mask = np.tile(final_mask[:, :, np.newaxis], (1, 1, 3))

    for mask in masks:
        label = np.max(mask)
        if label in label2color.keys():
            color = label2color[label]
        else:
            color = next(random_color)
            label2color[label] = color

        for i in range(3):
            final_mask[:, :, i][mask > 0]= color[i]

    return final_mask
    

# preprocessing
def load_masks(name):
    next_frame = ANNOTATIONS[name]
    next_mask_path = [mask['segmentation'] for mask in next_frame]
    next_masks = [np.load(mask_path) for mask_path in next_mask_path]
    return next_masks


if __name__ == '__main__':
    INPUT_PATH = './data/marked_images_skolkovo_stability_score'
    SAVE_PATH = './data/vis_consistent'
    json_file = 'skolkovo_stability_score.json'

    os.makedirs(SAVE_PATH, exist_ok=True)

    with open(os.path.join(INPUT_PATH, json_file)) as f:
            ANNOTATIONS = json.load(f)

    annotations = sorted(tuple(ANNOTATIONS.keys()))

    random_color = generate_color()
    label2color = {}

    image_list = []
    for frame in tqdm(annotations):
        masks = load_masks(frame)
        vis_masks = visualise_frame_masks(masks)
        vis_masks = Image.fromarray(vis_masks.astype('uint8'), 'RGB')
        image_list.append(vis_masks)


    image_list[0].save(
        os.path.join(SAVE_PATH, "vis_consistent_skolkovo_stability_score.gif"), 
        save_all=True, append_images=image_list[1:], optimize=False, duration=100, loop=0)
