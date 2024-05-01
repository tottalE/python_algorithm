arr = list(input())
arr_int = list(map(int, arr))
result = arr_int[0]

for i in range(1, len(arr)):
    if result > 1 and arr_int[i] > 1:
        result *= arr_int[i]
    else:
        result += arr_int[i]

print(result)
