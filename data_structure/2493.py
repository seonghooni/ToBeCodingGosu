from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

my_stack = [(1, towers[0])] # (idx, 탑의 높이)
answer = [0] * N

for i in range(1, N): # 어차피 1번 타워는 답이 0이므로 2번째부터 시작

    while my_stack:
        top_idx, top_height = my_stack[-1]

        if top_height > towers[i]:
            my_stack.append((i+1, towers[i])) # 만약 비교하고 있는 탑의 높이가 크다면 스택에 현재 탑도 넣음
            answer[i] = top_idx
            break
        else:
            my_stack.pop() # 만약 비교하고 있는 탑의 높이가 작다면, 현재 탑만 사용될 것임

    if not my_stack: # 만약 끝까지 자신보다 큰 탑이 없을 경우
        my_stack.append((i+1, towers[i]))
        answer[i] = 0


print(*answer, end=" ")

