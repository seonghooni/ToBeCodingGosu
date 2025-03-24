import sys
input = sys.stdin.readline

H, W = map(int, input().split())
heights = list(map(int, input().split()))
total = 0

for i in range(1, W-1):
    left_max =  max(heights[:i])
    right_max = max(heights[i+1:])

    min_height = min(left_max, right_max)

    if heights[i] < min_height:
        total += min_height - heights[i]

print(total)