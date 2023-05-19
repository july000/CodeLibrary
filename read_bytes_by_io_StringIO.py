import csv
import pandas as pd
import io
import time 
path1 = "F:\\renjunmei007\\05_code\\back\\51World\\Cybertron\\Modules\\Judge\\Source\\python\\offline_analyze\\sample_case\\real\\test.csv"
path2 = "D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\\lingshu\\20230510\\rosbag2.csv"
path3 = "F:\\renjunmei007\\05_code\\back\\51World\\bigdata-platform\\flink-jobs\\fill_acc_with_splrep\\test.csv"
path4 = "D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\\lingshu\\20230510\\rosbag2_test.csv"
# data = open(path, 'rb')
# print((data))

'''

bytes_data = b'ID,Time,PositionX,PositionY,PositionZ,Length,Width,Height,Yaw,Pitch,Roll,VX,VY,VZ,AX,AY,AZ,Category,Style,Color,Ego\\r\\n0,0.0,1828.3321077692322,1010.3354878711103,0.0,4.5,2.0,1.5,53.26705692361665,2.903294808077085,-0.7113696781820684,4.952797141535555,6.54796090925898,0.0,-0.6219329433906972,-0.8389157013057953,0.0,vehicle,car,,Y\\r\\n0,0.0500466,1828.5792073349905,1010.662155509194,0.0,4.5,2.0,1.5,53.25293956879114,2.848880059967895,-0.6934547761027869,4.922137535534822,6.506878660673878,0.0,-0.603309370801829,-0.8028441219430481,0.0,vehicle,car,,Y\\r\\n'
# with open(path, 'rb') as f:
#     da = f.read()
#     print(type(da), da)

# bio = io.BytesIO(bytes_data)
# ddd = bio.read()
# print(ddd)


content = bytes_data.decode()
file = io.StringIO(content)
csv_data = csv.reader(file, delimiter=",")
# for row in csv_data:
#     print(row)

# df = pd.read_csv(csv_data)
# print(df)
# print(csv_data)


from io import BytesIO
data = BytesIO(bytes_data)
df = pd.read_csv(data)
df['Ego'] = 'N'
# sss = df.to_records(index=False).tostring()
# print(sss.decode('UTF-8'))

stream = io.StringIO()
df.to_csv(stream, sep=",", index=False)

fff = stream.getvalue().encode('utf-8')

data2 = BytesIO(fff)
df2 = pd.read_csv(data2)
print(df2)
# fff = BytesIO(sss)
# df2 = pd.read_csv(fff)
# print(df2)

'''

def get_file_byte(path):
    with open(path, 'rb') as f:
        data = f.read()
        return data

def write_to_file(data, path):
    with open(path, 'wb') as f:
        f.write(data)


def change_by_file(path):
    file_start_time = time.time()
    data = get_file_byte(path)
    tmp = path.split('.csv')[0]+'_tmp.csv'
    write_to_file(data, tmp)
    df = pd.read_csv(tmp)
    start_time = df.loc[:, 'Time'].min()
    df['Time'] = df['Time'] - start_time + 20230518.0
    df.sort_values(by=['ID', 'Time'], inplace = True)
    df.to_csv(tmp, index=False)

    # print("change_by_file spent time = %f"%(time.time() - file_start_time))
    return time.time() - file_start_time

def change_by_stream(path):
    stream_start_time = time.time()
    data = get_file_byte(path)
    input_data = io.BytesIO(data)
    df = pd.read_csv(input_data)
    start_time = df.loc[:, 'Time'].min()
    df['Time'] = df['Time'] - start_time + 20230518.0
    df.sort_values(by=['ID', 'Time'], inplace = True)
    stream = io.StringIO()
    df.to_csv(stream, sep=",", index=False)
    fff = stream.getvalue().encode('utf-8')
    # print("change_by_file spent time = %f"%(time.time() - stream_start_time))
    return time.time() - stream_start_time

def copy_df(path):
    df = pd.read_csv(path)
    new_df = pd.concat([df, df, df, df, df, df, df, df, df, df, df, df, df, df, df, df, df, df, df, df, df, df, df, df])
    new_df.to_csv(path, index=False)

copy_df(path4)
t1 = 0.0
t2 = 0.0
for i in range(1):
    # print('================== i  = %d ============='%i)
    t1 += change_by_file(path4)
    t2 += change_by_stream(path4)
print(t1, t2)
