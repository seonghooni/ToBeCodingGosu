import sys
input = sys.stdin.readline

N = int(input())
original = list(map(int, input().strip()))
goal = list(map(int, input().strip()))

def turn(switch_count):
    for i in range(1, N-1):
        if temp[i-1] != goal[i-1]:
            switch_count += 1
            temp[i-1] = temp[i-1] ^ 1
            temp[i] = temp[i] ^ 1
            temp[i+1] = temp[i+1] ^ 1

    # 마지막에 대해서 비교 (N-2, N-1)
    if temp[N-2] != goal[N-2]:
        switch_count += 1
        temp[N-2] = temp[N-2] ^ 1
        temp[N-1] = temp[N-1] ^ 1

    if temp[N-1] == goal[N-1]: # 마지막까지 일치하면 성공
        print(switch_count)
        exit()

temp = original.copy()
turn(switch_count=0)

temp = original.copy()
temp[0] = temp[0]^1; temp[1] = temp[1]^1
turn(switch_count=1)

print(-1) # 실패할경우
