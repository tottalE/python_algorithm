class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [0 for _ in range(len(nums))]
        right_product = [0 for _ in range(len(nums))]

        product = 1

        for i in range(len(nums)):
            left_product[i] = product
            product *= nums[i]

        product = 1
        for i in range(len(nums)-1,-1,-1):
            right_product[i] = product
            product *= nums[i]
        
        answer = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            answer[i] = left_product[i]*right_product[i]

        return answer
