import sys
input = sys.stdin.readline

N = int(input())

rows = [0]

for _ in range(N):
    rows.append(int(input()))

dp = [1] * (N+1)

for i in range(1, N+1):
    for j in range(1, i):
        if rows[i] > rows[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))