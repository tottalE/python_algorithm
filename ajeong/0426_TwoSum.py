class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for i in range(0, len(nums)-1, 1):
            for j in range(i+1, len(nums), 1):
                if target == nums[i]+nums[j]:
                    answer.append(i)
                    answer.append(j)
                    break
            
        return answer
        
