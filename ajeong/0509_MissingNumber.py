class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = 0

        for i in nums:
            if first not in nums:
                break
            first += 1

        return first
