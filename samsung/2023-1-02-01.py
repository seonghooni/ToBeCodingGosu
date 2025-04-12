N, M, K = map(int, input().split())

miros = [[0] * (N+1)]
for _ in range(N):
    miro = [0] + list(map(int,input().split()))
    miros.append(miro)

people = []
for _ in range(M):
    person = list(map(int, input().split()))
    people.append(person)

exit_space = list(map(int, input().split()))

dx = [-1, 1, 0, 0] # 상/하 먼저
dy = [0, 0, -1, 1] # 상-하-좌-우

move_count = 0
# 범위 내에 있는지 확인하는 함수
def in_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

# 가장 작은 정사각형 한 변의 길이를 찾고, 해당하는 사람의 [idx]도 함께 return
def cal_minimum_rec():
    exit_x, exit_y = exit_space
    idx_list = []
    smallest = float('inf')
    for i in range(len(people)):
        x, y = people[i][0], people[i][1]
        length = max(abs(exit_x - x), abs(exit_y - y))
        if length < smallest:
            idx_list = [i]
            smallest = length
        elif length == smallest:
            idx_list += [i]
    return idx_list, smallest+1

def find_direction(x, y):
    exit_x, exit_y = exit_space
    d_list = []
    if x > exit_x: # 출구가 위쪽에 있다면
        d_list.append(0)
    elif x < exit_x:
        d_list.append(1)

    if y > exit_y: # 출구가 왼쪽에 있다면
        d_list.append(2)
    elif y < exit_y:
        d_list.append(3)

    return d_list

# 이동하는 함수(막혀있다면 가지 않음)
def move(i):
    x, y = people[i]
    d_list = find_direction(x, y)
    d_list.sort() # 상 하 좌 우 순서로 처리
    global move_count

    for d in d_list:
        nx = x + dx[d]
        ny = y + dy[d]
        if not in_range(nx, ny):
            continue
        if miros[nx][ny] > 0: # 벽이라면 stay
            nx = x
            ny = y
        else: # 벽이 아니라면 다른 방향은 따질 것도 없이 그 방향으로 간다.
            people[i] = [nx, ny]
            move_count += 1
            break


# 왼쪽 꼭짓점 찾는 함수
def find_point(i, distance_rec):
    person = people[i]
    x, y = person
    exit_x, exit_y = exit_space
    left = person; right = person # default로는 person으로 설정
    if y > exit_y: # 출구가 더 왼쪽
        left = exit_space
    elif y < exit_y:
        right = exit_space

    points = []
    if left == right: # 좌우 차이가 없다면
        if person[0] < exit_space[0]: # 더 높은걸 찾음
            high = person
        else:
            high = exit_space
        for i in range(distance_rec+1):
            points.append((high[0], high[1]-i))
    elif left[0] > right[0]: # 왼쪽이 높이가 더 낮으면
        points.append((left[0]-distance_rec, left[1]))
        points.append((right[0], right[1]-distance_rec))
    elif left[0] < right[0]: # 왼쪽의 높이가 더 높으면
        points.append((left[0], left[1]))
        points.append((right[0]-distance_rec, right[1]-distance_rec))
    else: # 높이가 둘 다 같으면
        for i in range(distance_rec+1):
            points.append((left[0]-i, left[1]))

    return points # [[x, y], ...]

# 좌상단 꼭짓점을 입력 받고, 정상적인 정사각형인지 확인
def is_rectangle_valid(x, y, length):
    return in_range(x,y) and in_range(x+length, y) and in_range(x,y+length) and in_range(x+length, y+length)

def find_optimal_rec(point_set):
    li = list(point_set)
    li.sort(key = lambda x: (x[0], x[1]))
    return li[0]

def rotate_90(arr, start_x, start_y, length):
    n = len(arr)
    global exit_space
    original_people = people[:]
    new_arr = [row[:] for row in arr]
    nx, ny = exit_space

    for x in range(start_x, start_x+length):
        for y in range(start_y, start_y+length):
            ox = x - start_x
            oy = y - start_y
            rx = oy
            ry = length-1-ox
            new_arr[start_x+rx][start_y+ry] = arr[x][y]
            if new_arr[start_x+rx][start_y+ry] > 0:
                new_arr[start_x + rx][start_y + ry] -= 1


            for i in range(len(original_people)):
                if original_people[i][0] == x and original_people[i][1] == y:
                    people[i] = [start_x+rx, start_y+ry]

            if exit_space[0] == x and exit_space[1] == y:
                nx = start_x+rx; ny = start_y+ry

    exit_space = [nx, ny]

    return new_arr


def print_miro():
    for miro in miros:
        print(miro)


minute = 0
while minute < K:
    minute += 1
    print(f'minute={minute}')
    for i in range(len(people)):
        move(i)
    temp = people[:]
    for person in temp:
        if person == exit_space:
            people.remove(person)

    # rectangle의 꼭짓점과 길이를 구해서 딱 하나 지정하는 과정
    idx_list, length = cal_minimum_rec() # 목록과 최소 길이
    point_set = set()
    for i in range(len(idx_list)):
        points = find_point(i, length-1)
        for point in points:
            x, y = point
            if is_rectangle_valid(x, y, length-1):
                point_set.add((x,y))
    start_x, start_y = find_optimal_rec(point_set)

    miros = rotate_90(miros, start_x, start_y, length)
    print_miro()
    print(people)
    print("--------")

print(move_count)
print(exit_space[0], exit_space[1])
# 꼭짓점 테스트
# for i in range(M):
#     points = find_point(i)
#     for point in points:
#         print(point[0], point[1])
#
#     print("--------")




