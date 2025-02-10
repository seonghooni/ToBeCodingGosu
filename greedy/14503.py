N, M = map(int, input().split())
i, j, dir = map(int, input().split())

directions = ((-1, 0), (0, 1), (1, 0), (0, -1)) # 북 동 남 서

rooms = []
for _ in range(N):
    rooms.append(list(map(int, input().split())))

count = 0

while True:
    if rooms[i][j] == 0:
        rooms[i][j] = 2
        count += 1

    is_exist_room = False
    for dx, dy in directions:
        nx = i + dx
        ny = j + dy
        if rooms[nx][ny] == 0:
            is_exist_room = True

    if not is_exist_room: # 주변에 빈 방이 존재하지 않는다면
        dir_x, dir_y = directions[dir]
        if rooms[i - dir_x][j - dir_y] != 1:
            i = i - dir_x
            j = j - dir_y
            continue
        else:
            break
    else: # 주변에 빈 방이 존재한다면
        dir = dir - 1 if dir > 0 else 3
        dir_x, dir_y = directions[dir]
        if rooms[i + dir_x][j + dir_y] == 0:
            i = i + dir_x
            j = j + dir_y

print(count)





