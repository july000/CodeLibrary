import pandas as pd
import numpy as np
path = "G:\\wxwork\\WXWork\\1688853099564451\\Cache\\File\\2023-11\\csv-geojson\\vehicle_data.csv"
split_folder = "G:\\wxwork\\WXWork\\1688853099564451\\Cache\\File\\2023-11\\csv-geojson\\\\split_traj\\"
df = pd.read_csv(path)
df = df.sort_values(['ID', 'Time'])
# print(df['Time'].min(), df['Time'].max(), df['Time'].max() - df['Time'].min())
split_time_gap = 60
# gf = df.groupby('Time')

t_min = df['Time'].min()
t_max = df['Time'].max()
# print(t_min, t_max, int(np.ceil(t_max)))
time_segs = [i for i in range(int(t_min), int(np.ceil(t_max)), int(split_time_gap))] + [int(np.ceil(t_max))]
for i in range(len(time_segs)-1):
    time = [time_segs[i], time_segs[i+1]]
    subd_df = df[(df['Time'] >= time[0]) & (df['Time'] < time[1])]
    subd_df['PositionZ'] = 0.0
    subd_df.sort_values(by=['ID', 'Time'], inplace=True)
    subd_df.to_csv(split_folder + "vehicle_data_enu_60s_%d.csv"%i, index=False)

