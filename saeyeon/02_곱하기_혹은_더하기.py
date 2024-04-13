data =list(input())
sum = 0

if data[0] =='0':
  sum += int(data[1])
  data.pop(0)
  data.pop(0)
else:
  sum += int(data[0])
  data.pop(0)

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