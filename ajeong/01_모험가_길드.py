

N = map(int, input())

scary = list(map(int, input().split()))

#공포도 높은 순으로 정렬
scary.sort(reverse=True)

cnt = 0

#모험가가 남아있을 때까지 반복
while scary:
    cnt += 1
    i = scary[0] #남아있는 모험가들 중에 가장 공포도가 높은 사람의 공포도
    del scary[0:i] #가장 공포도가 높은 사람의 공포도만큼 그룹을 지어준다.

print(cnt)

