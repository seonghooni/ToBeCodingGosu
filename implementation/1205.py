N, new_score, P = map(int, input().split())

if N == 0:
    print(1)
    exit()
ranking = list(map(int, input().split()))
current_rank = N+1

target_rank = N
while True:
    if current_rank == 1:
        break
    if new_score > ranking[target_rank-1]:
        if target_rank == 1:
            current_rank = 1
            break

        current_rank = target_rank
        target_rank -= 1
        continue
    elif new_score == ranking[target_rank-1]:
        if new_score == ranking[N-1] and N == P:
            print(-1)
            exit()
        current_rank = target_rank
        target_rank -= 1
    else:
        break

if current_rank > P:
    print(-1)
else:
    print(current_rank)