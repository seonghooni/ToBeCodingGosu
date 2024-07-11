# 시간초과로 틀렸던 문제
# 블로그 글을 참고하여 이해했음 https://blog.naver.com/PostView.naver?blogId=mugamta&logNo=223313727817&noTrackingCode=true
# 1. (데드라인 asc, 컵라면 desc)로 정렬하는 것이 중요
# 2. time=1부터 데드라인과 비교하되, 만약 데드라인이 걸리지 않는다면 추가, 걸린다면 우선순위큐의 맨 첫번째와 컵라면을 비교하여, 더 큰걸 넣는것이 중요
#    ex) (2,3), (2,1), (3,6), (3,5), (3,4) 라면 데드라인이 길더라도 (3,6), (3,5), (3,4)을 쓰는 것이 옳기 때문

import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
li.sort(key=lambda x: (x[0], -x[1]))

pq = []  # 선택할 문제
time = 1  # 시간
for i in range(N):
    deadline, cup_ramen = li[i]

    # 현재 데이터가 타임라인에 걸리지 않는다면
    if time <= deadline:
        heappush(pq, cup_ramen)  # 문제를 해결하고 컵라면을 받아감
        time += 1  # 시간 증가

    # 현재 데이터가 데드라인에 걸리지만,
    # 힙의 최상단 값인 가장 작은 컵라면보다 현재 컵라면 개수가 더 많다면
    elif pq[0] < cup_ramen:
        heappop(pq)  # 해당 문제를 푸는 대신
        heappush(pq, cup_ramen)  # 이 문제를 푸는 것이 이득
        # 푼 문제 수는 그대로이므로 시간은 그대로 둠

res = sum(pq)
print(res)

# import heapq
#
# num = int(input())
#
# priority_queue = []
# result = 0
# already_queue = dict()
#
# for _ in range(num):
#     tup = list(map(int, input().split()))
#     heapq.heappush(priority_queue, (-tup[1], tup[0]))
#
# for i in range(num):
#     head_tup = heapq.heappop(priority_queue)
#     cup, dead_line = head_tup
#
#     while dead_line > 0:
#         if dead_line in already_queue:
#             dead_line -= 1
#         else:
#             already_queue[dead_line] = 1
#             result += cup
#             break
#
# print(-result)


