# Multiprocessing consistancy

to label consistant frames of experiment with name "no_multiprocessing":
    python mark_label.py --exp-name no_multiprocessing

to visualize results
    python vis.py --exp-name no_multiprocessing

Profiler:
    python -m cProfile -s cumulative mark_label.py --exp-name no_multiprocessing