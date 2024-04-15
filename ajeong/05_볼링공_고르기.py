#A가 고른 볼링공의 무게를 제외하고 남아있는 선택지 개수를 구하면 됨
N, M = map(int, input().split())

w = list(map(int, input().split()))

cnt = 0


for i in range(0, N-1, 1):
    #B의 선택지를 choice 리스트로 만듦
    choice = w[i+1:]
    #A가 선택한 볼링공 w[i]와 같은 무게인 볼링공을 B의 선택지에서 지워줌
    if w[i] in choice:
        choice.remove(w[i])
    cnt += len(choice)

print(cnt)