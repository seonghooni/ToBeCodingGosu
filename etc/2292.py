import math

N = int(input())

left = (N-1) / 3
i = 1
while True:
    if left > i * (i-1):
        i += 1
    else:
        print(i)
        break