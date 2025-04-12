
# n, m, k = map(int, input().split())
#
# gun_places = [[0] * (n+1)]
# user_places = [[0] * (n+1) for _ in range(n+1)]
# user_info = [[0, 0, 0, 0, 0]]
#
# for _ in range(n):
#     gun_places.append([0] + list(map(int, input().split())))
#
# for i in range(1, m+1):
#     x, y, d, energy = map(int, input().split())
#     user_info.append([x, y, d, energy, 0]) # x, y, direction, energy, gun_power
#     user_places[x][y] = i
#
# dx = [-1, 0, 1, 0] # 북 동 남 서
# dy = [0, 1, 0, -1]
#
# # 범위를 벗어나는지 확인하는 함수
# def is_not_in_range(x, y):
#     if x < 1 or x > n or y < 1 or y > n:
#         return True
#
# def move(user_num, is_first):
#     x = user_info[user_num][0]
#     y = user_info[user_num][1]
#     d = user_info[user_num][2]
#
#     nx = x + dx[d]
#     ny = y + dy[d]
#
#     if is_first and is_not_in_range(nx, ny):
#         if d in (0, 1):
#             d += 2
#         elif d in (2, 3):
#             d -= 2
#         user_info[user_num][2] = d # 범위를 벗어나면 반대방향으로 이동함
#         move(user_num)
#         return
#
#     if is_first and user_places[nx][ny] != 0:
#         already_user_num = user_places[nx][ny]
#         print(f'{already_user_num}와 {user_num}의 맞짱')
#         loser_num = fight_and_who_lose(already_user_num, user_num, nx, ny)
#         print(f'{loser_num}가 졌다!')
#         # 새로 온놈이 졌다? = user_num이 졌다?
#         move(user_num, False)
#         # 원래 있던놈이 졌다? = already_user_num이 졌다?
#         move(already_user_num, False)
#
#     if not is_first and (is_not_in_range(nx, ny) or user_places[nx][ny] != 0):
#         nx =
#
#     user_info[user_num][0] = nx
#     user_info[user_num][1] = ny
#     user_places[x][y] = 0
#     user_places[nx][ny] = user_num
#     get_the_gun(nx, ny, user_num)
#
# # 1. 싸움(진 사람은 총을 버림, 이긴 사람은 총을 주움)
# # 2. 진 사람을 return
# def fight_and_who_lose(user_a, user_b, x, y):
#     a_energy, a_gun_power = user_info[user_a][3], user_info[user_a][4]
#     a_total_power = a_energy + a_gun_power
#
#     b_energy, b_gun_power = user_info[user_b][3], user_info[user_b][4]
#     b_total_power = b_energy + b_gun_power
#
#     winner = 0; loser = 0
#     if a_total_power > b_total_power: # b가 진다면
#         winner = user_a
#         loser = user_b
#         point = a_total_power - b_total_power
#     elif a_total_power < b_total_power:
#         winner = user_b
#         loser = user_a
#     else:
#         if a_energy > b_energy:
#             winner = user_a
#             loser = user_b
#         else:
#             winner = user_b
#             loser = user_a
#
#     gun_places[x][y] = max(gun_places[x][y], user_info[loser][4]) # 더 좋은 총을 땅위에 놓음
#     user_info[loser][4] = 0 # b 무기 몰수
#     temp = min(gun_places[x][y], user_info[winner][4])
#     user_info[winner][4] = max(gun_places[x][y], user_info[winner][4]) # 들고있는 총과 바닥에 있는 총 중에 더 좋은걸 가짐
#     gun_places[x][y] = temp # 더 안좋은 걸 땅에 놓음
#
#     return loser
#
# # 총 줍는 함수
# def get_the_gun(x, y, user_num):
#     new_gun_power = gun_places[x][y]
#     user_gun_power = user_info[user_num][4]
#     if new_gun_power == 0:
#         return
#
#     if new_gun_power > user_gun_power: # 유저가 들고있는 총보다 쎄다면
#         user_info[user_num][4] = new_gun_power # 총을 주움
#         gun_places[x][y] = user_gun_power # 들고 있던 총을 내려놓음
#
# for place in gun_places:
#     print(place)
#
# print("----")
#
# for i in range(1, m+1):
#     move(i)
# for place in gun_places:
#     print(place)
