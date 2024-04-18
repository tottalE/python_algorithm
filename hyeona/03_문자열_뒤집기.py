s = input()

zero_data = list(s.split('0'))
one_data = list(s.split('1'))
data0 = list(filter(None,zero_data)) #빈 문자열 제거
data1 = list(filter(None,one_data))

print(min(len(data0),len(data1)))
