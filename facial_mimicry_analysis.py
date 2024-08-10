import numpy as np

# Define event tuple (c, a, t)
Event = namedtuple('Event', ['cat', 'action', 'time'])

##### TODO: load the real data, below we probide an example #####
# Sample events representing interactions between two cats (signaler and responder)
events = [
    Event('s', 'AU25', 0.0),
    Event('s', 'AU26', 0.3),
    Event('r', 'AU25', 0.3),
    Event('s', 'EAD102', 0.45),
    Event('r', 'AU26', 0.45),
    Event('s', 'EAD104', 1.00),
    Event('r', 'AU47', 1.00),
    Event('r', 'EAD104', 1.15),
    Event('r', 'EAD105', 2.00)
]

# Define time windows of size 1 second
def create_time_windows(events, window_size=1.0):
    time_windows = []
    for i in range(len(events)):
        window_start = events[i].time
        window_end = window_start + window_size
        window_events = [e for e in events if window_start <= e.time <= window_end]
        time_windows.append(window_events)
    return time_windows

# Function to calculate RMsize (counting rapid mimicry instances)
def calculate_rm_size(S, R):
    return len(set(S) & set(R))

# Function to calculate RMratio (ratio of mimicry)
def calculate_rm_ratio(S, R):
    intersection = len(set(S) & set(R))
    union = len(set(S) | set(R))
    return intersection / union if union > 0 else 0

# Aggregate RMsize and RMratio over all windows
def aggregate_metrics(windows):
    rm_size = []
    rm_ratio = []
    for window in windows:
        S = [e.action for e in window if e.cat == 's']
        R = [e.action for e in window if e.cat == 'r']
        rm_size.append(calculate_rm_size(S, R))
        rm_ratio.append(calculate_rm_ratio(S, R))
    avg_rm_size = np.mean(rm_size)
    avg_rm_ratio = np.mean(rm_ratio)
    return avg_rm_size, avg_rm_ratio

# Create windows and calculate metrics
windows = create_time_windows(events)
avg_rm_size, avg_rm_ratio = aggregate_metrics(windows)

print(f"Average RMsize: {avg_rm_size}")
print(f"Average RMratio: {avg_rm_ratio}")

from collections import Counter

def find_frequent_combinations(events, n=2):
    combinations = [tuple([e.action for e in events[i:i+n]]) for i in range(len(events)-n+1)]
    return Counter(combinations).most_common()

frequent_combinations = find_frequent_combinations(events, n=2)
print(f"Frequent 2-grams: {frequent_combinations}")
