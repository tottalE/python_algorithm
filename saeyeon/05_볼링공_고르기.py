n, m = map(int, input().split())
ballList = list(map(int, input().split()))
ballList.sort()

# 1 2 2 3 3 / 1 2 2 ( 4+ 2*2 )
# 무게가 1인 거 골랐을 때 1의 개수 * 1이 아닌 거 개수
# 무게가 2인 걸 골랐을 때 2의 개수 * (나머지에서 2가 아닌 거 개수)
# 이렇게 더함!!

sum = 0
ballNum = []
remain = len(ballList)

for i in range(1, m + 1):
  sum += ballList.count(i) * (remain - ballList.count(i))
  remain -= ballList.count(i)

print(sum)
