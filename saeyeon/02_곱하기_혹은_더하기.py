data =list(input())
sum = 0

if data[0] =='0':
  sum += int(data[1])
  data.pop(0)
  data.pop(0)
else:
  sum += int(data[0])
  data.pop(0)

 #string 의 첫 줄을 일단 result 에 넣는다. 

 #만약 for loop 에서 reulst 가 0 초과라는 조건을 줫으면 위에서 이렇게 복잡하게 안 써도 왰음 

for i in data:
  if (int(i)>1):
    sum *= int(i)
  else:
    sum += int(i)
    
print(sum)

"""
입력 예시

001
100
051

"""