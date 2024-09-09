# 다음과 같이 경우의 수가 나뉜다.
# 1) 꿀이 한쪽 끝에 있는 경우, 벌 한 마리는 무조건 반대쪽 끝, 나머지 한 마리는 하나씩 탐색해서 비교해야 함
# 2) 벌이 양쪽 끝에 있는 경우, 꿀의 위치를 하나씩 탐색해서 비교해야 함
# 비교할 때 부분합을 사용해서 쉽게 처리할 수 있음 ★★★★★

N = int(input())
arr = list(map(int, input().split()))

result = 0

partial_sum = [0] * N
partial_sum[0] = arr[0]
for i in range(1, N):
    partial_sum[i] = partial_sum[i-1] + arr[i]

# 벌 벌 ... 꿀
for i in range(1, N-1):
    result = max(result, partial_sum[N-1] - arr[0] - arr[i] + partial_sum[N-1] - partial_sum[i])

# 벌 ... 꿀 ... 벌
for i in range(1, N-1):
    result = max(result, partial_sum[i] - arr[0] + partial_sum[N-2] - partial_sum[i-1])

# 꿀 ... 벌 벌
for i in range(1, N-1):
    result = max(result, partial_sum[N-2] + partial_sum[i-1] - arr[i])

print(result)