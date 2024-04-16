def solution(food_times, k):
    answer = 0
    
    currentIndex = -1
    
    if sum(food_times)<=k : return currentIndex

    circle = int(k/len(food_times))
    k = k%len(food_times)
    remainList=[]
    
    for i in range(len(food_times)):
        food_times[i] -= circle
        if food_times[i]<0:
            k-=food_times[i]
        else:
            remainList.append(i)
            
    
    while(k>=0):
        currentIndex+=1
        
        if currentIndex > len(food_times)-1:
            currentIndex = 0
            
        if food_times[currentIndex]>0:
            k-=1
            food_times[currentIndex]-=1
            

    answer = currentIndex + 1
    
    return answer
    
    
