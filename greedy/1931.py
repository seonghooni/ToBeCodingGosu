N = int(input())

time = list()
for i in range(N):
    time.append(list(map(int, input().split())))

time.sort(key=lambda x: (x[1], x[0]))

result = 1 # 최소 1개

next_index = 1
min_start_time = time[0][1]

while next_index < N:
    if time[next_index][0] >= min_start_time:
        min_start_time = time[next_index][1]
        result += 1

    next_index += 1

print(result)