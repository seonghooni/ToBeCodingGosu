N = int(input())

village = []

total_sum = 0

for _ in range(N):
    index, people = map(int, input().split())
    village.append((index, people))
    total_sum += people

village.sort(key=lambda x: x[0])

partial_sum = 0

for i in range(N):
    partial_sum += village[i][1]
    if partial_sum >= total_sum/2:
        print(village[i][0])
        break
