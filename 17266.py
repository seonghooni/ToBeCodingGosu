import math

N = int(input())
M = int(input())
points = list(map(int, input().split()))

# 양 끝점과의 거리 비교
max_distance = max(points[0], N-points[M-1])

for i in range(M-1):
    max_distance = max(max_distance, math.ceil((points[i+1] - points[i]) / 2))

print(max_distance)