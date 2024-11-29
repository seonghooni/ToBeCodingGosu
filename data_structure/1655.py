import heapq
import sys

# 시간이 너무 오래 걸림 (비교 후 push 및 pop을 각각 진행하기 때문)

# N = int(input())
# left_heap = [] # 최대힙
# right_heap = [] # 최소힙
#
# first_input = int(input())
# heapq.heappush(left_heap, -first_input)
# print(first_input)
# for _ in range(N-1):
#     input_value = int(input())
#     if len(left_heap) == len(right_heap):
#         right_min = right_heap[0]
#         if input_value > right_min: # right_heap의 최소값보다 현재값이 크다면
#             heapq.heappush(left_heap, heapq.heappop(right_heap))
#             heapq.heappush(right_heap, input_value)
#         else:
#             heapq.heappush(left_heap, -input_value)
#     else:
#         left_max = -left_heap[0]
#         if input_value < left_max:
#             heapq.heappush(right_heap, -heapq.heappop(left_heap))
#             heapq.heappush(left_heap, -input_value)
#         else:
#             heapq.heappush(right_heap, input_value)
#
#     print(-left_heap[0])


N = int(sys.stdin.readline()) # input()을 사용하면 시간초과가 발생함
left_heap = []
right_heap = []

for i in range(N):

    input_value = int(sys.stdin.readline()) # input()을 사용하면 시간초과가 발생함

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -input_value)
    else:
        heapq.heappush(right_heap, input_value)

    if right_heap and -left_heap[0] > right_heap[0]:
        left_max = -heapq.heappop(left_heap)
        right_min = heapq.heappop(right_heap)
        heapq.heappush(right_heap, left_max)
        heapq.heappush(left_heap, -right_min)

    print(-left_heap[0])