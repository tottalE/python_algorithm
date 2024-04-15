data = list(input())

# 0001100

countList = []
count=0
last = data[0]

#연속되는 거 기준으로 count를 셈
#예를 들어 1110011 이면 [3,2,2]


for i in range(len(data)): 
  if data[i] == last:
    count +=1
    last = data[i]

  else:
    countList.append(count)
    count =1
    last = data[i]

countList.append(count)

#[3,2,2] 가 개수가 홀수이면 n-1/2 짝수이면 /2 하면 됨

if (len(countList)%2==0):
  print(int(len(countList)/2))
  
else:
  print(int((len(countList)-1)/2))

# 테스트 케이스

#백준 기준 정답