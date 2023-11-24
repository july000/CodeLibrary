import numpy as np


def line_to_line(A, B, C, D):
    """Calculate the shortest distance between two lines AB and CD in 3D space."""

    AB = B - A
    CD = D - C
    AC = C - A

    cross = np.cross(AB, CD)
    cross_norm = np.linalg.norm(cross)

    if cross_norm == 0:  # parallel
        return np.linalg.norm(np.cross(AB, AC)) / np.linalg.norm(AB)
    else:
        return np.linalg.norm(np.dot(AC, cross)) / cross_norm

def point_to_line_segment(P, A, B):
    """Calculate the shortest distance from point P to line segment AB in 3D space."""

    AB = B - A
    AP = P - A
    BP = P - B
    if np.dot(AB, AP) < 0:
        return np.linalg.norm(AP), True
    elif np.dot(AB, BP) > 0:
        return np.linalg.norm(BP), True
    else:
        return np.linalg.norm(np.cross(AB, AP)) / np.linalg.norm(AB), False

def line_segment_distance(A, B, C, D):
    """Calculate the shortest distance between two line segments AB and CD in 3D space.

    Each of A, B, C, D is a numpy array representing a point in 3D space.
    """
    dis1, is_endpoint1 = point_to_line_segment(A, C, D)
    dis2, is_endpoint2 = point_to_line_segment(B, C, D)
    dis3, is_endpoint3 = point_to_line_segment(C, A, B)
    dis4, is_endpoint4 = point_to_line_segment(D, A, B)
    dis = line_to_line(A, B, C, D)
    print(is_endpoint1, is_endpoint2, is_endpoint3, is_endpoint4)
    print(dis1, dis2, dis3, dis4, dis)
    return min(dis1, dis2, dis3, dis4) if is_endpoint1 or is_endpoint2 or is_endpoint3 or is_endpoint4 else min(dis1, dis2, dis3, dis4, dis)



def distance_between_segments(A1, A2, B1, B2):
    # 计算两条线段的差向量
    D1 = A2 - A1
    D2 = B2 - B1

    # 计算两个差向量的点积
    dot_D1_D1 = np.dot(D1, D1)
    dot_D2_D2 = np.dot(D2, D2)
    dot_D1_D2 = np.dot(D1, D2)

    # 计算参数 t1 和 t2
    t1 = (np.dot(D1, D2) * np.dot(D2, D1) - np.dot(D1, D1) * np.dot(D2, D2)) / (np.dot(D1, D1) * np.dot(D2, D2) - np.dot(D1, D2) * np.dot(D2, D1))
    t2 = (np.dot(D1, D2) * np.dot(D1, D2) - np.dot(D1, D1) * np.dot(D2, D2)) / (np.dot(D1, D1) * np.dot(D2, D2) - np.dot(D1, D2) * np.dot(D2, D1))

    # 计算最短距离的平方
    distance_squared = np.linalg.norm((A1 + t1 * D1) - (B1 + t2 * D2)) ** 2

    # 如果最短距离小于等于零，则两条线段相交或部分重合
    if distance_squared <= 0:
        return 0

    # 返回最短距离
    return np.sqrt(distance_squared)

# 示例用法
# A1 = np.array([1, 2, 3])
# A2 = np.array([4, 5, 6])
# B1 = np.array([7, 8, 9])
# B2 = np.array([10, 11, 12])

# distance = distance_between_segments(A1, A2, B1, B2)
# print("最短距离:", distance)

# A =np.array([1,2,0])
# B =np.array([4,2,0])
# C =np.array([3,4,0])
# D =np.array([6,4,0])

# DIS = line_segment_distance(A, B, C, D)
# print(DIS)

A=np.array([13.43, 21.77, 46.81])
B=np.array([27.83, 31.74, -26.60])
C=np.array([77.54, 7.53, 6.22])
D=np.array([26.99, 12.39, 11.18])

DIS = line_segment_distance(A, B, C, D)
print(DIS)

DIS = distance_between_segments(A, B, C, D)
print(DIS)