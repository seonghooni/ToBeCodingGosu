# 못풀음

# n, m, h, k = map(int, input().split())
#
# people_info = []
# tree_info = []
# for _ in range(m):
#     x, y, direction = map(int, input().split())
#     people_info.append([x-1, y-1, direction])
#
# for _ in range(h):
#     x, y = map(int, input().split())
#     tree_info.append((x-1,y-1))
#
# # 증가할수록 시계방향(북, 동, 남, 서)
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# # -------- 술래 이동 관련 초기 값 -------- #
# is_clockwise = True
# move_dir = 0 # 0,1,2,3 임 현재는 시작이므로 0
# move_count = 0 # 현재 방향으로 이동한 횟수
# # move_count = move_limit일 경우 change_count 증가
# # 방향을 바꾼 횟수(change_count == 2가 되면 방향을 바꾸지만,
# # move_limit == (n-1)일 경우에는 change_count ==3 이어야 방향을 바꿈
# move_limit = 1
# change_count = 0
# master_x, master_y = n//2, n//2 # 술래 위치
#
# def master_move():
#     global master_x, master_y, move_dir, move_count, move_limit, change_count, is_clockwise
#     master_x = master_x + dx[move_dir]
#     master_y = master_y + dy[move_dir]
#     move_count += 1
#
#     if move_count == move_limit: # 현재 방향으로 충분히 많이 이동했다면
#         change_count += 1
#
#         if is_clockwise: # 시계방향
#             move_dir = (move_dir + 1) % 4 # 방향 전환 (1씩 증가)
#             if move_limit != n-1: # 최대 이동가능거리가 n-1이 아닐 경우,
#                 if change_count == 2: # 방향전환을 2번 했다면
#                     move_limit += 1# 최대 이동가능거리 1 증가
#                     change_count = 0
#             else:
#                 if master_x == 0 and master_y == 0: # 최종 목적지일 경우
#                     move_dir = 2
#                     change_count = 0
#                     is_clockwise = False
#
#         else:
#             move_dir = (move_dir - 1) % 4 # 방향 전환 (1씩 감소)
#             if move_limit != n-1:
#                 if master_x == n//2 and master_y == n//2:
#                     move_dir = 0
#                     change_count = 0
#                     is_clockwise = True
#                 elif change_count == 2:
#                     move_limit -= 1
#                     change_count = 0
#             else:
#                 if change_count == 3:
#                     move_limit -= 1
#                     change_count = 0
#
#         move_count = 0  # 이동한 횟수 0으로 초기화(방향을 바꾸기 때문)
#
# def people_move():
#     for person_info in people_info:
#
#         x, y, d = person_info
#
#         if abs(x-master_x) + abs(y-master_y) > 3:
#             continue
#         # print(f'{x}, {y} ->', end="")
#         nx = x + dx[d]
#         ny = y + dy[d]
#
#         if 0 <= nx < n and 0 <= ny < n: # 격자 내부
#             if nx == master_x and ny == master_y:
#                 continue
#             else:
#                 person_info[0] = nx
#                 person_info[1] = ny
#         else:                           # 격자 외부
#             if d == 0 or d == 1:
#                 d += 2
#                 person_info[2] = d
#             else:
#                 d -= 2
#                 person_info[2] = d
#             nx = x + dx[d]
#             ny = y + dy[d]
#
#             if nx == master_x and ny == master_y:
#                 continue
#             else:
#                 person_info[0] = nx
#                 person_info[1] = ny
#         # print(f'{person_info[0]}, {person_info[1]}')
#
#
# turn = 1
# score = 0
#
# while turn <= k:
#
#     people_move()
#     master_move()
#
#     master_sight = []
#
#     for i in range(3):
#         x = master_x + dx[move_dir] * i
#         y = master_y + dy[move_dir] * i
#         master_sight.append((x,y))
#
#     for sight in master_sight:
#         for person_info in people_info:
#             person_x, person_y, d = person_info
#             x, y = sight
#
#             if person_x == x and person_y == y:
#                 for tree in tree_info:
#                     if tree[0] == person_x and tree[1] == person_y:
#                         continue
#                     else:
#                         people_info_temp = [people for people in people_info if not (people[0] == x and people[1] == y)]
#                         count = len(people_info) - len(people_info_temp)
#                         score += turn * count
#                         break
#     people_info = people_info_temp[:]
#     turn += 1
#
# print(score)