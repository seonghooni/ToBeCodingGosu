from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

roads = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 길 정보 입력
for i in range(N):
    road = list(map(int, input().split()))

    for j in range(i+1, N):
        if road[j] == 1:
            roads[i+1].append(j+1)
            roads[j+1].append(i+1)

direction = list(map(int, input().split()))

my_queue = deque()

my_queue.append(direction[0])
visited[direction[0]] = True

while my_queue:
    node = my_queue.popleft()

    for connected_node in roads[node]:
        if not visited[connected_node]:
            visited[connected_node] = True
            my_queue.append(connected_node)

for node in direction:
    if not visited[node]:
        print("NO")
        exit()

print("YES")