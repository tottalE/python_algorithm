n, m = map(int, input().split())
arr = []
for _ in range(0,n):
    arr.append(list(map(int, input().split())))

sorted_list = [sorted(x)[0] for x in arr]

print(max(sorted_list))

# ----------------------------------------------------------------

n, m = map(int, input().split())
arr = []

for _ in range(0,n):
    arr.append(min(list(map(int, input().split()))))

print(max(arr))