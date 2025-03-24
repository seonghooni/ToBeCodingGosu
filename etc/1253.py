import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)

count = 0
for i in range(N):
    start = 0
    end = N-1

    if i==0: start = 1
    if i==N-1: end = N-2

    while start < end:
        sum_num = arr[start] + arr[end]
        if sum_num > arr[i]:
            end -= 1
            if end == i:
                end -= 1
        elif sum_num < arr[i]:
            start += 1
            if start == i:
                start += 1
        else:
            count +=1
            break

print(count)