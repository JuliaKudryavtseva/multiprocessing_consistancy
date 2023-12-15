# Multiprocessing consistancy

The problem of making video frames consistent is tightly connected to reconstruction of 3D scenes with NeRF arcitecture. Frame consistancy is labeling one objects with one class label. The current implemented algorithm performs satisfactory results, however, it is too slow. The main problem is in calculating IOU metrics between each mask in current masks array and each mask in next masks array, which is difficult task with images of high resolution.

to label consistant frames of experiment with name "no_multiprocessing":

     python mark_label.py --exp-name no_multiprocessing
    

to visualize results:

    python vis.py --exp-name no_multiprocessing


Start a profiler:

    python -m cProfile -s cumulative mark_label.py --exp-name no_multiprocessing
    