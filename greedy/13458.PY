import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())


result = 0
for i in range(N):
    n = A[i] - B
    if n < 0:
        result += 1
    else:
        result += math.ceil(n/C) + 1

print(result)
