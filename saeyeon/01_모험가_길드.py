n = map(int, input())  #모험가의 수 입력받음
exp = list(map(int, input().split()))  #모험가 리스트 입력 받음

exp.sort()  #공포도 낮은 순으로 정렬 3 2 2 2 1

order = 0
count = 0

while (order <= len(exp) - 1):
  if (len(exp) - (order) - exp[order] >= 0):  #현재 공포도가 남은 인원 수보다 적다면
    order += exp[order]  #같이 떠나는 사람 차례를 지나서 다음 사람 차례
    count += 1

  else:  #현재 공포도가 남은 인원 수보다 크다면:
    order += 1  #다음 인원으로 감

print(count)


#반례
# 1 1 2 2 5

n = map(int, input())  #모험가의 수 입력받음
exp = list(map(int, input().split()))  #모험가 리스트 입력 받음

exp.sort()  #공포도 낮은 순으로 정렬 3 2 2 2 1

order = 0
count = 0

while (order <= len(exp) - 1):
  if exp[order] == 1:  #1이면 자동으로 추가
    count += 1
    order += 1

  elif (len(exp) - (order) - exp[order] >= 0):  #현재 공포도가 남은 인원 수보다 적다면
    if exp[order] == exp[order + 1]:
      order += exp[order]  #같이 떠나는 사람 차례를 지나서 다음 사람 차례
      count += 1
    else:
      order += 1

  else:  #현재 공포도가 남은 인원 수보다 크다면:
    order += 1  #다음 인원으로 감

print(count)

#입력 예시
# 1 1 2 2 5
# 4 1 1 1 1
# 4 4 4 4
# 1 2 3
# 1 1 2 2 3
# 2 3
