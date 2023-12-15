# Multiprocessing consistancy

The problem of making video frames consistent is tightly connected to reconstruction of 3D scenes with NeRF arcitecture. Frame consistancy is labeling one objects with one class label on all frames. The current implemented algorithm performs satisfactory results, however, it is too slow. The main problem is in calculating IOU metrics between each mask in current masks array and each mask in next masks array, which is difficult task with images of high resolution.

## Quick start

git clone git@github.com:JuliaKudryavtseva/multiprocessing_consistancy.git
cd multiprocessing_consistancy

create folder data and put there numpy masks: 
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