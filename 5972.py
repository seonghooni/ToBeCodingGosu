import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 경로 설정
roots = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    src, dst, val = map(int, input().split())
    roots[src].append((dst, val))
    roots[dst].append((src, val))

distance = [float('inf')] * (N+1)

def dijkstra(start):
    global distance
    distance[start] = 0
    hq = [] # 힙큐

    heapq.heappush(hq, (0, start)) # (거리, 위치)

    while hq:
        cur_distance, cur_node = heapq.heappop(hq)

        if distance[cur_node] < cur_distance:
          continue

        for dst_node, dst_distance in roots[cur_node]:
            if cur_distance + dst_distance < distance[dst_node]:
                distance[dst_node] = cur_distance + dst_distance
                heapq.heappush(hq, (cur_distance + dst_distance, dst_node))

dijkstra(1)

print(distance[N])