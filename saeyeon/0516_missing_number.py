class Solution(object):
    def missingNumber(self, nums):

        full_nums=0

        for i in range(len(nums)+1):
            full_nums += i

        sum_nums = sum(nums)

        return full_nums-sum_nums

        """
        :type nums: List[int]
        :rtype: int
        """
        
