from collections import deque
def can_reach_end(map, k):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    n = len(map)
    m = len(map[0])
    print(n,m)
    visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]

    queue = deque([(0, 0, k)])
    
    while queue:
        x, y, remaining_k = queue.popleft()
        
        if x == n - 1 and y == m - 1:
            return True
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < m:
                if map[new_x][new_y] == 1 and remaining_k > 0 and not visited[new_x][new_y][remaining_k - 1]:
                    visited[new_x][new_y][remaining_k - 1] = True
                    queue.append((new_x, new_y, remaining_k - 1))
                elif map[new_x][new_y] == 0 and not visited[new_x][new_y][remaining_k]:
                    visited[new_x][new_y][remaining_k] = True
                    queue.append((new_x, new_y, remaining_k))
    return False

map = [
    [0, 1, 0],
    [1, 1, 0],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]

# n = len(map)
# m = len(map[0])
# visited = [[[False] * (3 + 1) for _ in range(m)] for _ in range(n)]
# print(visited)
# print(m,n)
# k = 0

# print(can_reach_bottom_right(map, 0))  # Output: True
rr = can_reach_end(map, 1)
print(rr)