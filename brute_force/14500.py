N, M = map(int, input().split())

paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

partial_sum = 0
max_sum = 0

# 1번 도형
for i in range(N): # ㅡ
    for j in range(M-3):
        partial_sum = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3]
        max_sum = max(partial_sum, max_sum)
for i in range(N-3): # ㅣ
    for j in range(M):
        partial_sum = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j]
        max_sum = max(partial_sum, max_sum)

# 2번 도형
for i in range(N-1):
    for j in range(M-1):
        partial_sum = paper[i][j] + paper[i][j+1] + paper[i+1][j] + paper[i+1][j+1]
        max_sum = max(partial_sum, max_sum)

# 3번 도형
for i in range(N-2):
    for j in range(M-1):
        partial_sum_1 = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1]
        partial_sum_2 = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1]
        partial_sum_3 = paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1] + paper[i+2][j]
        partial_sum_4 = paper[i][j] + paper[i][j + 1] + paper[i + 1][j] + paper[i + 2][j]
        max_sum = max(partial_sum_1, partial_sum_2, partial_sum_3, partial_sum_4, max_sum)
for i in range(N-1):
    for j in range(M-2):
        partial_sum_1 = paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i][j+2]
        partial_sum_2 = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]
        partial_sum_3 = paper[i][j] + paper[i][j + 1] + paper[i][j + 2] + paper[i + 1][j+2]
        partial_sum_4 = paper[i][j+2] + paper[i+1][j] + paper[i + 1][j+1] + paper[i + 1][j+2]
        max_sum = max(partial_sum_1, partial_sum_2, partial_sum_3, partial_sum_4, max_sum)

# 4번 도형
for i in range(N-2):
    for j in range(M-1):
        partial_sum_1 = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1]
        partial_sum_2 = paper[i][j+1] + paper[i + 1][j] + paper[i + 1][j+1] + paper[i + 2][j]
        max_sum = max(partial_sum_1, partial_sum_2, max_sum)
for i in range(N-1):
    for j in range(M-2):
        partial_sum_1 = paper[i][j+1] + paper[i][j+2] + paper[i+1][j] + paper[i+1][j+1]
        partial_sum_2 = paper[i][j] + paper[i][j+1] + paper[i + 1][j + 1] + paper[i+1][j+2]
        max_sum = max(partial_sum_1, partial_sum_2, max_sum)

# 5번 도형
for i in range(N-1):
    for j in range(M-2):
        partial_sum_1 = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+1]
        partial_sum_2 = paper[i][j+1] + paper[i+1][j] + paper[i+1][j + 1] + paper[i+1][j+2]
        max_sum = max(partial_sum_1, partial_sum_2, max_sum)
for i in range(N-2):
    for j in range(M-1):
        partial_sum_1 = paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+2][j+1]
        partial_sum_2 = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+1][j+1]
        max_sum = max(partial_sum_1, partial_sum_2, max_sum)

print(max_sum)