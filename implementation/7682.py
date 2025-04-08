import sys
input = sys.stdin.readline

def determine(arr, x1, x2, x3):
    if arr[x1] == arr[x2] == arr[x3]:
        return True
    else:
        return False

while True:
    board = input().strip()
    if board == 'end':
        exit()

    x_is_win = False
    o_is_win = False
    is_just_finished = False  # 그냥 끝난 경우
    x_count = 0
    o_count = 0

    for i in range(len(board)):
        if board[i] == 'O':
            o_count += 1
        elif board[i] == 'X':
            x_count += 1

    if board[0] != '.':
        if determine(board, 0, 3, 6) or determine(board, 0, 1, 2) or determine(board, 0, 4,
                                                                               8):  # 하나만 성공하는 여부를 따져봐야할까? 그건 나중에..
            if board[0] == 'O':
                if o_count == x_count:
                    o_is_win = True
                else:
                    print("invalid")
                    continue
            else:
                if x_count == o_count + 1:
                    x_is_win = True
                else:
                    print("invalid")
                    continue
    if board[1] != '.':
        if determine(board, 1, 4, 7):
            if board[1] == 'O':
                if o_count == x_count:
                    o_is_win = True
                else:
                    print("invalid")
                    continue
            else:
                if x_count == o_count + 1:
                    x_is_win = True
                else:
                    print("invalid")
                    continue
    if board[2] != '.':
        if determine(board, 2, 5, 8) or determine(board, 2, 4, 6):
            if board[2] == 'O':
                if o_count == x_count:
                    o_is_win = True
                else:
                    print("invalid")
                    continue
            else:
                if x_count == o_count + 1:
                    x_is_win = True
                else:
                    print("invalid")
                    continue
    if board[3] != '.':
        if determine(board, 3, 4, 5):
            if board[3] == 'O':
                if o_count == x_count:
                    o_is_win = True
                else:
                    print("invalid")
                    continue
            else:
                if x_count == o_count + 1:
                    x_is_win = True
                else:
                    print("invalid")
                    continue

    if board[6] != '.':
        if determine(board, 6, 7, 8):
            if board[6] == 'O':
                if o_count == x_count:
                    o_is_win = True
                else:
                    print("invalid")
                    continue
            else:
                if x_count == o_count + 1:
                    x_is_win = True
                else:
                    print("invalid")
                    continue

    if (x_is_win and not o_is_win) or (not x_is_win and o_is_win):
        print("valid")
        continue
    elif x_is_win and o_is_win:
        print("invalid")
        continue

    # 그냥 끝난 경우
    if x_count == 5 and o_count == 4:
        print("valid")
        continue
    else:
        print("invalid")
        continue