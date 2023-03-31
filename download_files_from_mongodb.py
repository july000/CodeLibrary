import requests
import sys
import os
import json
import pandas as pd

cmd = 'set PYTHONPATH=$PYTHONPATH:'+os.path.dirname(__file__)
os.system(cmd)
print(sys.path)
def download_file(url, save_file):
    r = requests.get(url, allow_redirects = True)

    with open(save_file, 'wb') as f:
        f.write(r.content)

    if url.split('.')[-1] == 'xosc':
        with open(save_file, 'r') as f:
            content = f.read()
            idx = content.find('xodr')
            odr_name = content[idx - 37: idx + 4]
            content = content.replace(odr_name, 'test.xodr')

        with open(save_file, 'w') as f:
            f.write(content)

def test_from_csv_odr_url(csv_url, odr_url):
    file_type = csv_url.split('.')[-1]
    if file_type == 'xosc':
        local_csv_or_osc = os.path.dirname(__file__)+'\\sample_case\\test.xosc'
    elif file_type == 'csv':
        local_csv_or_osc = os.path.dirname(__file__)+'\\sample_case\\test.csv'
    else:
        local_csv_or_osc = os.path.dirname(__file__)+'\\sample_case\\test.json'

    local_odr = os.path.dirname(__file__)+'\\sample_case\\test.xodr'

    download_file(csv_url, local_csv_or_osc)
    download_file(odr_url, local_odr)

def read_json(file_path):

    with open(file_path) as f:
        data = json.load(f)

        osc_actions = data['osc_actions']
        df = pd.json_normalize(osc_actions)
        # df = df['time'].apply(pd.Series,index=['start_time','end_time'])
        s=pd.DataFrame([[x] + [y] for x, y in df.time], columns=['start_time','end_time'])
        df = pd.concat([df, s], axis=1)
        df.to_csv(file_path+".csv", index=False)
        df_gp = df.groupby('id')
        for gp in df_gp:

            print(gp)
            print("="*30)

        # df2 = df.drop_duplicates(subset=['start_time' , 'id', 'type'], keep='first', inplace = True, ignore_index = True)
        # df2.to_csv(file_path+"_drop_duplicates.csv", index=False)
        # for action in osc_actions:
        #     time = action['time']
        #     id = action['id']
        #     type = action['type']
        #     print("id = {}, type = {}, time = {}".format(id, type, time))

if __name__ == '__main__':
    test_from_csv_odr_url(
        'http://10.66.12.37:30050/api/storage/filestore/trajectory_xosc?project-name=public&filename=bcc5916d-e933-4301-97f8-8767390f9151.semantic',
        'http://10.66.12.37:30050/api/storage/filestore/trajectory_xodr?project-name=public&filename=32c23586-841d-415d-9840-412d9a3875cf.xodr'
    )
    # read_json(os.path.dirname(__file__)+'\\sample_case\\ts.json')