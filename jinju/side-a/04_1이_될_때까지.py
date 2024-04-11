n, k = map(int, input().split())
cnt = 0

while 1:
    cnt += (n % k)
    n -= (n % k)
    
    if (n < k):
        cnt += -(1 - n)
        break
    
    if (n == k):
        cnt += 1
        break

    n = n // k
    cnt += 1


print(cnt)