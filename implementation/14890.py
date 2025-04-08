
N, L = map(int, input().split())

roads = []

for _ in range(N):
    roads.append(list(map(int, input().split())))

cnt = 0

# ----- L만큼 높이가 연속되는지 확인하는 함수
def continuous_determine(arr, visitied, start_at, height, L, right_side):
    length = 0
    is_continuous = False

    if right_side: # 오른쪽으로
        for k in range(L):  # L만큼 높이가 연속되는지 확인
            if start_at + k >= N: # index check
                break

            if arr[start_at + k] == height and not visitied[start_at + k]: # 시작지점부터 카운트
                length += 1
                if length == L:
                    is_continuous = True
                    break
            else:
                break
    else: # 왼쪽으로 L만큼 높이가 연속되는지 확인
        for k in range(L):
            if start_at - k < 0: # index check
                break

            if arr[start_at - k] == height and not visitied[start_at - k]:
                length += 1
                if length == L:
                    is_continuous = True
                    break
            else:
                break

    return is_continuous


root = []

for j in range(N):
    root.append(roads[j])
    temp = []
    for k in range(N):
        temp.append(roads[k][j])

    root.append(temp)

for row in root: # 여기로 돌아가고 싶음
    visited = [False] * N
    if all(x == row[1] for x in row):
        cnt += 1
        continue

    for i in range(len(row)-1):
        dif = row[i] - row[i+1]
        if dif == 1: # i+1 이 더 작을 경우 "\" 모양
            if continuous_determine(row, visited, i+1, row[i+1], L, right_side=True):
                if i+1+L < N and row[i+1+L] > row[i+1]: #"\|" 모양 방지
                    break
                for k in range(i+1, i+1+L):
                    visited[k] = True
            else:
                break

        elif dif == -1: # i 이 더 작을 경우 "/" 모양
            if continuous_determine(row, visited, i, row[i], L, right_side=False):
                for k in range(i, i-L, -1):
                    visited[k] = True
            else:
                break
        elif dif == 0:
            continue
        else: # 차이가 1이나 0이 아닐 경우
            break

    else:
        cnt += 1

print(cnt)