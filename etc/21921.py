N, X = map(int, input().split())
statistics = list(map(int, input().split()))

if sum(statistics) == 0:
    print("SAD")
    exit()

current_sum = sum(statistics[0:X])
max_visitors = current_sum
count_duration = 1

for i in range(0, N-X):
    current_sum = current_sum - statistics[i] + statistics[i+X]

    if current_sum > max_visitors:
        max_visitors = current_sum
        count_duration = 1
    elif current_sum == max_visitors:
        count_duration += 1

print(max_visitors)
print(count_duration)