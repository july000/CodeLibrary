from scipy.optimize import linear_sum_assignment
import numpy as np
from disjoint_set import DisjointSet
ds = DisjointSet()
ds.union(1,2)
print(ds.__contains__(0))
cost = [
[22,  14, 120, 21],
[19,  12, 172, 21],
[161, 122, 2, 50],
[19,  22, 90, 11],
[4, 51, 28, 43 ],
[128, 39, 28, 4 ]]
# cost = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])
row_ind, col_ind = linear_sum_assignment(cost, maximize=True)
print(row_ind, col_ind)
print(cost[row_ind, col_ind].sum())

# from hungarian_algorithm import algorithm
# # pip3 install hungarian-algorithm

# G = {
# 	'A': { '#191': 22, '#122': 14, '#173': 120, '#121': 21, '#128': 4, '#104': 51 },
# 	'B': { '#191': 19, '#122': 12, '#173': 172, '#121': 21, '#128': 28, '#104': 43 },
# 	'C': { '#191': 161, '#122': 122, '#173': 2, '#121': 50, '#128': 128, '#104': 39 },
# 	'D': { '#191': 19, '#122': 22, '#173': 90, '#121': 11, '#128': 28, '#104': 4 }
# }
# results = algorithm.find_matching(G, matching_type = 'min', return_type = 'list')
# print(results)