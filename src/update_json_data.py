import os
import json
import pandas as pd
import numpy as np

def change_map(input_dir):
    for case in os.listdir(input_dir):
        case_path = os.path.join(input_dir, case)
        if os.path.isfile(case_path):
            continue
        file_num = len(os.listdir(case_path))
        if file_num == 0:
            continue
        meta_json = os.path.join(case_path, 'haomo_flat.meta.json')
        if os.stat(meta_json).st_size == 0:
            continue
        with open(meta_json, 'r') as f:
            data = json.load(f)
            data['map'] = 'haomo_signal_new.xodr'
        with open(meta_json, 'w') as f1:
            # print(data['map'])
            json.dump(data, f1, indent=4)

def drop(csv_file):
    df = pd.read_csv(csv_file)
    df = df[df['Category']!='lane']
    df.loc[df['Ego'] == 'Y', 'Category'] = 'vehicle'
    df.loc[df['Ego'] == 'Y', 'Style'] = 'car'

    df.to_csv(csv_file, index=False)
    

if __name__ == '__main__':
    # path = 'D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\\demo\\haomo'
    # change_map(path)
    csv_file = 'D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\\0901-1028-01\\end\\fix-02\\haomo_flat.csv'
    drop(csv_file)
            
