from math import prod

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        if 0 in nums:
            for i in range(len(nums)):
                print(nums)
                temp = nums.copy()
                temp.pop(i)
                answer.append(prod(temp))
        else:
            total_prod = prod(nums)
            answer = []
            for num in nums:
                answer.append(total_prod//num)

        return answer
