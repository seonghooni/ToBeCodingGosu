import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

abs_max = max(-r1, -c1, r2, c2)

arr = [[0] * (c2-c1 + 1) for _ in range(r2-r1 +1)]

dx = [0, -1, 0, 1] # row
dy = [1, 0, -1, 0] # col

x = 0; y = 0
direction = 0
num = 1
level = 1
total_block = len(arr) * len(arr[0])

while total_block > 0:
    for _ in range(2): # 2번 반복
        for _ in range(level): # 해당 칸에 번호 입력
            if r1 <= x <= r2 and c1 <= y <= c2:
                arr[x - r1][y - c1] = num
                total_block -= 1
                max_num = num
            num += 1
            x = x + dx[direction]
            y = y + dy[direction]
        direction = (direction + 1) % 4
    level += 1

str_max_length = len(str(max_num))

for row in arr:
    for num in row:
        print(str(num).rjust(str_max_length), end=" ")
    print()


