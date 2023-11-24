import requests
import io
import pandas as pd

def download_file(url, url_type):
    r = requests.get(url, allow_redirects = True)
    input_data = io.BytesIO(r.content)
    if url_type == 'csv':
        df = pd.read_csv(input_data)
        groupby_df = df.groupby('ID')
    elif url_type == 'judge':
        data = pd.read_json(input_data)
    elif url_type == 'xodr':
        data = pd.read_xml(input_data)
    elif url_type == 'xosc':
        data = pd.read_xml(input_data)
    
    print()

csv_url = 'http://10.66.12.37:30050/api/storage/filestore/trajectory_source_data?project-name=public&filename=525c7b32-f506-401b-aae5-6f6642fcc4f7.origin.csv'


judge_url = 'http://10.66.12.37:30050/api/storage/filestore/trajectory_xosc?project-name=public&filename=420334c4-8dd8-4ce3-9d8b-32eaa86b160d.judge'
download_file(judge_url, 'judge')
