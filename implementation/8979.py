N, K = map(int, input().split())

countries = []
for _ in range(N):
    country = list(map(int, input().split()))

    if country[0] == K:
        gold = country[1]
        silver = country[2]
        bronze = country[3]
    else:
        countries.append(country)

rank = 1

for target, target_gold, target_silver, target_bronze  in countries:
    if target_gold > gold:
        rank += 1
    elif target_gold == gold:
        if target_silver > silver:
            rank += 1
        elif target_silver == silver:
            if target_bronze > bronze:
                rank += 1
            else:
                continue
        else:
            continue
    else:
        continue

print(rank)