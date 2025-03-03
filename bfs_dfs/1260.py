# dfs는 stack(list) 또는 재귀함수, bfs는 queue를 사용

# **주의**
# 1) 노드를 정렬하면서 데이터를 넣고 싶을때는 bisect를 사용하는 것이 좋음.
# 2) bisect가 아니라면 nodes[start][end] = 1 방식으로 간선을 기록함으로써 숫자가 작은 노드부터 탐색 가능
# heapq는 정렬된 요소로 꺼내기 위해선 heappop을 반드시 해야하므로 원본 데이터가 변경될 수 있음
#

import bisect
from collections import deque

N, M, V = map(int, input().split())

nodes = [ [] for _ in range(N+1) ]
is_visited = [ False for _ in range(N+1) ]
is_visited_2 = [ False for _ in range(N+1) ]

for _ in range(M):
    start, end = map(int, input().split())
    bisect.insort(nodes[start], end)
    bisect.insort(nodes[end], start)

def bfs(node):
    bfs_queue = deque()
    bfs_queue.append(node)
    is_visited[node] = True

    while bfs_queue:
        start_node = bfs_queue.popleft()
        print(start_node, end=" ")
        for end_node in nodes[start_node]:
            if not is_visited[end_node]: # 방문하지 않은 노드라면
                is_visited[end_node] = True
                bfs_queue.append(end_node)

def dfs(node):
    # if not is_visited[node]:
    #     print(node, end=" ")
    #     is_visited[node] = True
    #     for i in nodes[node]:
    #         dfs(i)

    print(node, end=" ")
    is_visited_2[node] = True
    for i in nodes[node]:
        if not is_visited_2[i]:
            dfs(i)

dfs(V)
print()
bfs(V)
