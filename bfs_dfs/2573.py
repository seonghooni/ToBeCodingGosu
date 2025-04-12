from collections import deque
N, M = map(int, input().split())

seas = [[]] # 1-index

is_first = False
remainder_2 = deque()

for i in range(1, N+1):
    row = [0] + list(map(int, input().split()))
    for j in range(1, M+1):
        if not is_first and row[j] > 0:
            remainder_2.append((i, j))
            is_first = True

    seas.append(row)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()
result = 0


# -------------------------------- 빙하를 녹이는 과정
while remainder_2:
    visited = [[False] * (M+1) for _ in range(N+1)]

    x, y = remainder_2.pop()
    queue.append((x,y))
    visited[x][y] = True
    result += 1

    remainder = deque() # 녹아도 빙하인 위치 저장

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            if 0 < ax <= N and 0 < ay <= M:
                # 주변에 바다가 얼마나 접했는지 확인
                if seas[ax][ay] == 0 and not visited[ax][ay]: # 방문하지 않았다는건 이번턴에 0이 된게 아닌, 원래 바다라는 뜻
                    if seas[x][y] > 0: # 빙하가 녹는다.
                        seas[x][y] -= 1
                elif seas[ax][ay] > 0 and not visited[ax][ay]: # 주변에 빙산이 접했다면,
                    queue.append((ax,ay)) # 빙산인 위치만 큐에 추가함
                    visited[ax][ay] = True

        if seas[x][y] != 0:  # 녹았을때도 빙하인지 확인
            remainder.append((x, y))

    # -------------------------------- 녹은 빙하가 몇개인지 확인하는 과정

    visited = [[False] * (M+1) for _ in range(N+1)]

    if not remainder:
        print(0)
        exit()
    x, y = remainder.popleft()

    queue.append((x,y))
    visited[x][y] = True

    # print(f'remainder = {remainder}')

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            if 0 < ax <= N and 0 < ay <= M:
                if seas[ax][ay] > 0 and not visited[ax][ay]:
                    queue.append((ax, ay))
                    visited[ax][ay] = True

    is_first = False

    while remainder:
        x, y = remainder.popleft()

        if visited[x][y]:
            if not is_first:
                remainder_2.append((x,y))
                is_first = True
            continue
        else:
            print(result)
            exit()

print(0)
