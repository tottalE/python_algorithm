class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        pairs = set()
        
        if(len(nums) < 3):
            return answers

        hashmap = {}

        #숫자 개수 카운트
        for num in nums:
            #아직 맵에 없는 원소면 새로 추가
            if num not in hashmap:
                hashmap[num] = 1
            #최대 3개까지만 카운트
            elif hashmap[num] <= 2:
                hashmap[num] += 1
            else:
                continue
        
        new_nums = []

        #해시맵에 카운트한 원소 개수 기반으로 새로운 숫자 배열 생성
        for key in hashmap.keys():
            for i in range(hashmap[key]):
                new_nums.append(key)

        for i in range(len(new_nums)):
            x = new_nums[i]
            hashmap[x]-=1
            for j in range(i+1, len(new_nums)):
                y = new_nums[j]
                hashmap[y]-=1

                #해시맵에 x,y와 더해서 0이되는 원소 값이 있는 경우
                if((-1)*(x+y) in hashmap and hashmap[(-1)*(x+y)] >= 1):
                    pair = [x,y,(-1)*(x+y)]
                    #정렬하기 위해 우선 리스트로 변수 생성
                    pair.sort()
                    #list는 set 안에 안 들어가서 튜플로 변형
                    pairs.add(tuple(pair))

                hashmap[y]+=1
            hashmap[x]+=1

        for pair in pairs:
            #튜플을 다시 리스트로 변형
            answers.append(list(pair))

        return answers
