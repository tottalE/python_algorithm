# get input
n = int(input())
arr = list(map(int, input().split()))

# 내림차순으로 정렬
arr.sort()

# 리스트의 길이와 가장 작은 요소를 변수에 담음
result = 0
cnt = 0

for i in arr:
    cnt += 1
    if cnt >= i: # 큰 경우가 뭐지?
        result += 1
        cnt = 0

print(result)
