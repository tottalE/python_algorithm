food_times = list(map(int, input().split()))

k = int(input())

cnt = 0

#k를 1씩 줄여가면서 원소값을 1씩 줄임. 어느 인덱스에서 방송이 끊겼는지 cnt에 저장
while k>0:
    for i in range(len(food_times)):
        if food_times[i]>0:
            food_times[i] -= 1
            cnt = i
            k -= 1
            if k == 0:
                break
        else:
            continue

#cnt의 다음 원소가 0인지 아닌지 확인하면서 양수인 값이 있으면 바로 멈춤.
for i in range(1, len(food_times)+1, 1):
    next_idx = (cnt+i)%len(food_times)
    if(food_times[next_idx]>0):
        next_idx = next_idx+1
        break
    else:
        next_idx = -1

print(next_idx)