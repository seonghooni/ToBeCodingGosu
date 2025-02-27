import sys
input = sys.stdin.readline

N, M = map(int, input().split())
titles = []
idx = -1
for _ in range(N):
    title, score = input().split()
    score = int(score)
    titles.append((title, score))
    idx += 1

for _ in range(M):
    individual_score = int(input())

    start = 0
    end = idx

    while start <= end:
        mid = (start + end) // 2
        if individual_score <= titles[mid][1]:
            end = mid - 1
        else:
            start = mid + 1

    print(titles[start][0])