data = list(map(int,input()))

answer = data[0]

for i in range(1,len(data)):
  if(answer == 0 or data[i] == 0):
    answer += data[i]
  else:
    answer *= data[i]

print(answer)
