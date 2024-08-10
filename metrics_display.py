### display mimicry metrics from the constructed files

import numpy as np
size_list = np.load("size_metricNA.npy", allow_pickle=True)
fullnes_list = np.load("fullness_metricNA.npy", allow_pickle=True)
size_video_means = np.array([np.nanmean([inner_val for inner_val in val if inner_val > 0]) for val in size_list])
fullness_video_means = np.array([np.nanmean([inner_val for inner_val in val if inner_val > 0]) for val in fullnes_list])

print("size")
print(np.min([val for val in size_video_means if not np.isnan(val)]))

print(np.max([val for val in size_video_means if not np.isnan(val)]))

print(np.nanmean(size_video_means))

print(np.nanstd(size_video_means))

print(np.median([val for val in size_video_means if not np.isnan(val)]))

print("fullness")
print(np.min([val for val in fullness_video_means if not np.isnan(val)]))
print(np.max([val for val in fullness_video_means if not np.isnan(val)]))
print(np.nanmean(fullness_video_means))
print(np.nanstd(fullness_video_means))
print(np.median([val for val in fullness_video_means if not np.isnan(val)]))
