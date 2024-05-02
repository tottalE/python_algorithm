class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_unique = list(set(nums))
        if len(nums) == len(num_unique):
            return False
        else:
            return True
        
