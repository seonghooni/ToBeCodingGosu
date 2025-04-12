from collections import deque

R, C, K = map(int, input().split())

forest = [ [0] * (C+1) for _ in range(R+4) ]

center = [(0, 0)] # 중심의 위치, ex) 1번 정령의 센터는 center[1] = (7,4)
exit_dir = [float('inf')] # 출구의 방향, ex) 1번 정령의 출구는 exit_dir[1] = 0

for i in range(K):
    c, d = map(int, input().split())
    center.append((2, c))
    exit_dir.append(d)

dx = [-1, 0, 1, 0] # 북/동/남/서
dy = [0, 1, 0, -1]


def print_2d(arr_2d):
    for arr in arr_2d:
        print(arr)
    print("-----")

# 범위를 확인하는 함수
def in_range(x, y):
    return 1 <= x <= R+3 and 1 <= y <= C

# 골렘이 숲 안에 완전히 들어왔는지 확인
def is_totally_in_forest(num):
    x, y = center[num]
    return x >= 5

# 첫번째 방법으로 이동하는게 가능한지 확인하는 함수
def check_one(center_x, center_y):
    for dx, dy in [(2,0), (1,1), (1,-1)]: # 센터 기준으로 떨어진 거리로 계산
        nx = center_x + dx
        ny = center_y + dy

        # 범위를 벗어나는 경우 False를 리턴한다.
        if not in_range(nx, ny):
            return False

        # 한 군데라도 이미 골렘이 있을 경우 False를 리턴한다.
        if forest[nx][ny] != 0:
            return False

    return True # 그 외의 경우에는 True를 리턴

# 두번째 방법으로 이동하는게 가능한지 확인하는 함수
def check_two(center_x, center_y):
    for dx, dy in [(-1,-1),(0,-2),(1,-2),(1,-1),(2,-1)]:
        nx = center_x + dx
        ny = center_y + dy

        # 범위를 벗어나는 경우 False를 리턴한다.
        if not in_range(nx, ny):
            return False

        # 한 군데라도 이미 골렘이 있을 경우 False를 리턴한다.
        if forest[nx][ny] != 0:
            return False
    return True

# 세번째 방법으로 이동하는게 가능한지 확인하는 함수
def check_three(center_x, center_y):
    for dx, dy in [(-1,1),(0,2),(1,2),(1,1),(2,1)]:
        nx = center_x + dx
        ny = center_y + dy

        # 범위를 벗어나는 경우 False를 리턴한다.
        if not in_range(nx, ny):
            return False

        # 한 군데라도 이미 골렘이 있을 경우 False를 리턴한다.
        if forest[nx][ny] != 0:
            return False
    return True

# 정령의 center를 중심으로, 상/하/좌/우/가운데를 forest에 업데이트 한다.
def update(num):
    x, y = center[num]
    for dx, dy in [(0,0), (1,0), (-1,0), (0,-1), (0,1)]:
        nx = x + dx
        ny = y + dy

        forest[nx][ny] = num

# 각 방법으로 이동 가능하다면 이동하는 함수, update까지 진행함
# input = 정령 번호
def move(num):
    global forest
    while True:
        x, y = center[num]

        if check_one(x, y):
            center[num] = (x+1, y) # 한 칸 아래로 이동
        elif check_two(x, y):
            center[num] = (x+1, y-1) # 반시계방향으로 회전하면서 왼쪽 아래로 이동
            exit_dir[num] = (exit_dir[num]-1)%4
        elif check_three(x, y):
            center[num] = (x+1, y+1) # 시계방향으로 회전하면서 오른쪽 아래로 이동
            exit_dir[num] = (exit_dir[num]+1)%4
        else:
            break # 아무것도 해당되지 않는다면 더이상 이동하지 못하므로 종료

    if is_totally_in_forest(num):
        update(num)
        # TODO:: bfs()
        return bfs(num)
    else:
        forest = [[0] * (C + 1) for _ in range(R + 4)]
        return 0

# 번호에 해당하는 정령이 움직이면서 가장 낮은 row를 갱신함
def bfs(num):
    x, y = center[num]
    queue = deque()
    visited = [[False] * (C+1) for _ in range(R+4)] # TODO:: 이건 나중에 메모리문제 생기면 수정해볼지도?

    queue.append((x,y,num)) # x, y, 현재 서있는 골렘의 번호
    visited[x][y] = True

    max_row = 0
    while queue:
        x, y, n = queue.popleft()
        max_row = max(max_row, x)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_range(nx, ny):
                continue
            if forest[nx][ny] == 0:
                continue

            # 방문해보지 않았을 경우
            if not visited[nx][ny]:
                # 이동하려는 위치가 같은 골렘인지 확인 해야함
                if forest[nx][ny] == n:
                    visited[nx][ny] = True
                    queue.append((nx,ny,forest[nx][ny]))
                # 현재 골렘과 다른 골렘일 경우, 현재 위치가 출구인지 확인해야만 이동 가능
                else:
                    d = exit_dir[n] # 현재 서있는 골렘의 출구 방향
                    center_x, center_y = center[n]
                    exit_x, exit_y = center_x + dx[d], center_y + dy[d]
                    if (x, y) == (exit_x, exit_y):
                        visited[nx][ny] = True
                        queue.append((nx,ny,forest[nx][ny]))

    return max_row-3 # 우리가 맨 처음에 행3개를 추가해줬기 때문

ans = 0
for num in range(1, K+1):
    ans += move(num)
    # print_2d(forest) # 북동남서
    # print(bfs(i))

print(ans)