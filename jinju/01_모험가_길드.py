# get input
n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

length = len(arr)
temp = arr.pop()
cnt = 0

while(length >= temp):
    for _ in range(0, temp):
        temp = arr.pop()
    length = len(arr)
    cnt += 1

print(cnt)