N, M = map(int, input().split())

places = [[]]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

cctv_infos = []

for i in range(N):
    row = list(map(int, input().split()))
    places.append([0] + row)
    for j in range(len(row)):
        if row[j] in (1,2,3,4,5):
            cctv_infos.append((i+1, j+1, row[j])) # (x, y, cctv_num)

total_count = len(cctv_infos)

# print(cctv_infos)

# print(places)
def cctv_1(arr, x, y, num):
    nx = x + dx[num] # num = 0, 1, 2, 3
    ny = y + dy[num]

    while 1 <= nx <= N and 1 <= ny <= M and arr[nx][ny] != 6:
        if arr[nx][ny] == 0:
            arr[nx][ny] = 8 #          ->  8 == "#"

        nx += dx[num]
        ny += dy[num]

def cctv_2(arr, x, y, num):
    if num == 0 or num == 2:
        for n in (0, 2):
            nx = x + dx[n]
            ny = y + dy[n]
            while 1 <= nx <= N and 1 <= ny <= M and arr[nx][ny] != 6:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 8  # ->  8 == "#"
                nx += dx[n]
                ny += dy[n]

    else:
        for n in (1, 3):
            nx = x + dx[n]
            ny = y + dy[n]
            while 1 <= nx <= N and 1 <= ny <= M and arr[nx][ny] != 6:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 8  # ->  8 == "#"
                nx += dx[n]
                ny += dy[n]

def cctv_3(arr, x, y, num):
    for n in (num, (num - 1) % 4):
        nx = x + dx[n]
        ny = y + dy[n]
        while 1 <= nx <= N and 1 <= ny <= M and arr[nx][ny] != 6:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 8  # ->  8 == "#"
            nx += dx[n]
            ny += dy[n]

def cctv_4(arr, x, y, num):
    for n in (num, (num - 1) % 4, (num - 2) % 4):
        nx = x + dx[n]
        ny = y + dy[n]
        while 1 <= nx <= N and 1 <= ny <= M and arr[nx][ny] != 6:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 8  # ->  8 == "#"
            nx += dx[n]
            ny += dy[n]

def cctv_5(arr, x, y, num):
    for n in range(4):
        nx = x + dx[n]
        ny = y + dy[n]
        while 1 <= nx <= N and 1 <= ny <= M and arr[nx][ny] != 6:
            if arr[nx][ny] == 0:
                arr[nx][ny] = 8  # ->  8 == "#"
            nx += dx[n]
            ny += dy[n]


def make_permutation(cctv_count):
    global cases
    cases = [[]]  # 초기값: 빈 리스트 하나

    for _ in range(cctv_count):
        new_cases = []
        for case in cases:
            for i in range(4):
                new_cases.append(case + [i])
        cases = new_cases

make_permutation(total_count)
# print(cases)

min_cnt = 65
for case in cases:
    temp = [row[:] for row in places]
    for i in range(total_count):
        x, y, cctv_num = cctv_infos[i]

        if cctv_num == 1:
            cctv_1(temp, x, y, case[i])
        elif cctv_num == 2:
            cctv_2(temp, x, y, case[i])
        elif cctv_num == 3:
            cctv_3(temp, x, y, case[i])
        elif cctv_num == 4:
            cctv_4(temp, x, y, case[i])
        elif cctv_num == 5:
            cctv_5(temp, x, y, case[i])

    # for temp_row in temp:
    #     print(temp_row)

    cnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if temp[i][j] == 0:
                cnt += 1

    min_cnt = min(cnt, min_cnt)

print(min_cnt)
# cctv_5(places, 3, 3, 0)



