class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in nums:
            #when two numbers are different
            if num != (target - num) and (target - num) in nums:
                return [nums.index(num), nums.index(target - num)]
            #when two numbers are same 
            elif nums.count(target - num) > 1:
                return [nums.index(num), nums.index(target - num, nums.index(num)+1)]
