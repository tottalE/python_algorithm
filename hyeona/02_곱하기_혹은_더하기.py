data = list(map(int,input()))

answer = data[0]

for i in range(1,len(data)):
  if(answer == 0 or data[i] == 0 or answer == 1 or data[i] == 1):
    answer += data[i]
  else:
    answer *= data[i]

print(answer)
