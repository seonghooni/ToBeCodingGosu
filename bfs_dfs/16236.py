from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
space = []
result = 0

for i in range(N):
    input_arr = list(map(int, input().split()))
    space.append(input_arr)
    for j in range(N):
        if input_arr[j] == 9:
            shark_x = i
            shark_y = j

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(shark_x, shark_y):
    shark_queue = deque()
    visited = [[False] * N for _ in range(N)]
    distance = [[float('inf')] * N for _ in range(N)]
    feeds = [] # 먹을 수 있는 생선들의 위치 저장

    shark_queue.append((shark_x, shark_y))
    visited[shark_x][shark_y] = True
    distance[shark_x][shark_y] = 0
    space[shark_x][shark_y] = 9

    while shark_queue:
        current_x, current_y = shark_queue.popleft()
        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if space[nx][ny] <= shark_size:
                    shark_queue.append((nx, ny))
                    visited[nx][ny] = True
                    distance[nx][ny] = distance[current_x][current_y] + 1
                    if 0 < space[nx][ny] < shark_size:
                        feeds.append((nx, ny, distance[nx][ny]))

    return sorted(feeds, key=lambda x: (x[2], x[0], x[1]))


shark_size=2
feeds_count=0

while True:

    feeds = bfs(shark_x, shark_y)

    if not feeds:
        print(result)
        break

    nx, ny, dist = feeds[0]

    space[shark_x][shark_y] = 0
    space[nx][ny] = 0
    shark_x = nx; shark_y = ny

    result += dist
    feeds_count +=1

    if feeds_count == shark_size:
        feeds_count = 0
        shark_size += 1