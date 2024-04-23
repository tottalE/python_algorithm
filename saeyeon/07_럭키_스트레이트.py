def solution():
  data= list(map(int, input()))

  sum1, sum2 = 0,0
  
  for i in range(int(len(data)/2)):
    sum1 += data[i]
    sum2 += data[len(data)-1-i]

  if sum1 == sum2 :
    print("LUCKY")
  else:
    print("READY")


solution()