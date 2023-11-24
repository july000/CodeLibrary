import pandas as pd
input_file = 'D:\cybertron\Cybertron\Tools\TrajectoryProcess\\test\lingshu\\20221201\\test.csv'
df = pd.read_csv(input_file)
start_time = df.loc[:,'Time'].min()
df['Time'] = df['Time'] - start_time

output_file = input_file.split('.csv')[0]+'_fixed.csv'
df.to_csv(output_file, index=False)

f = open(output_file, 'rb')
data = f.read()
print(data)