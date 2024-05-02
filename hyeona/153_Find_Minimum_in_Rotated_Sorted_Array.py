class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]

        left = 1
        right = len(nums)-1
        mid = (left+right)//2

        while(left < right):
            if(nums[mid-1]>nums[mid]):
                return nums[mid]
            if(nums[mid]>nums[mid+1]):
                return nums[mid+1]
            
            if(nums[mid] > nums[0]):
                left = mid+1
            else:
                right = mid-1
            
            mid = (left+right)//2

        return min(nums[0],nums[mid])
