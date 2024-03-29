# 추에 대한 값을 받고 리스트에 넣음
# 1. 자신을 추가
# 2. 추로 만들수 있는 무게값들이 존재할 경우, 하나씩 빼서 추가함
    # N = int(input())
    # available_set = set()
    #
    # chu_list = list(map(int, input().split()))
    #
    # for chu in chu_list:
    #     new_available_set = set()
    #     for already_available in available_set:
    #         new_available_set.add(already_available + chu)
    #
    #     available_set.update(new_available_set)
    #     available_set.add(chu)
    #
    # available_list = list(available_set)
    #
    # for i in range(len(available_list)):
    #     if i == len(available_list) - 1 or available_list[i + 1] != available_list[i] + 1:
    #         result = available_list[i] + 1
    #         break
    #
    # print(result)
# ---- 위와 같은 방법으로 문제를 풀 경우 '메모리 초과'가 뜸
# 도저히 모르겠어서 검색을 하여 다음과 같은 방식으로 풀 수 있다는 걸 배움
# 추를 1번째부터 x번째까지 작은순서부터 차례로 검토한다고 하자.
# [1,1,2,3,7] 라고 한다면 가능한 무게를 한번 추가해보자
# 1부터 살핀다면 [1]
# 그다음 1이 또 추가되므로 [1,2], 그다음 2가 추가되므로 [1,2,3], 그다음 3이 추가되므로 [1,2,3,4,5,6]
# 만약 7이 추가된다면, [1,2,3,4,5,6, 8,9,10,11,12,13]이 된다.
# 7이 아니라 6이었다면?... [1,2,3,4,5,6,7,8,9,10,11,12]가 된다.
# 즉, 새로운 무게추 X와 지금까지 측정할 수 있는 무게의 최대값인 K를 비교해 구할 수 있다.
# 만약 지금까지 측정할 수 있는 무게의 최댓값이 20이라면, 무게추의 무게가 22 이상일 경우 빈 공간이 생긴다는 것이다.

N = int(input())

chu_list = list(map(int, input().split()))

chu_list.sort()

max_sum = 0

while chu_list:
    target = chu_list.pop(0)
    if target > max_sum + 1:
        print(max_sum + 1)
        exit(0)
    else:
        max_sum += target

print(max_sum+1)