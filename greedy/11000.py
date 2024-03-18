import heapq

n = int(input())
lectures = []
lecture_rooms = []

for _ in range(n):
    lectures.append(list(map(int, input().split())))

lectures.sort()

heapq.heappush(lecture_rooms, lectures[0][1])
for i in range(1, n):
    end_time_of_lecture = heapq.heappop(lecture_rooms)
    if lectures[i][0] < end_time_of_lecture:
        heapq.heappush(lecture_rooms, end_time_of_lecture)
        heapq.heappush(lecture_rooms, lectures[i][1])
    else:
        heapq.heappush(lecture_rooms, lectures[i][1])

print(len(lecture_rooms))