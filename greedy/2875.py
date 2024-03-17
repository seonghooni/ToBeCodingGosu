n, m, k = map(int, input().split())

num_solo = 0
num_team = 0

if m > n//2: # 남자x2가 여자보다 더 많음
    num_solo += m - n//2
    num_solo += n%2
    num_team = n//2
else:       # 그 외의 경우
    num_solo = n - m*2
    num_team = m

if k - num_solo > 0: # 대회에 필요한 인원이 남는 인원보다 많을 경우
    k = k - num_solo
    while k > 0:
        n = n-2
        m = m-1
        k = k-3
        num_team = num_team-1

print(num_team)
