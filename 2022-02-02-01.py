import heapq
from collections import deque

n, m = map(int, input().split())

places = [[8] * (n+1)]
base_camps = [] # (x,y)를 저장함
no_access = [[False] * (n+1) for _ in range(n+1)]
goals = [(0, 0, 0)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
# people = [] # 현재 움직이고 있

ready_member = deque() # 준비중인 멤버 (번호를 저장)
moving_member = deque()  # 움직이고 있는 멤버 (번호, 현재 x, 현재 y) 저장

for i in range(n):
    row = list(map(int, input().split()))
    places.append([8] + row)

    for j in range(n):
        if row[j] == 1:
            base_camps.append((i+1, j+1))

for i in range(1, m+1):
    x, y = map(int, input().split())
    goal = (i, x, y) # idx, x, y
    goals.append(goal)
    ready_member.append(i)

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

# 유저의 번호를 받아, 유저의 목적지까지의 최단거리를 찾지만, 경로를 저장하지 않고 방향을 저장함
def dijkstra(idx, cur_x, cur_y):
    goal_x, goal_y = goals[idx][1], goals[idx][2]
    visited = [[False] * (n+1) for _ in range(n+1)]
    shortest = float('inf')
    cur_dist = 0
    roots = []
    queue = []
    heapq.heappush(queue, (cur_dist, cur_x, cur_y, []))
    visited[cur_x][cur_y] = True

    while queue:
        dist, x, y, root = heapq.heappop(queue)
        if dist > shortest:
            continue
        if x == goal_x and y == goal_y:
            shortest = dist
            roots.append(root)
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not in_range(nx, ny):
                continue

            if not no_access[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(queue, (dist+1, nx, ny, root + [i]))

    return roots, shortest

# 네 방향중 가장 적합한 방향을 찾음
def find_optimal_root(roots):
    roots.sort(key = lambda x: x[0])
    return roots[0][0]

# 사용자의 번호를 입력받아서 가능한 모든 베이스캠프를 찾음
def find_basecamp(idx):
    shortest = float('inf')
    available_camps = []
    for i in range(len(base_camps)):
        base_camp_x = base_camps[i][0]
        base_camp_y = base_camps[i][1]

        _, distance = dijkstra(idx, base_camp_x, base_camp_y)

        if distance < shortest:
            shortest = distance
            available_camps = [(base_camp_x, base_camp_y)]
        elif distance == shortest:
            available_camps.append((base_camp_x, base_camp_y))

    return available_camps

# 가능한 모든 베이스캠프 중에 가장 적합한 베이스캠프를 찾음
def find_optimal_basecamp(available_camps):
    optimal = (n+1, n+1)
    for camp in available_camps:
        camp_row = camp[0]
        camp_col = camp[1]
        if camp_row < optimal[0]:
            optimal = camp
        elif camp_row == optimal[0]:
            if camp_col < optimal[1]:
                optimal = camp

    return optimal

def move(idx, nx, ny):
    # 좌표를 바꿔줌
    for i in range(len(moving_member)):
        num, cur_x, cur_y = moving_member[i]
        if num == idx:
            moving_member[i] = (num, nx, ny) # 좌표 업데이트


t = 0
while moving_member or ready_member:

    t+=1
    # 1번
    for idx, member in enumerate(moving_member):
        member_num, member_x, member_y = member
        roots, _ = dijkstra(member_num, member_x, member_y)
        d = find_optimal_root(roots)

        nx = member_x + dx[d]
        ny = member_y + dy[d]
        move(member_num, nx, ny)

    # 2번
    remove_list = [] # 지워야할 목록 저장
    for idx, member in enumerate(moving_member):
        member_num, member_x, member_y = member
        _, goal_x, goal_y = goals[member_num]
        if goal_x == member_x and goal_y == member_y:
            remove_list.append(member)
            no_access[member_x][member_y] = True
    for target in remove_list:
        moving_member.remove(target)

    # 3번
    if ready_member and ready_member[0] >= t:
        num = ready_member.popleft()

        available = find_basecamp(num) # 이용 가능한 모든 베이스캠프를 찾음
        optimal_camp = find_optimal_basecamp(available)

        x, y = optimal_camp
        base_camps.remove(optimal_camp) # 남아있는 베이스캠프 목록에서 지움
        no_access[x][y] = True # 접근 불가로 설정
        moving_member.append((num, x, y))

    # for place in no_access:
    #     print(place)
    # print(f'움직이고 있는 멤버: {moving_member}')
    # print(f'대기하고 있는 멤버: {ready_member}')
    # print("----------------")

print(t)