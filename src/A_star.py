from re import S
import numpy as np
import sys
'''
A* 算法的思路
f(n) = g(n) + h(n)
g(n):表示起点到当前节点的距离
h(n):表示当前节点到终点的预测距离
目标:f(n)越小越好

贪心算法：只考虑一步的代价，选择最小的进行前进，短视
Dij算法：考虑到终点的代价，选择最小代价进行前进， 计算量太大
A*算法：对Dij算法进行优化，先判断一下某个节点是否值得进行进一步的搜索， 就是h(n)的设计，选择预估代价最小的那个进行搜索，而不是计算完所有之后再选择

算法设计
map：地图
方向：上下左右移动
障碍物：
open_set:待搜索
close_set:已搜索

初始化close_set和open_set
将起点加入到open_set, 并设置优先级为0(最高)
如果open_set不为空，则从中取优先级最高的节点n
    如果节点n是终点，则：
        从终点开始逐步追踪parent节点，一直到达起点
        返回找到路径，结束
    如果节点n不是终点，则
        将节点n从open_set中移除，加入到close_set中
        遍历节点n的所有的临近节点
            如果临近节点m在close_set中，则
                跳过，选取下一个临近节点
            如果临近节点m也不在open_set中，则
                设置节点m的parent为节点n
                计算节点m的优先级
                将节点m加入open_set中
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cost = sys.maxsize
        self.parent = None
    
class RandomMap:
    def __init__(self, size = 50):
        self.size = size
        self.obstacle = size // 8
        self.GenerateObstacle()
    
    def generateObstacle(self):
        self.obstacle_point = []
        self.obstacle_point.append(Point(self.size//2, self.size//2))
        self.obstacle_point.append(Point(self.size//2, self.size//2-1))

        # Generate an obstacle in the middle
        for i in range(self.size//2-4, self.size//2):
            self.obstacle_point.append(Point(i, self.size-i))
            self.obstacle_point.append(Point(i, self.size-i-1))
            self.obstacle_point.append(Point(self.size-i, i))
            self.obstacle_point.append(Point(self.size-i, i-1))

        for i in range(self.obstacle-1):
            x = np.random.randint(0, self.size)
            y = np.random.randint(0, self.size)
            self.obstacle_point.append(Point(x, y))

            if (np.random.rand() > 0.5): # Random boolean ⑥
                for l in range(self.size//4):
                    self.obstacle_point.append(Point(x, y+l))
                    pass
            else:
                for l in range(self.size//4):
                    self.obstacle_point.append(Point(x+l, y))
                    pass
    
    def isObstacle(self, x, y):
        for p in self.obstacle_point:
            if x == p.x and y ==p.y:
                return True
        return False
    
class AStar:
    def __int__(self, map):
        self.map = map
        self.open_set = []
        self.close_set = []

    def isStartPoint(self, p):
        return p.x == 0 and p.y == 0
    
    def isEndPoint(self, p):
        return p.x == self.map.size - 1 and p.y == self,map.size - 1

    def HeuristicCost(self, p):
        dis_x = self.map.size - 1 - p.x
        dis_y = self.map.size - 1 - p.y
        return dis_x + dis_y
    
    def baseCost(self, p):
        return p.x + p.y
    
    def totalCost(self, p):
        return self.HeuristicCost(p) + self.baseCost(p)
    
    def IsInPointList(self, p, point_list):
        for point in point_list:
            if point.x == p.x and point.y == p.y:
                return True
        return False
    
    def isInOpenList(self, p):
        return self.isInPointList(p, self.open_set)

    def isInCloseList(self, p):
        return self.isInPointList(p, self.close_set)

    def isVaildPoint(self, x, y):
        if x < 0 or y < 0:
            return False
        elif x >= self.map.size or y >= self.map.size:
            return False
        else:
            return not self.map.isObstacle(x, y)

    def run(self):
        start_point = Point(0, 0)
        start_point.cost = 0
        self.open_set.append(start_point)
        while True:
            index = self.selectPointInOpenList()
            point = self.open_set[index]

            if self.isEndPoint(point):
                return 
            self.open_set.remove(point)
            self.close_set.append(point)

            x = point.x
            y = point.y
            self.processPoint(x-1, y-1, point)
            self.processPoint(x-1, y, point)
            self.processPoint(x-1, y+1, point)
            self.processPoint(x, y-1, point)
            self.processPoint(x, y+1, point)
            self.processPoint(x+1, y-1, point)
            self.processPoint(x+1, y, point)
            self.processPoint(x+1, y+1, point)
    
    def processPoint(self, x, y, parent):
        if not self.isVaildPoint(x, y):
            return
        point = Point(x, y)
        if self.isInCloseList(point):
            return
        if not self.isInOpenList(point):
            point.parent = parent
            point.cost = self.totalCost(point)
            self.open_set.add(point)

    def selectPointInOpenList(self):
        






    
        

