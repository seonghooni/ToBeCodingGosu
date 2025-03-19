from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

root = [0] * 101
for i in range(101):
    root[i] = i

distance = [float('inf')] * 101
distance[1] = 0

for _ in range(N+M):
    src, dst = map(int, input().split())
    root[src] = dst

my_deque = deque()
my_deque.appendleft(1)

while my_deque:
    start = my_deque.popleft()
    min_distance = distance[start] # 출발하는 장소까지 가는 최단시간
    for i in range(1, 7):
        if start+i < 101:
            end = root[start+i] # 현재 위치로부터 +1 ~ +6 까지 이동 가능
            if min_distance+1 < distance[end]: # 현재 위치에서 1~6 띄워서 가는 거리가 "기존보다" 더 빠르다면
                distance[end] = min_distance+1 # 기존값을 바꿈
                my_deque.append(end)

print(distance[100])
