from itertools import combinations

n,m = map(int, input().split())

data = list(map(int, input().split()))
combs = list(combinations(data,2))

for x,y in combs:
  if(x == y):
    combs.remove((x,y))

print(len(combs))
