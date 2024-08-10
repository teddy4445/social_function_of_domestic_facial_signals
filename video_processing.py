### This code uses model introduced in Martvel et al. (2024) paper (could be found in citations). 
import sys
sys.path.append('/AnimalFace')
from detect import *
from verify import *

models = load_models(root+'/AnimalFace/weights')

import os
import zipfile
import re
import torch
from torchvision.transforms import Compose, Resize, CenterCrop, ToTensor, Normalize
import pandas as pd

zip_dir = '/CatCafe/Raw Videos' ### original data

wmv_files = []

for root, dirs, files in os.walk(zip_dir):
    for file in files:
        if file.endswith('.mp4'):
            file_path = os.path.join(root, file)
            wmv_files.append(file_path)

def process_video(input_file, sec, output):
    name = input_file[53:]
    vid_name = name.split('/')[-1][:-4]
    cap = cv2.VideoCapture(input_file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    un_ids = []
    frame_count = 0
    vlandmarks = []
    vframe_count = []
    vtime_sec = []
    vconf = []
    vyconf = [] 
    ids = []
    lm = []

    empty = 0
    multy = 0
    nocatY = 0
    bcat = 0
    gcat = 0
    sframes = 0

    video_statistics = {}
    video_statistics['video_name'] = vid_name
    video_statistics['total_frames'] = total_frames

    csv_file_path = os.path.join(output, f"{vid_name}.csv")

    for i in tqdm(range(total_frames), "Processing " + csv_file_path):
        ret, frame = cap.read()
        if ret:
            if frame_count % int(fps * sec) == 0:
                sframes += 1
                time_sec = frame_count / fps
                lmks = locate(frame, models, tracking = False)

                if lmks is not None:
                    for instance in lmks:
                        landmarks = instance[0]
                        yconf = instance[1]
                        lm.append(landmarks)
                        vyconf.append(yconf)
                        vframe_count.append(frame_count)
                        vtime_sec.append(time_sec)

                else:
                    vyconf.append(0)
                    lm.append(0)
                    vframe_count.append(frame_count)
                    vtime_sec.append(time_sec)
                    empty += 1

            frame_count += 1
        else:
            break

    cap.release()

    frame_data = pd.DataFrame({
        'frame_count': pd.Series(vframe_count),
        'time_sec': pd.Series(vtime_sec),
        'id': pd.Series(ids),
        'conf': pd.Series(vyconf),
        #'conf': pd.Series(vconf),
        'landmarks': pd.Series(lm)
    })

    with open(csv_file_path, 'w') as f:
        frame_data.to_csv(f, index=False)

    return vid_name, vframe_count, vtime_sec, vconf, vlandmarks, sframes, empty, multy, nocatY, bcat, gcat

# Initialize folder for storing CSV files
output_folder = '/CatFACS_test/'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for fil in wmv_files:
    au = fil.split('/')[-2].split(' ')[1]
    fold = output_folder+au
    if not os.path.exists(fold):
        os.makedirs(fold)

import pandas as pd

names = []
f_frames = []
c_frames = []

for video_file in wmv_files[54:]:
    vid_name, vframe_count, vtime_sec, vconf, vlandmarks, sframes, empty, multy, nocatY, bcat, gcat = process_video(video_file, 0.1, output_folder)
