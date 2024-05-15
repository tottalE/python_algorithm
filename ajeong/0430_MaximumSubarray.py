class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub = nums[0]
        curSum = 0

        for n in nums:
          #이전까지의 합이 음수라면 다음 인덱스부터의 sum을 구하는 것이 효율적
          if curSum < 0:
            curSum = 0
          curSum += n
          maxSub = max(maxSub, curSum)
        return maxSub
