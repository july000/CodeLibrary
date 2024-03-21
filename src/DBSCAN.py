from sklearn import datasets
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import copy
import math

# 基本概念
# https://cloud.tencent.com/developer/article/1827291
# 1. 邻域
# 2. 核心对象 core object ： 如果一个点的邻域内的点的个数大于minPtrs， 则称该点是核心对象
# 3. 密度直达：如果xj是xi邻域内的一个点，且xi是核心对象，则它们之间是密度直达的
# 4. 密度可达：经过序列，序列内相邻两点是密度直达，则称首尾两点是密度可达的
# 5. 密度相连：两个点均可以通过另外一个点密度可达，则这两个点是密度相连的

# 1. 定义半径阈值，minPtrs
# 2. 遍历所有的样本点，确定核心对象集合，这个集合中都是核心对象
# 3. 循环遍历核心对象集合，当集合不空的时候，为每个核心对象船舰一个队列，自己先入队，
# 当队列不空的时候，依次将其邻域内的点都加入队列，直至这个队列为空停止，
# 此时的数据集中已经不包含这个簇的样本点了，外层循环的时候，记录的样本集合见此内层循环时的样本集合，就得到了该簇的样本点
def get_dis(x, y):
    return np.sqrt(np.sum(np.square(x-y)))

def get_neighbers(datas, pt, theta):
    neighbers = []
    for data in datas:
        if get_dis(data, pt) <= theta:
            neighbers.append(data)
    return neighbers

def get_core_objs(datas, theta, minPtr):
    core_objs = []
    for data in datas:
        neibs = get_neighbers(datas, data, theta)
        if len(neibs) >= minPtr:
            core_objs.append(data)

def get_cluters(datas, theta, minPtr):
    core_objs = get_core_objs(datas, theta, minPtr)
    k = 0
    clusters = []
    for core_obj in core_objs:
        cur_datas = copy.deepcopy(datas)
        datas -= core_obj
        queue = [core_obj]
        while queue:
            front = queue.pop(0)
            neighbers = get_neighbers(front)
            for nb in neighbers:
                queue.append(nb)
            datas -= neighbers
        k+=1
        cluster = cur_datas - datas
        clusters.append(cluster)
    return clusters

X1, y1 = datasets.make_circles(n_samples=2000, factor=.6, noise=.02)
X2, y2 = datasets.make_blobs(n_samples=400, n_features=2, centers=[[1.2, 1.2]], cluster_std=[[.1]], random_state=9)
X = np.concatenate((X1, X2))
print(type(X[0]))
eps = 0.08
min_Pts = 10
begin = time.time()
C = get_cluters(X, eps, min_Pts)
end = time.time()
plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=C)
plt.show()