class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(len(nums)==1):
            return 0 if nums[0] == target else -1
        
        l = 0
        r = len(nums)-1
        mid = (l+r)//2

        while(l<=r):
            if(nums[mid] == target):
                return mid
            if(nums[mid] > target and target >= nums[l]):
                r = mid-1
            elif(nums[mid] > target and nums[l] > nums[mid]):
                r = mid-1
            elif(nums[mid] < nums[l] and target >= nums[l]):
                r = mid-1
            else:
                l = mid+1
            mid = (l+r)//2
        return -1
