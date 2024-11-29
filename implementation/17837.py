N, K = map(int, input().split())
board = []
first_row = [0] * (N+1) # 보드의 색깔에 대한 정보를 담고 있는 배열
board.append(first_row)
info = []
current_board = [[[] for _ in range(N+1)] for _ in range(N+1)] # 말의 순서에 대한 정보를 담고 있는 배열
dy = [0, 0, 0, -1 ,1] # 행
dx = [0, 1, -1, 0, 0] # 열

for _ in range(N):
    row = list(map(int, input().split()))
    row.insert(0, 0)
    board.append(row)

for _ in range(K):
    info.append(list(map(int, input().split())))

for i in range(K):
    y = info[i][0] # 행
    x = info[i][1] # 열
    current_board[y][x].append(i)

turn = 0

while turn < 1001:
    turn += 1
    if turn > 1000:
        print(-1)

    # 한 사이클 실행
    for i in range(K):
        y = info[i][0]
        x = info[i][1]

        # 미리 가는 타일을 확인
        ay = y + dy[info[i][2]]
        ax = x + dx[info[i][2]]

        # already_reverse = False # 이미 방향전환 된 것인지 확인 (중복으로 방향전환시키지 않기 위함)
        if ax < 1 or ax > N or ay < 1 or ay > N or board[ay][ax] == 2: # 1. 범위를 초과할 경우 2. 파란색 타일일 경우
            # 방향 전환
            if info[i][2] == 1 or info[i][2] == 3:
                info[i][2] += 1
            else:
                info[i][2] -= 1

            ay = y + dy[info[i][2]]
            ax = x + dx[info[i][2]]
            # already_reverse = True


        if ax < 1 or ax > N or ay < 1 or ay > N or board[ay][ax] == 2: # 다시한번 파란색이거나 범위를 초과할 경우
            ay = y
            ax = x
        elif board[ay][ax] == 0: # 다음 타일이 흰색일 경우
            move_list = []
            while True:
                num = current_board[y][x].pop()
                move_list.append(num)
                if num == i:
                    break
            move_list.reverse()
            current_board[ay][ax].extend(move_list)

            for j in move_list:
                info[j][0] = ay
                info[j][1] = ax

        elif board[ay][ax] == 1: # 다음 타일이 빨간색일 경우
            move_list = []
            while True:
                num = current_board[y][x].pop()
                move_list.append(num)
                if num == i:
                    break
            current_board[ay][ax].extend(move_list)

            for j in move_list:
                info[j][0] = ay
                info[j][1] = ax

        if len(current_board[y][x]) == 4:
            print(turn)
            exit()


