import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

sum_val = arr[0]
start = 0
end = 0
min_length = 100001
while start <= end:
    if sum_val < S:
        if end == N-1:
            break
        end += 1
        sum_val += arr[end]
    elif sum_val >= S:
        cur_length = end - start + 1
        min_length = min(min_length, cur_length)
        if min_length == 1:
            break

        sum_val -= arr[start]
        start += 1

    # print(sum_val)

if min_length != 100001:
    print(min_length)
else:
    print(0)