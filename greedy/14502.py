from collections import deque
from copy import deepcopy
from itertools import combinations

N, M = map(int, input().split())
lab = []

# 지도 입력
for _ in range(N):
    lab.append(list(map(int, input().split())))

virus_point = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 2]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(map_case):
    queue = deque()
    queue.extend(virus_point)

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and map_case[nx][ny] == 0:
                queue.append((nx, ny))
                map_case[nx][ny] = 2

    count = 0
    for i in range(N):
        for j in range(M):
            if map_case[i][j] == 0:
                count += 1

    return count

# 가용 지역
available = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]

max_count = 0
for wall_case in combinations(available, 3):
    map_case = deepcopy(lab)

    for wall in wall_case:
        map_case[wall[0]][wall[1]] = 1

    max_count = max(max_count, bfs(map_case))

print(max_count)