N = int(input())

ropes = list()

for i in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)
max_weight = ropes[0]

for i in range(N):
    max_num = i+1
    while max_num < N and ropes[i] == ropes[max_num]:
        max_num = max_num + 1

    weight = ropes[i] * max_num

    if weight > max_weight:
        max_weight = weight

print(max_weight)