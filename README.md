# Multiprocessing consistancy

The problem of making video frames consistent is tightly connected to reconstruction of 3D scenes with NeRF architecture and segmentation of objects on new rendered images without using huge neural backbones. Frame consistency is labeling one objects with one class label on all frames. The current implemented algorithm performs satisfactory results, however, it is too slow. The main problem is in calculating IOU metrics between each mask in current masks array and each mask in next masks array, which is difficult task with images of high resolution.


Before algorithm     |  After algorithm
:-------------------------:|:-------------------------:
![](https://github.com/JuliaKudryavtseva/multiprocessing_consistancy/blob/main/vis_consistent/vis_consistent.gif)  |  ![](https://github.com/JuliaKudryavtseva/multiprocessing_consistancy/blob/main/vis_consistent/cupy.gif)

## Quick start
```
git clone git@github.com:JuliaKudryavtseva/multiprocessing_consistancy.git
cd multiprocessing_consistancy
pip install -r requirements.txt
```
or install mpi4py and cupy from:

https://pypi.org/project/mpi4py/

https://docs.cupy.dev/en/stable/install.html#requirements



create folder data and put there numpy masks: 

https://drive.google.com/file/d/15ywBQ55yWYsuvv3QvLoTmVNN1jwMvUX3/view?usp=sharing
```
data
├─ numpy_masks               
│  ├─ 0015
│  │  ├─ 0.npy  
│  │  ├─ 1.npy  
│  ...
| sk_masks.json
```

## Algorithm without multiprocessing

     python mark_label.py --exp-name no_multiprocessing
    

to visualize results:

    python vis.py --exp-name no_multiprocessing


Start a profiler:

    python -m cProfile -s cumulative mark_label.py --exp-name no_multiprocessing
    

## Algorithm with multiprocessing

Options:

    python mark_label.py --exp-name multiprocessing --multi multi

    python mark_label.py --exp-name mpi --multi mpi

    python mark_label.py --exp-name cupy --multi cupy


## Get estimation of the results of multiprocessing

    python running_time/get_results.py

# Results   

Average time results       |  Average speed up results 
:-------------------------:|:-------------------------:
![](https://github.com/JuliaKudryavtseva/multiprocessing_consistancy/blob/main/running_time/time_per_image.png)  |  ![](https://github.com/JuliaKudryavtseva/multiprocessing_consistancy/blob/main/running_time/all_images_speed_up.png)
