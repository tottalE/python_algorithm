n = int(input())

data = list(map(int, input().split()))

data.sort()

selected = []
answer = 0
idx = 0
curr = data[idx]

while True:
  if idx == n:
    break
  
  if len(selected) == (data[idx]-1):
    answer += 1
    idx += 1
    selected = []
  else:
    selected.append(data[idx])
    idx += 1
  

print(answer)
