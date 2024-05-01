class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        
        for i in range(len(nums)):
            temp = nums[i]
            if idxs.get(temp) == None:
                idxs[temp] = i
            else:
                if (temp * 2) == target:
                    return [idxs[temp], i]
            
        
        for num, idx in idxs.items():
            temp = target - num
            if idxs.get(temp):
                if temp == num:
                    continue
                return [idx, idxs[temp]]

        return []  
                
