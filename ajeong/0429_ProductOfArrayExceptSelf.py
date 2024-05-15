class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []

        front = 1
        back = 1

        for i in range(len(nums)):
            front = 1
            back = 1
            for j in nums[0:i]:
                front *= j
            for j in nums[i+1:]:
                back *= j
            answer.append(front * back)
        
        return answer


        
