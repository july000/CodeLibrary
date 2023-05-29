import json
import os
import urllib3
import time
from concurrent.futures import ThreadPoolExecutor
http_connection_pool = urllib3.PoolManager()


xiandai_url = "http://10.66.12.37:30080/xiandai/adscene/rawdata"
dev_url = "http://10.66.12.37:30080/default/adscene/rawdata"
lingshutest_url = "http://10.66.12.37:30080/lingshutest/adscene/rawdata"

def load_local_file_content(path):
    with open(path, 'rb') as file:
        return file.read()


def upload_single_case(url, csv_file_path, xodr_file_path, meta, xodr_filename, csv_filname):
    csv_data = load_local_file_content(csv_file_path)
    xodr_data = load_local_file_content(xodr_file_path)
    # video_data = load_local_file_content(video_path)

    # 导入原始数据
    res_import = http_connection_pool.request('POST', url, 
                                        fields={
                                        'meta':json.dumps(meta),
                                        'map': (xodr_filename, xodr_data),
                                        'mix_trajectory':(csv_filname, csv_data),
                                        # 'front_video':('front_video',video_data)
                                        })
    
    print(str(res_import.data))

def uppp():
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

def check_translate_status(process_id):
    failed_case = {}
    res_transform = http_connection_pool.request('GET', "http://10.66.12.37:31666/scene-processes/" + str(process_id))
    res_transform_data = json.loads(res_transform.data.decode())
    print(res_transform_data['raw_data_info']['xodr_filename'], res_transform_data['raw_data_info']['traj_filename'])
    vid = res_transform_data['raw_data_info']['traj_filename'].split('.origin.csv')[0]
    
    scene_status = res_transform_data['scene_status']
    # if scene_status == 4:
    #     failed_case[]
        
    


def parallel_upload_cases(input_dir, thread_pool, xodr_file_path, data_source, xodr_filename, csv_filname, start_idx, end_idx):
    for i, case_name in enumerate(os.listdir(input_dir)):
        if start_idx <= i <= end_idx:
            case_path = os.path.join(input_dir, case_name)
            csv_file_path = os.path.join(case_path, 'haomo_flat.csv')
            thread_pool.submit(upload_single_case, csv_file_path, xodr_file_path, {'map_type':'xodr', 'data_source':data_source}, xodr_filename, csv_filname)



if __name__ == '__main__':
    # csv_file_path = 'D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\\demo\\lixiang\\demo_case\\traj.csv'
    # xodr_file_path = 'D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\demo\\lixiang\\demo_case\\map.xodr'
    # video_file_path = 'D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\demo\\lixiang\\demo_case\\video.mp4'
    
    # thread_pool = ThreadPoolExecutor(max_workers=5)
    # input_dir = "\\\\10.66.9.58\\share2\\datamining\\scenarios\\haomo\\1210\\processed\\osc\\"
    # xodr_path = "\\\\10.66.9.58\\share2\\datamining\\scenarios\\haomo\\map_no_signal.xodr"
    # parallel_upload_cases(input_dir, thread_pool, xodr_path, 'haomo', 'haomo_4188.xodr', 'haomo_flat.csv', 0, 30)

    # check_translate_status(5054)
    # csv_file_path = '\\\\10.66.9.58\\share2\\datamining\\scenarios\\haomo\\1210\\processed\\osc\\hibag_V71R003_default_013_20211210100844_20211210100940\\haomo_flat.csv'
    # xodr_file_path = "\\\\10.66.9.58\\share2\\datamining\\scenarios\\haomo\\map_no_signal.xodr"

    # csv_file_path = 'C:\\Users\\junmei\\Documents\\WXWork\\1688853099564451\\Cache\\File\\2023-05\\rosbag-xodr-parse-production-375-lc_5677_test\\rosbag2.csv'
    # xodr_file_path = "C:\\Users\\junmei\\Documents\\WXWork\\1688853099564451\\Cache\\File\\2023-05\\rosbag-xodr-parse-production-375-lc_5677_test\\2023_03_31_05_36_35_zlog.xodr"

    # csv_file_path = "D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\\015\\rosbag2.csv"
    # xodr_file_path = "D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\\lingshu\\2023419\\2023_04_14_02_23_09_ehp_output.xodr"


    csv_file_path = "C:\\Users\\junmei\\Documents\\WXWork\\1688853099564451\\Cache\\File\\2023-05\\rosbag-xodr-parse-production-375-lc_5677_test\\rosbag2.csv"
    xodr_file_path = "C:\\Users\\junmei\\Documents\\WXWork\\1688853099564451\\Cache\\File\\2023-05\\rosbag-xodr-parse-production-375-lc_5677_test\\2023_03_31_05_36_35_zlog.xodr"

    upload_single_case(lingshutest_url, csv_file_path, xodr_file_path, {'map_type':'xodr', 'data_source':'lingshu'}, 'lingshu__0529_2023_03_31_05_36_35_zlog.xodr', 'lingshu.csv')

