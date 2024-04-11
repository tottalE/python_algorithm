# m: 몇번 더하는지, k: 연속해서 더할 수있는 횟ㅅ, n: 자연수의 개수
# k <= m

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0

arr.sort(reverse=True)
print(arr)
while (m-k) >= 0:
    if (m-k) > 0:
        for _ in range(0,k):
            sum += arr[0]
        m -= k
        sum += arr[1]
        m -= 1

    elif (m-k) == 0:
        for _ in range(0,k):
            sum += arr[0]
        m = -1

    else:
        for _ in range(0, m):
            sum += arr[0]
        m = -1

print(sum)