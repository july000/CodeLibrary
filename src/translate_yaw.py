import pandas as pd

def run(csv):
    #     | y轴(90)                           |x(0)
    #     |                                   |
    #     |                                   |
    # -------------- x轴(0)       ------------------------- y(90)
    #     | 
    #         ()                              | (180)
    # 将右边的正北为零度，顺时针增加的角度转换成左边的正东为零度，逆时针增加
    df = pd.read_csv(csv)
    df['Yaw'] = (90.0-df['Yaw'])%360.0
    df.to_csv(csv, index=False)
    return
if __name__=='__main__':
    run("D:\\cybertron\\Cybertron\\Tools\\TrajectoryProcess\\test\\demo\\testi.csv")

