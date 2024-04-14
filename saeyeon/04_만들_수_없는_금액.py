n = int(input())
coin = list(map(int, input().split()))

coin.sort()

num = 0
sum = 0
numList = coin

#가장 작은 게 1 이 아니면 무조건 1
if coin[0] != 1:
  print(1)

else:
  #가장 큰 수보다는 작은 경우
  for i in range(len(coin)):
    sum += coin[i]
    if sum not in coin:
      localList = coin[i + 1:len(coin) - 1]

    sum += i
    if (sum not in coin) and (sum + 1 not in coin):
      print(sum + 1)
      exit()

  # 가장 큰 수보다 커야하는 경우
  if (num == len(coin)):
    print(sum + 1, "case3")
"""
5
3 2 1 1 9 = 8
1 1 2 3 9


1 2 4  = 8

1 1 2 2 7 = 

1 2 3 13 = 7

1 3 5 7 = 2

1 2 5 7 = 4 

# 앞에 것을 더한 게 뒤에 없는지를 보면 되나...? 
# 근데 뒤에 있는 것끼리 더해서 맞는 합일 수도 있음

그럼 반대로 뒤에서 1개씩 빼보기...? 

1 1 2 3 9
2 3 4 10 4 11 10 6 14 

--------
1개로 만들 수 있는 수
2개로 만들 수 있는 수 
3개로 만들 수 있는 수




4 + 3 + 2 1 



3
3 5 7 = 1

1 2 3 = 4
1 1 3 = 4

2 2 3 = 1
1 1 5 = 3

1 2 5 = 4

1 1 7 = 3
1 3 7 = 2
1 2 4 7 =5
1 2 3 3 5
1 1 2 5 = 4

1 1 3 4 = 가장 큰 수보다


1 2 3 4 5 = 








"""
