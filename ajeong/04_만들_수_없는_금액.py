N = int(input())

coins = list(map(int, input().split()))

coins.sort()

cost = []

#조합을 구해야하나...?
for i in coins:
    cost.append(i)

#2개로 만들 수 있는 금액
for i in range(N-1):
    for j in (i+1, N-1, 1):
        temp = coins[i]+coins[j]
        if temp not in cost:
            cost.append(temp)

print(cost)

cost.sort()

answer = 0
for i in range(1, len(cost)+1, 1):
    if i not in cost:
        answer = i
        break

if answer == 0:
    answer = cost[-1]+1
    
print(answer)

#2개로 만들 수 있는 금액
#조합을 다 구하지 않고도 작은 값이
