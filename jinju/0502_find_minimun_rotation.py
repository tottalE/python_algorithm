class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        if nums[0] < nums[-1]:
            return nums[0]

        while r-l>1:
            if nums[r] > nums[r-1] and nums[l] < nums[l+1]:
                l += 1
                r -= 1
            elif nums[r] > nums[r-1]:
                r -= 1
            elif nums[l] < nums[l+1]:
                l += 1
        
        return nums[r]
