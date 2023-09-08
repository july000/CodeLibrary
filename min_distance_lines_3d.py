import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.optimize import fsolve

def line_to_line(A, B, C, D):
    '''
    Calculate the shortest distance between two lines AB and CD in 3D space.

    3D空间中的线的位置关系：
    1.重合
    2.平行
    3.相交（垂直是相交的特殊情况）
    4.异面

    重合和平行的时候，两条线的方向向量的叉乘是零向量，利用模长判断是否是重合与平行
        重合的最短距离是0
            重合的最短距离也是同样的方式计算，只是计算出来的是0
        平行的最短距离计算方法是：
            线的方向向量与两条线分别穿过的点构成的向量的叉乘的模长/叉乘向量的模长
            就是计算平行四边形的高

    相交是同一个平面内的两条直线的相交，判断叉乘与两条线分别穿过的点构成的向量的点乘是否为零，此时，最短距离就是0
    可以和异面的计算合为同一类，因为此时是分子为0

    异面直线
    思路是求出叉乘向量
    构建方程：叉乘向量与直线上的两点构成的向量的点乘是0，表示这两个向量垂直
    w(p-p0)=0
    w(q-q0)=0

    w(p-p0) = w(q-q0)
    w(p-q) = w(p0-q0)
    两边同时取模长
    |p-q| = |w|*|p0-q0|/|w|
    '''

    AB = B - A  # dir_v1
    CD = D - C  # dir_v2
    AC = C - A  # dir_ss

    cross = np.cross(AB, CD)
    cross_norm = np.linalg.norm(cross)

    if cross_norm == 0:  # parallel
        return np.linalg.norm(np.cross(AB, AC)) / np.linalg.norm(AB)
    else:
        return np.linalg.norm(np.dot(AC, cross)) / cross_norm

def point_to_line_segment(P, A, B):
    '''
    Calculate the shortest distance from point P to line segment AB in 3D space.
    return min_dis, is_endpoint(最短距离的计算是否来自线段AB的某一个端点与P的距离)
    '''

    AB = B - A
    AP = P - A
    BP = P - B
    if np.dot(AB, AP) < 0:
        '''
            P *

                    A _____________ B

        '''
        return np.linalg.norm(AP), True
    elif np.dot(AB, BP) > 0:
        '''
                                P *

            A _____________ B

        '''
        return np.linalg.norm(BP), True
    else:
        '''
                     P *

            A _____________ B

        '''
        return np.linalg.norm(np.cross(AB, AP)) / np.linalg.norm(AB), False

def line_segment_distance(A, B, C, D):
    '''
    Calculate the shortest distance between two line segments AB and CD in 3D space.
    Each of A, B, C, D is a numpy array representing a point in 3D space.
    '''
    dis1, is_endpoint1 = point_to_line_segment(A, C, D)
    dis2, is_endpoint2 = point_to_line_segment(B, C, D)
    dis3, is_endpoint3 = point_to_line_segment(C, A, B)
    dis4, is_endpoint4 = point_to_line_segment(D, A, B)
    dis = line_to_line(A, B, C, D)
    # print(is_endpoint1, is_endpoint2, is_endpoint3, is_endpoint4)
    # print(dis1, dis2, dis3, dis4, dis)
    
    # 
    return min(dis1, dis2, dis3, dis4) if is_endpoint1 or is_endpoint2 or is_endpoint3 or is_endpoint4 else min(dis1, dis2, dis3, dis4, dis)

def line_segment_distance_by_diff(A, B, C, D):
    '''
    建模思想
    seg1:AB
    seg2:CD
    p:A+m(B-A)
    q:C+m(D-C)
    dis(p,q) ** 2 = |p-q|*|p-q| = [(A-C) + m(B-A) - n(D-C)]*[(A-C) + m(B-A) - n(D-C)]
                  = |A-C|**2 
    求dis(p,q)的最小值，分别对m, n求导，令倒数为0，求解方程组
    如果m，n是否在[0,1]之间
    '''
    AB = B - A  # dir_v1
    CD = D - C  # dir_v2
    AC = C - A  # dir_ss

    m = sp.Symbol('m')
    n = sp.Symbol('n')
    p = A + m*AB
    q = C + n*CD

    expr = np.dot((q-p), (q-p))

    der_m = sp.diff(expr, m)
    der_n = sp.diff(expr, n)
    equations = [sp.Eq(der_m, 0), sp.Eq(der_n, 0)]
    solution = sp.solve(equations, (m, n))

    if 0 <= solution[m] <= 1 and 0 <= solution[n] <= 1:
        dis = expr.subs([(m, solution[m]), (n, solution[n])])
    else:
        dis1, is_endpoint1 = point_to_line_segment(A, C, D)
        dis2, is_endpoint2 = point_to_line_segment(B, C, D)
        dis3, is_endpoint3 = point_to_line_segment(C, A, B)
        dis4, is_endpoint4 = point_to_line_segment(D, A, B)
        dis = min(dis1, dis2, dis3, dis4)

    return dis

def plot_3d_line_segment(pointA, pointB):
    x1, y1, z1 = pointA
    x2, y2, z2 = pointB
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot([x1, x2], [y1, y2], [z1, z2])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

if __name__ == '__main__':



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
    dis = line_segment_distance_by_diff(A, B, C, D)
    print(dis)

    # plot_3d_line_segment(A, B)
