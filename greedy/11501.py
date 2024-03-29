T = int(input())

for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))

    benefit = 0

    max_price = days[len(days)-1]
    for i in range(len(days)-1, -1, -1):
        if days[i] >= max_price:
            max_price = days[i]
        else:
            benefit += max_price - days[i]

    print(benefit)