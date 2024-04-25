def digit_length(i):
  digit = 0
  while i >= 10:
    i = i // 10
    digit+=1

  return digit+1

def solution(s):
  length_half = len(s)//2
  gap = 1
  start_index = 0
  i = 1 #index of the string to compare
  min_total_length = len(s)
  total_length = 0
  count = 1
  
  while gap <= length_half : #기준 문자열이 전체 문자열 길이의 절반 이상인 경우에는 비교 문자열과 중복이 될 수 없음
      end_index = start_index + gap
      j = i + gap
      str = s[start_index:end_index]
      comp_str = s[i:j]
      if str == comp_str: #기준 문자열과 비교 문자열이 일치하는 경우 카운트
          count += 1
          i += gap
          j = i + gap
      else:
          total_length+=len(str)
          if count != 1:
              total_length+=(digit_length(count)) #중복되는 숫자 개수 추가
          start_index = i
          end_index = j
          i = start_index + gap
          j = i + gap
          count = 1

      if(j > len(s)): #전체 문자열 마지막까지 비교를 마친 경우
        total_length+=len(str)
        total_length+=(len(s)%gap) #남은 문자열이 있는 경우
        if count != 1:
          total_length+=(digit_length(count)) #중복되는 숫자 개수 추가
        if(min_total_length > total_length):
          min_total_length = total_length
        gap += 1
        start_index = 0
        i = start_index+gap
        total_length = 0
  return min_total_length
