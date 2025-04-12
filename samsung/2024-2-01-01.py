from collections import deque
N, M, F = map(int, input().split())
places = [[0] * (N+1)]

for _ in range(N):
    places.append([0] + list(map(int, input().split())))

# 단면의 배열을 저장할 장소 (2차원 배열을 저장하므로) rec은 3차원 배열
# 동/서/남/북/윗면, -1이 등장한다면 -1은 평면을 말함
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
recs = deque()

for i in range(5):
    rec = []
    for _ in range(M):
        rec.append(list(map(int, input().split())))

    recs.append(rec)

cur_d = 4 # 타임머신의 위치는 초기에 윗면(4)일 것임
rec_x, rec_y = 0, 0 # 시간의벽의 좌상단 좌표
cur_x, cur_y = 0, 0 # 현재 위치
min_cost = float('inf')

# 위에서 바라봤을때, 시간의 벽의 최초 x,y좌표를 구하는 함수
def find_point_rec():
    global rec_x, rec_y
    for i in range(1, N+1):
        for j in range(1, N+1):
            if places[i][j] == 3:
                rec_x = i
                rec_y = j
                return

# 윗면에서 현재 위치를 찾는 함수
def find_curent():
    global cur_x, cur_y
    for i in range(1,M+1):
        for j in range(1,M+1):
            if recs[4][i][j] == 2:
                cur_x = i
                cur_y = j
                return

# 단면을 회전시키는 함수 (dimension과 각도 90, 180, 270을 받음)
def rotate(dimension, degree):
    before_rec = recs[dimension]
    new_rec = [row[:] for row in before_rec]
    n = len(before_rec)
    # 90도 일때
    if degree == 90:
        for i in range(n):
            for j in range(n):
                new_rec[j][n-1-i] = before_rec[i][j]
    elif degree == 180:
        for i in range(n):
            for j in range(n):
                new_rec[n-1-i][n-1-j] = before_rec[i][j]
    elif degree == 270:
        for i in range(n):
            for j in range(n):
                new_rec[n-1-j][i] = before_rec[i][j]

    recs[dimension] = new_rec

# 시간의 벽 단면도 위에서 범위를 초과할 경우 이 함수를 실행함
# 어느 차원으로 이동하는지 (dimension, nx, ny)를 return 해줌
# dimension은 동/서/남/북/윗면 순으로 0/1/2/3/4 임
def other_dimension_nx_ny(cur_dimension, nx, ny):
    # 현재 동쪽면일 경우
    if cur_dimension == 0:
        # ny가 1보다 작으면 윗면으로 가야함
        if ny < 1:
            return (4, nx, M)
        # ny가 M보다 크면 미지의 공간(평면)으로 가야함
        elif ny > M:
            return (-1, rec_x-1+nx, rec_y+M)
        # nx가 1보다 작으면 북쪽면으로 가야함
        elif nx < 1:
            return (3, M-ny+1 ,M)
        # nx가 M보다 크면 남쪽면으로 가야함
        elif nx > M:
            return (2, ny, M)
    # 현재 서쪽면일 경우
    elif cur_dimension == 1:
        # ny가 1보다 작으면 평면으로 가야함
        if ny < 1:
            return (-1, rec_x-1+nx, rec_y-1)
        # ny가 M보다 크면 윗면으로 가야함
        elif ny > M:
            return (4, nx, 1)
        # nx가 1보다 작으면 북쪽면으로 가야함
        elif nx < 1:
            return (3, ny, 1)
        # nx가 M보다 크면 남쪽면으로 가야함
        elif nx > M:
            return (2, M-ny+1, 1)
    # 현재 남쪽면일 경우
    elif cur_dimension == 2:
        # ny가 1보다 작으면 서쪽면으로 가야함
        if ny < 1:
            return (1, M, M-nx+1)
        # ny가 M보다 크면 동쪽면으로 가야함
        elif ny > M:
            return (0, M, nx)
        # nx가 1보다 작으면 윗면으로 가야함
        elif nx < 1:
            return (4, M, ny)
        # nx가 M보다 크면 평면으로 가야함
        elif nx > M:
            return (-1, nx+M-1, rec_y-1+ny)
    # 현재 북쪽면일 경우
    elif cur_dimension == 3:
        # ny가 1보다 작으면 서쪽면으로 가야함
        if ny < 1:
            return (1, 1, nx)
        # ny가 M보다 크면 동쪽면으로 가야함
        elif ny > M:
            return (0, 1, M-nx+1)
        # nx가 1보다 작으면 평면으로 가야함
        elif nx < 1:
            return (-1, rec_x-1, rec_y-1+ny)
        # nx가 M보다 크면 윗면으로 가야함
        elif nx > M:
            return (4, 1, ny)
    # 현재 윗면일 경우
    elif cur_dimension == 4:
        # ny가 1보다 작으면 서쪽면
        if ny < 1:
            return (1, nx, M)
        # ny가 M보다 크면 동쪽면
        elif ny > M:
            return (0, nx, 1)
        # nx가 1보다 작으면 북쪽면
        elif nx < 1:
            return (3, M, ny)
        # nx가 M보다 크면 남쪽면
        elif nx > M:
            return (2, 1, ny)
    # 현재 평면일 경우
    elif cur_dimension == -1:
        # ny가 rec_y+M-1이면 동쪽면
        if ny == rec_y+M-1:
            return (0, nx-M+1,M)
        # 서쪽면으로 이동
        elif ny == rec_y:
            return (1, nx-M+1,1)
        # 남쪽면으로 이동
        elif nx == rec_x+M-1:
            return (2, M, ny-M+1)
        # 북쪽면으로 이동
        elif nx == rec_x:
            return (3, 1, ny-M+1)
# 위에서 본 전체를 출력
def print_places():
    for place in places:
        print(place)
    print("---")

# 단면을 출력
def print_one_rec(i):
    for row in recs[i]:
        print(row)
    print("---")

# 시간의 선이 끝에 위치할때도 처리해야할까? 해야할거같은데..
# ...
def bfs(x_1, y_1):
    global min_cost
    visited_2d = [[False] * (N+1) for _ in range(N+1)]
    visited_3d = [[[False] * (M+1) for _ in range(M+1)] for _ in range(5)]
    queue = deque()

    roots = [(x_1, y_1)]
    queue.append((cur_d, x_1, y_1, 0, roots))
    visited_3d[4][x_1][y_1] = True
    while queue:
        d, x, y, cost, roots = queue.popleft()
        if d == -1 and places[x][y] == 4:
            min_cost = min(min_cost, cost)
            print(roots)
        # 시간의 벽 위일때
        if d != -1:
            for i in range(4):
                nd = d
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위를 벗어난다면 다른 차원
                if nx < 1 or nx > M or ny < 1 or ny > M:
                    nd, nx, ny = other_dimension_nx_ny(d, nx, ny)
                # 다음 차원이 3차원일 경우
                if nd != -1 and not visited_3d[nd][nx][ny] and recs[nd][nx][ny] == 0:
                    visited_3d[nd][nx][ny] = True
                    queue.append((nd, nx, ny, cost+1, roots + [(nx, ny)]))
                # 다음 차원이 2차원일 경우
                elif nd == -1:
                    # 2차원에서 범위를 벗어나면 continue
                    if nx < 1 or nx > N or ny < 1 or ny > N:
                        continue
                    # 2차원에서 방문하지 않은 곳이라면 queue에 추가
                    if not visited_2d[nx][ny] and places[nx][ny] == 0:
                        visited_2d[nx][ny] = True
                        queue.append((nd, nx, ny, cost+1, roots + [(nx, ny)]))
        # 평면위 일때
        else:
            for i in range(4):
                nd = -1
                nx = x + dx[i]
                ny = y + dy[i]
                # 범위를 벗어난다면 continue
                if nx < 1 or nx > N or ny < 1 or ny > N:
                    continue
                # 3차원으로 이동해야할 경우
                if rec_x <= nx < rec_x+M and rec_y <= ny < rec_y+M:
                    nd, nx, ny = other_dimension_nx_ny(nd, nx, ny)
                    if not visited_3d[nd][nx][ny] and recs[nd][nx][ny] == 0:
                        visited_3d[nd][nx][ny] = True
                        queue.append((nd, nx, ny, cost+1, roots + [(nx, ny)]))
                else:
                    if not visited_2d[nx][ny] and places[nx][ny] != 1:
                        visited_2d[nx][ny] = True
                        queue.append((nd,nx,ny,cost+1, roots + [(nx, ny)]))

# -------------시간의 벽 단면도 입력------------
rotate(0, 270)
rotate(1, 90)
rotate(3, 180)

for i in range(5):
    recs[i] = [[0] * M] + recs[i]

    for j in range(M+1):
        recs[i][j] = [0] + recs[i][j]

# -------------시간의 벽 단면도 입력------------


find_point_rec() # 시간의벽의 좌상단 좌표를 받음
find_curent()
bfs(cur_x, cur_y)
print_places()

for i in range(5):
    print_one_rec(i)

print(min_cost)