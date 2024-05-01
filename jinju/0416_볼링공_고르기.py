n, m = map(int, input().split())
list_int = list(map(int, input().split()))
ball_cnt = []

cnt = 1
total = 0
list_int.sort()
temp = list_int[0]

# 1 2 2 3 3 -> 1 2, 1 2, 1 3, 1 3, 2 3, 2 3, 2 3, 2 3
for i in range(1, len(list_int)):
    if list_int[i] == temp:
        cnt += 1
    else:
        ball_cnt.append(cnt)
        cnt = 1
    temp = list_int[i]

ball_cnt.append(cnt)

for ball in ball_cnt:
    n -= ball
    total += n * ball

print(total)
