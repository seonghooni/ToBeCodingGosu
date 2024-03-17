N = int(input())

x = N // 5
while True:

    remainder = N - 5*x

    if remainder % 3 == 0:
        y = remainder // 3
        print(x+y)
        exit()
    else:
        x -= 1
        # x가 음수이면 -1 출력
        if x == -1:
            print(-1)
            exit()
