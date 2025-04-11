L, N, Q = map(int, input().split())

chess = [[0] * (L+1)]
traps = []
for i in range(L):
    row = list(map(int, input().split()))
    for j in range(L):
        if row[j] == 1:
            traps.append((i+1, j+1))
    chess.append([0] + row)

knights_info = [[0]]
for i in range(1, N+1):
    knights_info.append(list(map(int, input().split())))

orders = []
for i in range(Q):
    orders.append(list(map(int, input().split())))

hp = [0] * (N+1) # 기사들의 체력을 담는 배열
initial_hp = [0]
boards = [[0] * (L+1) for _ in range(L+1)] # 보드 모양 저장 (기사들의 위치를 기록)
knights = [[] for _ in range(N+1)] # 기사들의 연쇄적인 위치를 기록할 것임 ex) knights[1] = [(0,1), (0,2)]
before_move = [] # 움직이기 전의 좌표가 저장되는 곳 (num, x, y)
after_move = [] # 움직인 이후의 좌표가 저장되는 곳 (num, x, y)

dx = [-1, 0, 1, 0] # 위/오/아/왼
dy = [0, 1, 0, -1]

# 기사 정보를 내가 필요한 변수에 담는 함수
def init():
    for i in range(1, N+1):
        r, c, h, w, k = knights_info[i]
        hp[i] = k

        for j in range(h):
            for k in range(w):
                boards[r+j][c+k] = i
                knights[i].append((r+j, c+k))



def print_2d(arr_2d):
    for arr in arr_2d:
        print(arr)
    print("-----")

# (기사의 번호, 방향)를 입력받아, 움직일 수 있는지 확인할 것임 (벽이나 타일을 벗어나는지만 확인)
def can_move(knight_num, d):
    spaces = knights[knight_num]

    for space in spaces:
        x, y = space
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 1 or nx > L or ny < 1 or ny > L:
            return False

        if chess[nx][ny] == 2:
            return False

    return True  # ← 들여쓰기를 for문 바깥으로 맞춰줌

def can_totally_move(knight_num, d):
    i_can = can_move(knight_num, d) # 자기자신부터 봐야함
    if i_can: # 자기자신은 움직일 수 있다면
        adjacent_knights = set()
        # 인접한 기사들도 봐야함
        for x, y in knights[knight_num]:
            nx = x + dx[d]
            ny = y + dy[d]
            if boards[nx][ny] != knight_num and boards[nx][ny] != 0: # 인접한 기사가 자기자신이 아닐 경우
                adjacent_knights.add(boards[nx][ny])

        for adjacent_num in adjacent_knights:
            if not can_totally_move(adjacent_num, d): # 인접한 기사에서 하나라도 이동불가능하다고 결론이 날 경우
                return False

        return True
    else: # 자기자신이 움직일 수 없다면 False 리턴
        return False
def move(knight_num, d, order_num):
    before_move = []
    after_move = []

    for i in range(len(knights[knight_num])):
        x, y = knights[knight_num][i]
        nx = x + dx[d]
        ny = y + dy[d]

        knights[knight_num][i] = (nx, ny)
        before_move.append((knight_num, x, y))
        after_move.append((knight_num, nx, ny))

    update(before_move, after_move)

    if knight_num != order_num:
        hurt(knight_num)

def totally_move(knight_num, d, order_num):
    # 인접한 기사들도 연쇄적으로 이동
    adjacent_knights = set()
    for x, y in knights[knight_num]:
        nx = x + dx[d]
        ny = y + dy[d]
        if boards[nx][ny] != knight_num and boards[nx][ny] != 0:  # 인접한 기사가 자기자신이 아닐 경우
            adjacent_knights.add(boards[nx][ny])

    for adjacent_num in adjacent_knights:
        totally_move(adjacent_num, d, order_num)

    move(knight_num, d, order_num)

# 기사의 번호를 입력받고, 범위 내에 지뢰가 있다면 hp를 깎음
ans = 0

def hurt(knight_num):
    global ans
    places = knights[knight_num]

    for (x, y) in places:
        if (x, y) in traps:
            if hp[knight_num] > 0:
                hp[knight_num] -= 1

    if hp[knight_num] <= 0:
        remove_list = []
        for num, x, y in after_move:
            if num == knight_num:
                remove_list.append((num,x,y))

        for num, x, y in remove_list:
            after_move.remove((num,x,y))

        for (x, y) in places:
            boards[x][y] = 0
        knights[knight_num] = [] # 죽으면 기록을 지움


# 기사에게 명령을 내리고 종합적으로 이동 가능하면, 이동시키는 함수
def order(knight_num, d):
    # 가려는 방향으로 진출할 수 있는지 종합적으로 확인함
    if can_totally_move(knight_num, d):
        totally_move(knight_num, d, knight_num)

# board를 초기화함
def update(before_move, after_move):
    for _, x, y in before_move:
        boards[x][y] = 0

    for num, x, y in after_move:
        boards[x][y] = num

init()
initial_hp = hp[:]

# print_2d(boards)
for num, d in orders:
    if knights[num]:
        order(num, d)

    # print_2d(boards)

for i in range(1, len(hp)):
    if hp[i] > 0:
        ans += initial_hp[i] - hp[i]
print(ans)
# print(knights)
# totally_move(2, 1, 2)

# print(knights)

