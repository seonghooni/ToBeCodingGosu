import sys
input = sys.stdin.readline

arr = [[0] * 4 for _ in range(10001)]

# arr[n][i] : i까지 합하여 n이어야 하며, i보다 작은 값들로 구성되어야 함
# ex) arr[3][3] : 3을 포함하여 합이 3이면서, 앞에 있는 수들은 3보다 작아야 하는 경우의 수
arr[1][1] = arr[2][1] = arr[2][2] = 1
arr[3][1] = arr[3][2] = arr[3][3] = 1

for i in range(4, 10001):
    arr[i][1] = arr[i-1][1]
    arr[i][2] = arr[i-2][1] + arr[i-2][2]
    arr[i][3] = arr[i-3][1] + arr[i-3][2] + arr[i-3][3]

test_case = int(input())
for _ in range(test_case):
    N = int(input())
    print(arr[N][1] + arr[N][2] + arr[N][3])