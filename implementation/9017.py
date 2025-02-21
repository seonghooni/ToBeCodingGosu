T = int(input())
for _ in range(T):
    N = int(input())

    inputs = list(map(int, input().split()))

    total_count = dict()
    actual_score_board = dict() # 참여하는 팀만 기록한 보드

    # 팀마다 참여한 팀원의 수 확인
    for i in range(len(inputs)):
        team_member_count = total_count.get(inputs[i], 0)
        team_member_count += 1
        total_count[inputs[i]] = team_member_count

    for team_number, member_count in total_count.items():
        if member_count == 6:
            actual_score_board[team_number] = []

    # 참여한 팀만 유효하게 점수 기록
    score = 1
    for i in range(len(inputs)):
        if inputs[i] in actual_score_board.keys():
            actual_score_board[inputs[i]].append(score)
            score+=1

    min_score = 6000 # 최저 점수
    min_team_number = 0

    for team_number, score_arr in actual_score_board.items():

        current_team_score = sum(score_arr[0:4])
        if current_team_score == min_score:
            min_team_score_arr = actual_score_board[min_team_number]
            if score_arr[4] < min_team_score_arr[4]:
                min_team_number = team_number
        elif current_team_score < min_score:
            min_score = current_team_score
            min_team_number = team_number

    print(min_team_number)