class Solution(object):
    def maxProduct(self, nums):

        currSum = 1
        maxSum = 0

        for i in range(len(nums)):
            if nums[i] > 0 and currSum == 0:
                currSum = 1
                
            currSum *= nums[i]
            if currSum < nums[i]:
                currSum = nums[i]
            else:
                maxSum = currSum

        return maxSum

        """
        :type nums: List[int]
        :rtype: int
        """
        
