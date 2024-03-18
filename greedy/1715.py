import heapq

n = int(input())

if n == 1:
    print(0)
    exit(0)

decks = []
for _ in range(n):
    heapq.heappush(decks, int(input()))

answer = 0

while len(decks) > 1:
     a = heapq.heappop(decks)
     b = heapq.heappop(decks)
     answer += (a + b)

     heapq.heappush(decks, a+b)

print(answer)
