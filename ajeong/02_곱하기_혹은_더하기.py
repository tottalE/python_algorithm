S = input()

new_S = ""

#0이 포함되어 있는 지 없는지를 나눔

#0이 없으면 무조건 곱하는 게 큰 수
# if "0" not in S:
#     answer = 1
#     for i in range(0, len(S), 1):
#         answer *= int(S[i])

#0이 중간에 있으면 
# else:
answer = int(S[0])
for i in range(1, len(S), 1):
    #이전의 값이 0이거나 추가해야하는 숫자가 0또는1이면 더하기 연산해야 함
    if (answer== 0 or answer==1) or (int(S[i])==0 or int(S[i])==1):
        answer += int(S[i])
    else:
        answer *= int(S[i])

print(answer)