
#  pip install asammdf[gui]
# https://asammdf.readthedocs.io/en/latest/gui.html#general-shortcuts
















# import cantools

# # 加载数据库文件（DBC）
# db = cantools.database.load_file('path/to/your/file.dbc')

# # 加载 MF4 文件
# mf4_file = cantools.db.load_file('G:\\wxwork\\WXWork\\1688853099564451\\Cache\\File\\2023-07\\Gen5_2022-06-27_14-37_0102.MF4', database=db)

# # 获取信号数据
# signal_data = mf4_file.get_signals()

# # 读取信号数据
# for signal in signal_data:
#     data = signal.data
#     timestamps = signal.timestamps

#     # 打印数据和时间戳示例
#     for timestamp, value in zip(timestamps, data):
#         print(f"Timestamp: {timestamp}, Value: {value}")



from distutils.command.install_egg_info import to_filename
import asammdf

# 加载 MF4 文件
mdf_file = asammdf.MDF('G:\\wxwork\\WXWork\\1688853099564451\\Cache\\File\\2023-07\\Gen5_2022-06-27_14-37_0102.MF4')
i = 0
all_channels = []
for group in mdf_file.groups:
    for channel in group['channels']:
        print(channel.name)
        print(channel.comment)
        print(channel.data_type)
        print("==============================================")
#         all_channels.append(channel.name)
# print(all_channels)
# for m in mdf_file.iter_channels():
#     if i >= 2:
#         break
#     print(m)
#     print(dir(m))
#     i += 1

# df = mdf_file.to_dataframe()
# print(df.head())
# # 获取信道数据
# channel_data = mdf_file.iter_to_dataframe()

# # # 读取信道数据
# data = channel_data.samples

# # # 获取时间戳
# timestamps = channel_data.timestamps

# # # 打印数据和时间戳示例
# for timestamp, value in zip(timestamps, data):
#     print(f"Timestamp: {timestamp}, Value: {value}")