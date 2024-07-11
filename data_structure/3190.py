# 1. 뱀의 몸체를 이동하는 것을 deque() 으로 표현할 줄 알아야 한다.
# 2. 방향 변경시 index = ( index + 1 ) % 4 같은 방법을 잘 알아둬야 한다.

from collections import deque

N = int(input())
K = int(input())

board = [ [ 0 for _ in range(N+1) ] for _ in range(N+1) ]

# 사과 체크
for _ in range(K):
    i, j = map(int, input().split())
    board[i][j] = 1

M = int(input())
info = deque()
body = deque()
for _ in range(M):
    time, direction = input().split()
    info.append((int(time), direction))

second = 0
x = 1; y = 1
body.append([1, 1])
board[1][1] = 2 # 2는 자신의 몸
# D일 경우 index 증가
index = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    second += 1

    x = x + dx[index]
    y = y + dy[index]

    if x<1 or x>N or y<1 or y>N:
        break
    elif board[y][x] == 2:
        break

    if board[y][x] == 1:
        board[y][x] = 2
        body.append([y, x])
    else:
        board[y][x] = 2
        body.append([y, x])
        ty, tx = body.popleft()
        board[ty][tx] = 0

    if info:
        time, direction = info.popleft()
        if second == time:
            if direction == "D":
                index = ( index + 1 ) % 4
            else:
                index = ( index - 1 ) % 4
        else:
            info.appendleft((time, direction))

print(second)