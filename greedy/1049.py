# 각 브랜드에 대해 입력을 받을때마다 패키지의 최소가격과 낱개의 최소가격을 저장
# 낱개 6개를 사는 가격과 패키지 1개를 사는 가격을 비교
# 1. 낱개 6개를 사는 가격이 더 싸거나 같다면 낱개로만 구매
# 2. 패키지 1개를 사는 가격이 더 싸다면
#   2-1) 나머지 개수를 낱개로 사는게 싼지 패키지로 사는게 싼지 비교하고 처리

N, M = map(int, input().split())
min_package = 1001
min_piece = 1001
cost = 0

for _ in range(M):
    package, piece = map(int, input().split())
    min_package = min(package, min_package)
    min_piece = min(piece, min_piece)

if N >= 6:
    if min_package <= min_piece * 6:
        cost = cost + min_package * (N // 6)
        N = N % 6
    else:
        cost = cost + min_piece * N
        N = 0

if min_package <= min_piece * N:
    cost = cost + min_package
    N = 0
else:
    cost = cost + min_piece * N
    N = 0

print(cost)