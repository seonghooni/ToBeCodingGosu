from collections import deque

N, M = map(int, input().split())
s_x, s_y, e_x, e_y = map(int, input().split()) # 메두사의 좌표를 s라고 해도 좋음.
s_x += 1
s_y += 1
e_x += 1
e_y += 1

places = [[0] * (N+1)]
warriors_info = []
warriors_board = [[0] * (N+1) for _ in range(N+1)] # 각 셀에 위치하는 전사의 수
sights = [[[False] * (N+1) for _ in range(N+1)] for _ in range(4)]# 메두사의 초기 시야
is_hide = [[[False] * (N+1) for _ in range(N+1)] for _ in range(4)] # 전사에 의해 가려진 시야
stone_list = []
catch_warriors_idx_list = [] # 메두사를 잡은 전사들의 idx
move_count = 0

iii = list(map(int, input().split()))
for i in range(len(iii)//2):
    warrior = iii[i*2:(i+1)*2]
    warriors_info.append((warrior[0]+1, warrior[1]+1))
    warriors_board[warrior[0]+1][warrior[1]+1] += 1

for i in range(N):
    places.append([0] + list(map(int, input().split())))


def in_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

distance = [[float('inf')] * (N+1) for _ in range(N+1)] # 거리를 기록할 것임

dx = [-1,1,0,0] # 상/하/좌/우
dy = [0,0,-1,1]

# 공원을 기준으로 메두사까지와의 거리가 어떻게 되는지 확인
def bfs():
    visited = [[False] * (N+1) for _ in range(N+1)]
    queue = deque()
    distance[e_x][e_y] = 0
    visited[e_x][e_y] = True
    queue.append((e_x, e_y))
    while queue:
        x, y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_range(nx,ny):
                continue
            # 방문 안한 길이라면 방문
            if places[nx][ny] == 0 and not visited[nx][ny]:
                distance[nx][ny] = distance[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx,ny))

def medusa_move():
    global s_x, s_y
    min_dist = float('inf')
    d_list = []
    for i in range(4): # 상->하->좌->우 순서로 확인할 것임
        nx = s_x + dx[i]
        ny = s_y + dy[i]
        if not in_range(nx,ny):
            continue
        if distance[nx][ny] < min_dist:
            d_list = [i]
            min_dist = distance[nx][ny]
        elif distance[nx][ny] == min_dist:
            d_list.append(i)

    s_x = s_x + dx[d_list[0]]
    s_y = s_y + dy[d_list[0]]

    l = len(warriors_info)
    for _ in range(l):
        if (s_x, s_y) in warriors_info:
            warriors_info.remove((s_x, s_y))
            warriors_board[s_x][s_y] = 0



# 최초 메두사 시야 확인
def medusa_sight(i):
    # 상/하/좌/우
    queue = deque()
    queue.append((s_x, s_y))
    if i == 0:
        d_list = [(-1, -1), (-1, 0), (-1, 1)]
    elif i == 1:
        d_list = [(1, -1), (1, 0), (1, 1)]
    elif i == 2:
        d_list = [(-1, -1), (0, -1), (1, -1)]
    elif i == 3:
        d_list = [(-1, 1), (0, 1), (1, 1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in d_list:
            nx = x + dx
            ny = y + dy
            if not in_range(nx, ny):
                continue

            # 아직 확인하지 않은 영역이라면 큐에 넣음
            if not sights[i][nx][ny]:
                sights[i][nx][ny] = True
                queue.append((nx,ny))

# row 순서대로 전사가 시야 안에 속하는지 확인한 후, 가려지는 영역 표시
# (석화된 전사 수, [전사 좌표]) return
def medusa_sight_update(i):
    cnt = 0
    stone_list = []
    # 위를 보고 있는 것을 기준으로 생각
    if i == 0:
        for x in range(s_x-1, 0, -1):
            for y in range(1, N+1):
                if sights[i][x][y] and not is_hide[i][x][y] and warriors_board[x][y] > 0: # 시야 내에 있고, 전사가 있을 경우
                    hide_sight_update(0, x, y)
                    cnt += warriors_board[x][y]
                    stone_list.append((x,y))
    # 아래를 보고 있는 것을 기준으로 생각
    elif i == 1:
        for x in range(s_x+1, N+1):
            for y in range(1, N+1):
                if sights[i][x][y] and not is_hide[i][x][y] and warriors_board[x][y] > 0: # 시야 내에 있고, 전사가 있을 경우
                    hide_sight_update(1, x, y)
                    cnt += warriors_board[x][y]
                    stone_list.append((x, y))
    # 왼쪽을 보고 있는 것을 기준으로 생각
    elif i == 2:
        for y in range(s_y-1, 0, -1):
            for x in range(1, N + 1):
                if sights[i][x][y] and not is_hide[i][x][y] and warriors_board[x][y] > 0: # 시야 내에 있고, 전사가 있을 경우
                    hide_sight_update(2, x, y)
                    cnt += warriors_board[x][y]
                    stone_list.append((x, y))
    elif i == 3:
        # 오른쪽을 기준으로 생각
        for y in range(s_y+1, N+1):
            for x in range(1, N+1):
                if sights[i][x][y] and not is_hide[i][x][y] and warriors_board[x][y] > 0: # 시야 내에 있고, 전사가 있을 경우
                    hide_sight_update(3, x, y)
                    cnt += warriors_board[x][y]
                    stone_list.append((x, y))

    return cnt, stone_list
# 메두사가 보는 방향(상/하/좌/우)과 전사의 x,y 좌표를 입력받음
def hide_sight_update(medusa_d, warrior_x, warrior_y):
    d_list = []
    if medusa_d == 0: # 메두사 시야가 위쪽이라면
        d_list.append((-1,0))
        if warrior_y < s_y: # 전사가 왼쪽에 있을 때
            d_list.append((-1,-1))
        elif warrior_y > s_y: # 전사가 오른쪽에 있을 때
            d_list.append((-1,1))
    elif medusa_d == 1: # 메두사 시야가 아래쪽
        d_list.append((1,0))
        if warrior_y < s_y: # 전사가 왼쪽에 있을 때
            d_list.append((1,-1))
        elif warrior_y > s_y: # 전사가 오른쪽에 있을 때
            d_list.append((1,1))
    elif medusa_d == 2: # 메두사 시야가 왼쪽
        d_list.append((0,-1))
        if warrior_x < s_x: # 전사가 위쪽에 있을 때
            d_list.append((-1,-1))
        elif warrior_x > s_x: # 전사가 아래쪽에 있을 때
            d_list.append((1,-1))
    elif medusa_d == 3: # 메두사 시야가 오른쪽
        d_list.append((0,1))
        if warrior_x < s_x: # 전사가 위쪽에 있을 때
            d_list.append((-1,1))
        elif warrior_x > s_x: # 전사가 아래쪽에 있을 때
            d_list.append((1,1))

    queue = deque()
    queue.append((warrior_x, warrior_y))
    while queue:
        x, y = queue.popleft()
        for dx, dy in d_list:
            nx = x + dx
            ny = y + dy
            if not in_range(nx, ny):
                continue

            # 아직 확인하지 않은 영역이라면 큐에 넣음
            if not is_hide[medusa_d][nx][ny]:
                is_hide[medusa_d][nx][ny] = True
                queue.append((nx, ny))

# 전사 첫번째 이동
def warrior_move_1(k, dd):
    global move_count
    catch_count = 0
    d_list = []
    x, y = warriors_info[k]

    # 석화 리스트에 있을 경우 움직이지 않음
    if (x,y) in stone_list:
        return catch_count

    temp_d_list = []
    if x < s_x: # 전사가 위에 있다면
        temp_d_list.append(1)
    elif x > s_x:
        temp_d_list.append(0)
    if y < s_y: # 전사가 왼쪽에 있다면
        temp_d_list.append(3)
    elif y > s_y:
        temp_d_list.append(2)

    for i in temp_d_list:
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue
        # 시야 내에 있는 경우 스킵
        if sights[dd][nx][ny] and not is_hide[dd][nx][ny]:
            continue

        # 그렇지 않을 경우 이동 가능
        d_list.append(i)

    if len(d_list) >= 1:
        d_list.sort()
        d = d_list[0]

        warriors_board[x][y] -= 1
        x = x + dx[d]
        y = y + dy[d]
        warriors_info[k] = (x, y)

        # 메두사를 잡는게 아닌 경우
        if (x,y) != (s_x, s_y):
            warriors_board[x][y] += 1
        else:
            catch_count += 1
        move_count += 1



    return catch_count

def warrior_move_2(k, dd):
    global move_count
    catch_count = 0
    d_list = []
    x, y = warriors_info[k]

    # 석화 리스트에 있을 경우 움직이지 않음
    if (x, y) in stone_list:
        return catch_count

    temp_d_list = []
    if x < s_x:  # 전사가 위에 있다면
        temp_d_list.append(1)
    elif x > s_x:
        temp_d_list.append(0)
    if y < s_y:  # 전사가 왼쪽에 있다면
        temp_d_list.append(3)
    elif y > s_y:
        temp_d_list.append(2)

    for i in temp_d_list:
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny):
            continue
        # 시야 내에 있는 경우 스킵
        if sights[dd][nx][ny] and not is_hide[dd][nx][ny]:
            continue

        # 그렇지 않을 경우 이동 가능
        d_list.append(i)

    if len(d_list) == 2:
        for d in d_list:
            if d // 2 < 1: # 상하인 경우
                d_list.remove(d)

    if len(d_list) == 1:
        d = d_list[0]

        warriors_board[x][y] -= 1
        x = x + dx[d]
        y = y + dy[d]
        warriors_info[k] = (x, y)

        # 메두사를 잡는게 아닌 경우
        if (x, y) != (s_x, s_y):
            warriors_board[x][y] += 1
        else:
            catch_count += 1
        move_count += 1

    return catch_count


bfs()
if distance[s_x][s_y] == float('inf'):
    print(-1)
    exit()

while (s_x, s_y) != (e_x, e_y):

    sights = [[[False] * (N + 1) for _ in range(N + 1)] for _ in range(4)]  # 메두사의 초기 시야
    is_hide = [[[False] * (N + 1) for _ in range(N + 1)] for _ in range(4)]  # 전사에 의해 가려진 시야
    medusa_move()
    if (s_x, s_y) == (e_x, e_y):
        print(0)
        exit()

    d = 0
    max_cnt = 0
    stone_list = []
    for i in range(4):
        medusa_sight(i)
        cnt, sl = medusa_sight_update(i)
        if cnt > max_cnt:
            max_cnt = cnt
            stone_list = sl
            d = i

    catch_count = 0
    move_count = 0

    for k in range(len(warriors_info)):
        if warriors_info[k] in stone_list:
            continue
        catch_count += warrior_move_1(k, d)
        if (warriors_info[k][0], warriors_info[k][1]) == (s_x, s_y):
            continue
        if warriors_info[k] in stone_list:
            continue
        catch_count += warrior_move_2(k, d)

    l = len(warriors_info)
    for _ in range(l):
        if (s_x, s_y) in warriors_info:
            warriors_info.remove((s_x, s_y))
    print(move_count, max_cnt, catch_count)
# while (s_x,s_y) != (e_x, e_y):
#     medusa_move()
#     print(s_x, s_y)
