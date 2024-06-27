# 사실상 dfs 문제인데, dfs 문제가 너무 오랜만이라 잘 못풀었다.
# 다만 27번째 줄의 경우, 파이프가 목적지까지 도달하지 못할 경우 기존에 타고왔던 경로는 다시 not visited로 해줘야 하지 않나?
# 27번째 줄을 실행할 경우 시간초과, 실행하지 않을 경우 통과가 된다...

R, C = map(int, input().split())

route = []
visited = [[-1 for _ in range(C)] for _ in range(R)]

for _ in range(R):
    route.append(list(input()))

result = 0
dx = [-1, 0, 1]

def dfs(x, y):
    if y == C-1:
        return True

    for i in range(3):
        ax = x + dx[i]
        ay = y + 1
        if 0 <= ax < R and ay < C:
            if route[ax][ay] == '.' and visited[ax][ay] == -1:
                visited[ax][ay] = 1
                if dfs(ax, ay):
                    return True
    # visited[x][y] = -1
    return False

for i in range(R):
    if dfs(i,0):
        result += 1
print(result)