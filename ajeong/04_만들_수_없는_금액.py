from itertools import combinations

N = int(input())

coins = list(map(int, input().split()))

coins.sort()


#조합을 구해야하나...?
#1부터 키워가면서 만들 수 없으면 그냥 종료 시키는건 너무 위험..?
