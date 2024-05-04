class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        hashmap = {}
        answer=set()

        for num in nums:
          # [-1,0,1]과 같은 경우
            if -num in hashmap and 0 in hashmap and num !=0:
                answer.add((abs(num),-abs(num),0))
              
          #[-1,-1,2]와 같은 경우에서 2의 시점
            if (-num//2) in hashmap and hashmap[-num//2] >=2 and num>1:
                answer.add((num,-num//2,-num//2))
              
          #[-1,-1,2] 와 같은 경우에서 -1 의 시점
            if -num*2 in hashmap and num in hashmap and num!= 0:
                answer.add((num,num,-num*2))

          #[0,0,0] 과 같은 시점
            if num == 0 and num in hashmap and hashmap[num]>=2:
                answer.add((0,0,0))

          #못 걸러낸 엣지 케이스: [-3,2,1]와 같은 경우...
            if num in hashmap: hashmap[num] +=1
            
            else: hashmap[num]=1

        return answer
