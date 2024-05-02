from math import prod
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 0
        positive_prod = 1
        negative_prod = 1

        if len(nums) == 1:
            return nums[0]
        
        if prod(nums) > 0:
            return prod(nums)
        count_zero = count(nums)
        if count_zero % 2 == 0:
        for num in nums:
            if num < 0:
                negative_prod = negative_prod * num
                positive_prod = 1
                max_prod = max(max_prod, negative_prod)

            elif num > 0:
                positive_prod *= num
                max_prod = max(max_prod, positive_prod)

            else:
                max_prod = max(max_prod, 0)
                positive_prod = 1
                negative_prod = 1

        return max_prod
