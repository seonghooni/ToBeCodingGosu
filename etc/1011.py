import math

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    distance = y-x

    n = math.ceil(math.sqrt(distance))

    half = ( n**2 - (n-1)**2 - 1 ) / 2

    if distance <= (n-1)**2 + half:
        result = n*2 - 2
    else:
        result = n*2 - 1

    print(result)

