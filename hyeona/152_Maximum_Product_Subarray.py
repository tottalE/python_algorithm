class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        dp_abs = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp_abs[0] = abs(nums[0])

        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]*nums[i],nums[i])
            dp_abs[i] = max(dp_abs[i-1]*abs(nums[i]),nums[i])

        max_product = 0
        
        for i in range(len(nums)):
            if(dp[i] == dp_abs[i]):
                max_product = max(max_product,dp[i])
        
        return max_product
