import json
import os
import numpy as np
import matplotlib.pyplot as plt


with open('running_time/no_multi.json') as f:
        no_multi = json.load(f)

no_multi = np.array(no_multi)


result_files = [s for s in os.listdir('running_time') if s.endswith('.json') and s[:2] != 'no']
vis_results = {}

for result_file in result_files:
    dir_result_file = os.path.join('running_time/', result_file)
    with open(dir_result_file) as f:
        module_result = json.load(f)
        module_result = np.array(module_result)

        speed_up = no_multi/module_result
        avr_speed_up = np.mean(speed_up)

        vis_results[result_file.split('.')[0]] = (avr_speed_up, speed_up)


for module in vis_results.keys():
     all_speed_up = vis_results[module][1]
     plt.plot(np.arange(len(all_speed_up)), all_speed_up, label=module)
     plt.legend()
     plt.title('Speed up for all images')
     plt.xlabel('image number')
     plt.ylabel('Speed up for one image')

plt.savefig('running_time/all_images_speed_up.png')
plt.clf()

for module in vis_results.keys():
     avr_speed_up = vis_results[module][0]
     plt.plot(np.arange(16), [avr_speed_up]*16, label=module)
     plt.legend()
     plt.title('Average speed up for all images')
     plt.ylabel('Average speed up')

plt.savefig('running_time/avr_speed_up.png')
