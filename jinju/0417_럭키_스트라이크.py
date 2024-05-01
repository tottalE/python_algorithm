lucky = "LUCKY"
ready = "READY"
temp = 0

n = input()
length = len(n) // 2

for i in range(length):
    temp += int(n[i])
    
    
for i in range(length, len(n)):
    temp -= int(n[i])
    
if temp == 0:
    print(lucky)
else:
    print(ready)
