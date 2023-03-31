from asyncio.windows_events import NULL
import json
import os
import urllib3
import time

def load_local_file_content(path):
    with open(path, 'rb') as file:
        return file.read()

http_connection_pool = urllib3.PoolManager()

def upload_single_case(csv_file_path, xodr_file_path, video_path=None):
    meta = {}
    meta["map_type"] = "xodr"
    meta["data_source"] = "lixiang"
    meta = json.dumps(meta)

    case_number = os.path.dirname(csv_file_path).split('\\')[-1]
    print(case_number)
    csv_data = load_local_file_content(csv_file_path)
    xodr_data = load_local_file_content(xodr_file_path)
    video_data = load_local_file_content(video_path)

    # 导入原始数据
    res_import = http_connection_pool.request('POST', "http://10.66.12.37:30080/default/adscene/rawdata", 
                                        fields={
                                        'meta':meta,
                                        'map': (case_number, xodr_data),
                                        'mix_trajectory':("traj_csv", csv_data),
                                        'front_video':('front_video',video_data)
                                        })
    
    print(str(res_import.data))
    res_import_data = json.loads(res_import.data.decode())
    process_id = res_import_data['process_id']
    transform_process_id = process_id + 1

    time.sleep(5)

    # 根据process-id拿到scene-id
    while True:
        res_transform = http_connection_pool.request('GET', "http://10.66.12.37:31666/scene-processes/" + str(transform_process_id))
        # print(str(res_transform.data))
        res_transform_data = json.loads(res_transform.data.decode())
        scene_status = res_transform_data['scene_status']
        if scene_status == 2:
            scene_id = res_transform_data['scene_id']
    
            # 根据scene-id拼出可视化的url
            scene_url = 'http://10.66.12.37:30050/api/visualization/?scene_id='+scene_id+'=front&data_url=ws://10.66.12.37:31888/visualization'

            # print(case_number, scene_url)
            return (case_number, scene_url)
        elif scene_status == 4:
            return (-1, "transform failed")


if __name__ == '__main__':
    csv_file_path = 'D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\\demo\\lixiang\\demo_case\\traj.csv'
    xodr_file_path = 'D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\demo\\lixiang\\demo_case\\map.xodr'
    video_file_path = 'D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\demo\\lixiang\\demo_case\\video.mp4'
    
    case_number, scene_url = upload_single_case(csv_file_path, xodr_file_path, video_file_path)
