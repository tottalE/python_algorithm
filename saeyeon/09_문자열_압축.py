def solution(s):
    
    shortenList=[]
    shortenList.append(len(s)) #문자열이 1개일 때 대비
    
    step=range(1,int(len(s)/2)+1) #자르는 단위는 1개부터 len(data)/2개까지 가능하다...
    
    for i in step:
        sum = len(s)
        current = ''
        last = ''
        first = True
        cnt=0
        
        for j in range(0,len(s),i):
            current = s[j:j+i]

            if current == last:  #현재거가 마지막거랑 같으면 sum 에서 그 생략된 단위를 없앰..
                sum -= i
                cnt+=1
                if first:  #그게 첫번째 거면 다시 +=1 해줌
                    sum +=1
                    first = False
            else:               
                first = True
                if cnt>9:  #만약 반복이 10번 이상이면 단위가 하나 더 생기니까 sum에 1을 더해줌
                    sum+=1
                elif cnt>99:
                    sum+=2
                elif cnt>999:
                    sum+=3
                    
                cnt=0
                
            last = current
            
                
        shortenList.append(sum)
        
    answer = min(shortenList)
            
    
    
    return answer