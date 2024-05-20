class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums)+1)]
        dp[0] = 0

        for i in range(1,len(nums)):
            j = i-1

            #앞선 원소들 중에 현재 원소보다 작고
            #longest increasing subsequence를 가지는 원소 탐색
            max_v = 0
            max_index = 0
            while(j > 0):
                if(nums[j] < nums[i]) and max_v <= dp[j]:
                    max_v = dp[j]
                    max_index = j
                j-=1
            
            if(nums[max_index] < nums[i]):
                dp[i] = max_v+1

        return max(dp)+1
            
