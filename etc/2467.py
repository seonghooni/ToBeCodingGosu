import sys
input = sys.stdin.readline

N = int(input())
squids = list(map(int, input().split()))

left_idx = 0
right_idx = N-1

min_abs = abs(squids[left_idx] + squids[right_idx])

answer_left = 0
answer_right = N-1

if squids[0] < 0 and squids[N-1] < 0: # 음수만 있을 때
    print(squids[N-2], squids[N-1])
elif squids[0] > 0 and squids[N-1] > 0: # 양수만 있을 때
    print(squids[0], squids[1])
else:
    while left_idx < right_idx:
        temp_sum = squids[left_idx]+squids[right_idx]
        if abs(temp_sum) < min_abs:
            answer_left = left_idx
            answer_right = right_idx
            min_abs = abs(temp_sum)

            if min_abs == 0:
                break

        if temp_sum < 0:
            left_idx += 1
        else:
            right_idx -= 1

    print(squids[answer_left], squids[answer_right])

