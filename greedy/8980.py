town, max_box = map(int, input().split())
box_num = int(input())
box_info = []
result = 0
for _ in range(box_num):
    box_info.append(list(map(int, input().split())))

box_info.sort(key=lambda x: (x[1], -x[0]))

result += box_info[0][2]
for i in range(1, box_num): # 1, 2, ..., box_num
    box_src, box_dst, box_size = box_info[i]

    before_sum = 0 # 해당 배송을 진행하기 전, 기존에 있던 배송 무게를 계산하기 위함
    for j in range(i): # 0, 1, ..., box_num-1
        if box_src < box_info[j][1]:
            before_sum += box_info[j][2]

    if before_sum >= max_box: # 이미 최대 수하량 이상인 경우 패스
        box_info[i][2] = 0
        continue
    else:
        box_info[i][2] = min(box_info[i][2], max_box - before_sum)
        result += box_info[i][2]

print(result)

