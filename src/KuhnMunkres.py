import numpy as np
import math

# Kuhn-Munkres匹配算法
class KMMatch(object):

    def __init__(self, graph):
        assert isinstance(graph, np.ndarray), print("二分图的必须采用numpy array 格式")
        assert graph.ndim == 2, print("二分图的维度必须为2")
        self.graph = graph

        rows, cols = graph.shape
        self.rows = rows
        self.cols = cols

        self.lx = np.zeros(self.cols, dtype=np.float32)  # 横向结点的顶标
        self.ly = np.zeros(self.rows, dtype=np.float32)  # 竖向结点的顶标

        self.match_index = np.ones(cols, dtype=np.int32) * -1  # 横向结点匹配的竖向结点的index （默认-1，表示未匹配任何竖向结点）
        self.match_weight = 0  # 匹配边的权值之和

        self.inc = math.inf

    def match(self):
        # 初始化顶标, lx初始化为0，ly初始化为节点对应权值最大边的权值
        for y in range(self.rows):
            self.ly[y] = max(self.graph[y, :])

        for y in range(self.rows):  # 从每一竖向结点开始，寻找增广路
            while True:
                self.inc = np.inf
                self.vx = np.zeros(self.cols, dtype=np.int32)  # 横向结点的匹配标志
                self.vy = np.zeros(self.rows, dtype=np.int32)  # 竖向结点的匹配标志
                if self.dfs(y):
                    break
                else:
                    self.update()
                # print(y, self.lx, self.ly, self.vx, self.vy)
        return self.match_index

    # 更新顶标
    def update(self):
        for x in range(self.cols):
            if self.vx[x]:
                self.lx[x] += self.inc
        for y in range(self.rows):
            if self.vy[y]:
                self.ly[y] -= self.inc

    def dfs(self, y):  # 递归版深度优先搜索
        self.vy[y] = 1
        for x in range(self.cols):
            if self.vx[x] == 0:
                t = self.lx[x] + self.ly[y] - self.graph[y][x]
                if t == 0:
                    self.vx[x] = 1
                    # 两种情况：一是结点x没有匹配，那么找到一条增广路；二是X结点已经匹配，采用DFS，沿着X继续往下走，最后若以未匹配点结束，则也是一条增广路
                    if self.match_index[x] == -1 or self.dfs(self.match_index[x]):
                        self.match_index[x] = y  # 未匹配边变成匹配边
                        # print(y, x, self.match_index)
                        return True
                else:
                    if self.inc > t:
                        self.inc = t
        return False
if __name__ == '__main__':
    graph = np.array([[2, 1, 1], [3, 2, 1], [1, 1, 1]])
    # # graph = np.array([[3,4,6,4,9],[6,4,5,3,8],[7,5,3,4,2],[6,3,2,2,5],[8,4,5,4,7]])
    km = KMMatch(graph)
    print(km.match())
