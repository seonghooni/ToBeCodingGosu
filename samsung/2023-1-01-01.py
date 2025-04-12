from collections import deque
N, M, K = map(int, input().split())

boards = [[0] * (M+1)]
for _ in range(N):
    board = list(map(int, input().split()))
    boards.append([0] + board)

distance = [[float('inf')] * (M+1) for _ in range(N+1)] # bfs를 실행할때마다, 목적지까지의 거리를 저장하는 2차원 배열
related_battle = [[False] * (M+1) for _ in range(N+1)] # 공격과 관련있는지 확인하는 2차원 배열
recent_battle = [[0] * (M+1) for _ in range(N+1)] # 가장 최근에 공격한 turn을 확인하는 2차원 배열
dx = [0, 1, 0, -1] # 우/하/좌/상
dy = [1, 0, -1, 0]
attacker_x = 0; attacker_y = 0

# 범위를 벗어난 경우 적절한 인덱스를 반환함 (보통 -1을 벗어나지 않음)
def process_nx_ny(x, y):
    nx = x; ny = y # return 할 "제대로 된 위치"
    if x == 0:
        nx = N
    elif x == N+1:
        nx = 1

    if y == 0:
        ny = M
    elif y == M+1:
        ny = 1

    return nx, ny

def bfs(x, y):
    global distance
    distance = [[float('inf')] * (M + 1) for _ in range(N + 1)] # 거리 정보 초기화
    visited = [[False] * (M+1) for _ in range(N+1)]
    queue = deque()

    # 초기 세팅
    queue.append((x,y,0)) # x, y, distance
    distance[x][y] = 0
    visited[x][y] = True

    while queue:
        x, y, dist = queue.popleft()
        if dist > distance[x][y]: # 최단거리 이상이라면 더 볼것도 없이 PASS
            continue
        else:
            distance[x][y] = dist

        for i in range(4):
            nx, ny = process_nx_ny(x + dx[i], y + dy[i]) # 범위를 벗어났어도 적절한 nx, ny를 할당받음

            if not visited[nx][ny] and boards[nx][ny] != 0:
                visited[nx][ny] = True
                queue.append((nx, ny, dist+1))

# 타겟을 만날때까지 레이저 공격을 함
# TODO :: distance[x][y] == 'inf'인지 확인을 통해 레이저 공격 가능한지 식별

# 공격자 선정하는 함수, 좌표(x,y)를 return함
def select_attacker():
    # 가장 약한놈들만 선정
    min_power = float('inf')
    chosen = [] # 가장 약한놈들을 선택, (x, y)를 저장

    for i in range(1, N+1):
        for j in range(1, M+1):
            if boards[i][j] == 0:
                continue
            if boards[i][j] < min_power:
                chosen = [(i, j)]
                min_power = boards[i][j]
            elif boards[i][j] == min_power:
                chosen.append((i, j))

    if len(chosen) == 1:
        x, y = chosen[0]
        return x, y

    # 2개 이상이라면 가장 최근에 공격한 포탑을 선정
    most_recent = 0
    second_chosen = []
    for board in chosen:
        x, y = board
        if recent_battle[x][y] > most_recent:
            second_chosen = [(x, y)]
            most_recent = recent_battle[x][y]
        elif recent_battle[x][y] == most_recent:
            second_chosen.append((x, y))

    if len(second_chosen) == 1:
        x, y = second_chosen[0]
        return x, y


    # 2개 이상이라면 행+열 값이 가장 큰 포탑을 선정
    max_total = 0
    third_chosen = []
    for i in range(len(second_chosen)):
        x, y = second_chosen[i]
        if x+y > max_total:
            third_chosen = [(x, y)]
            max_total = x+y
        elif x+y == max_total:
            third_chosen.append((x, y))

    if len(third_chosen) == 1:
        x, y = third_chosen[0]
        return x, y

    # 2개 이상이라면 열 값이 가장 큰 포탑을 선정
    third_chosen.sort(key=lambda x: -x[1]) # 열 값이 큰 순서대로 정렬
    x, y = third_chosen[0]
    return x, y

# 피해자 선정하는 함수, 좌표(x,y)를 return함
def select_victim():
    # 가장 강한놈들만 선정
    max_power = 0
    chosen = []  # 가장 강한놈들을 선택, (x, y)를 저장
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if boards[i][j] == 0 or (i,j) == (attacker_x, attacker_y): # 망가진 포탑과 자기자신은 제외
                continue
            if boards[i][j] > max_power:
                chosen = [(i,j)]
                max_power = boards[i][j]
            elif boards[i][j] == max_power:
                chosen.append((i,j))

    if len(chosen) == 1:
        x, y = chosen[0]
        return x, y

    # 2개 이상이라면 가장 오래전에 공격한 포탑을 선정
    most_ago = float('inf')
    second_chosen = []
    for board in chosen:
        x, y = board
        if recent_battle[x][y] < most_ago:
            second_chosen = [(x, y)]
            most_ago = recent_battle[x][y]
        elif recent_battle[x][y] == most_ago:
            second_chosen.append((x, y))

    if len(second_chosen) == 1:
        x, y = second_chosen[0]
        return x, y

    # 2개 이상이라면 행+열 값이 가장 작은 포탑을 선정
    min_total = float('inf')
    third_chosen = []
    for board in second_chosen:
        x, y = board
        if x+y < min_total:
            third_chosen = [(x, y)]
            min_total = x+y
        elif x+y == min_total:
            third_chosen.append((x, y))

    if len(third_chosen) == 1:
        x, y = third_chosen[0]
        return x, y

    # 2개 이상이라면 열 값이 가장 작은 포탑을 선정
    third_chosen.sort(key=lambda x: x[1]) # 열 값이 작은 순서대로 정렬
    x, y = third_chosen[0]
    return x, y

def attack_lazer(x,y): # 레이저 공격을 하는 포탑의 좌표 (x,y)를 받음
    original_x = x; original_y = y
    related_battle[x][y] = True
    while True:
        # 당장에 최단거리인 방향을 골라냄
        d_list = [] # (d, nx, ny)를 저장
        shortest = distance[x][y] # 가야할 위치가 자기자신보다는 dist가 작아야 하므로
        for i in range(4):
            nx, ny = process_nx_ny(x + dx[i], y + dy[i])

            if distance[nx][ny] < shortest:
                d_list = [(i, nx, ny)]
                shortest = distance[nx][ny]
            elif distance[nx][ny] == shortest:
                d_list.append((i, nx, ny))

        # 우/하/좌/상 우선순위대로 딱 하나만 골라냄
        d_list.sort(key=lambda x: x[0])

        # 진격하면서 공격함
        _, x, y = d_list[0]
        # print(f'[{x}][{y}] 공격받음')
        related_battle[x][y] = True

        if distance[x][y] == 0:
            boards[x][y] -= boards[original_x][original_y] # 맞으면 (공격자의 공격력)만큼 감소
            break
        else:
            boards[x][y] -= boards[original_x][original_y] // 2 # 맞으면 (공격자의 공격력/2)만큼 감소

def attack_bomb(victim_x,victim_y):
    related_battle[attacker_x][attacker_y] = True # 전투와 관련되어 있음

    # 대각선도 고려해줘야 한다.
    dx_temp = dx[:] + [-1, -1, 1, 1]
    dy_temp = dy[:] + [-1, 1, -1, 1]

    for i in range(len(dx_temp)):
        nx, ny = process_nx_ny(victim_x + dx_temp[i], victim_y + dy_temp[i])

        if boards[nx][ny] != 0 and (nx,ny) != (attacker_x, attacker_y):
            boards[nx][ny] -= boards[attacker_x][attacker_y] // 2 # 주변은 1/2 만큼 피해를 입음
            related_battle[nx][ny] = True # 전투와 관련되어 있음

    boards[victim_x][victim_y] -= boards[attacker_x][attacker_y] # 타겟은 정확하게 피해를 입음
    related_battle[victim_x][victim_y] = True  # 전투와 관련되어 있음

# 전투와 무관한 포탑들 회복
def heal():
    for i in range(1, N+1):
        for j in range(1, M+1):
            if not related_battle[i][j] and boards[i][j] != 0: # 전투와 무관하며, 망가진 포탑이 아닐 경우
                boards[i][j] += 1




# for row in boards:
#     print(row)
# print("-----")

turn = 1
while turn <= K:
    related_battle = [[False] * (M + 1) for _ in range(N + 1)]  # 공격과 관련있는지 확인하는 2차원 배열 (매번 초기화 해야함)

    # 공격자 선정
    attacker_x, attacker_y = select_attacker()
    # 공격자 공격력 증가
    boards[attacker_x][attacker_y] += N+M
    # print(f'공격자 선정: ({attacker_x},{attacker_y})')

    # 피해자 선정
    victim_x, victim_y = select_victim()
    # print(f'피해자 선정: ({victim_x},{victim_y})')

    # 레이저 공격이 가능한지 알아보기 위한 bfs
    bfs(victim_x, victim_y)

    # 공격
    if distance[attacker_x][attacker_y] != float('inf'): # bfs 결과, 레이저 공격을 할 수 있다는 뜻
        attack_lazer(attacker_x, attacker_y)
    else:
        attack_bomb(victim_x, victim_y)

    # 공격자의 recent_battle 갱신
    recent_battle[attacker_x][attacker_y] = turn

    # 무관한 포탑 힐함
    heal()

    potap_count = 0 # 포탑 개수
    # 음수는 0으로 수정
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if boards[i][j] < 0:
                boards[i][j] = 0
            elif boards[i][j] > 0:
                potap_count += 1

    if potap_count == 1:
        break

    turn += 1

    # for row in boards:
    #     print(row)
    # print("-----------")

ans = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        ans = max(ans, boards[i][j])

print(ans)