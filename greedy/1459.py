x, y, w, s = map(int, input().split())

result = 0
if 2*w < s: # 일직선으로 2번 가는게 대각선 1번보다 무조건 이득일 경우
    result = w * (x+y)
else:
    sol_1 = min(x, y) * s + abs(x - y) * w  # 대각선 + 일직선
    if (x+y) % 2 == 0: # x좌표와 y좌표의 합이 짝수인 경우
        sol_2 = max(x,y) * s # 대각선으로만 가는 경우
    else: # x좌표와 y좌표의 합이 홀수인 경우
        sol_2 = (max(x,y) - 1) * s + w # 대각선으로만 다 채우고, 일직선 1번
    result = min(sol_1, sol_2)

print(result)