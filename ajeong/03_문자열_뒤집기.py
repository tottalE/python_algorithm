#0과 1의 덩어리 개수가 더 적은 개수가 최소 뒤집기임.

S = input()

#0 덩어리와 1 덩어리의 개수를 저장하기 위한. 
cnt1 = 1 #일단 문자열이 하나라도 들어왔으면 덩어리가 하나 있다는 거
cnt2 = 0

first = S[0]

#바뀌는 횟수를 세봄
for i in range(0, len(S)-1, 1):
    if S[i] != S[i+1]:
        if S[i+1] == first:
            cnt1 += 1
        else:
            cnt2+= 1

#덩어리 중 작은 거 출력
print(min(cnt1, cnt2))