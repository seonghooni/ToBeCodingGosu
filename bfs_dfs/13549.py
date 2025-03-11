import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

dist = [float('inf')] * 100001
dist[N] = 0

queue_ = deque()
queue_.append(N)

while queue_:
    pos = queue_.popleft()

    if pos*2 < 100001 and dist[pos] < dist[pos*2]:
        dist[pos*2] = dist[pos]
        queue_.appendleft(pos*2)

    if pos+1 < 100001 and dist[pos]+1 < dist[pos+1]:
        dist[pos+1] = dist[pos]+1
        queue_.append(pos+1)

    if pos-1 > -1 and dist[pos]+1 < dist[pos-1]:
        dist[pos-1] = dist[pos]+1
        queue_.append(pos-1)

print(dist[K])
