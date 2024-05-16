def search(nums, target):
  l,r = 0, len(nums)-1
   
  while l<=r:
     mid=(l+r)//2
     if target == nums[mid]:
       return mid

    # left soted portion
     if nums[l] <= nums[mid]:
      if target > nums[mid] or target < nums[l]:
        l = mid + 1

      else:
        r = mid -1

    # right sorted portion
     else:
      if target < nums[mid] or target > nums[r]:
        r= mid -1
      else:
        r = mid + 1

  return -1

print(search([4,5,6,7,0,1,2],0))
