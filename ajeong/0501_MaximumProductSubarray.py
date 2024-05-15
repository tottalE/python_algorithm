class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        #곱셈이니까 초기화는 1로
        #이전의 음수값이 다음의 음수와 만나서 양수 최댓값이 되기때문에 음수도 같이 저장 해놓음.
        curMin, curMax = 1, 1 

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            tmp = curMax * n
            #이전 max와 곱한 수, 이건 min과 곱한 수, n 중에 큰 값과 작은 값을 계속 저장해서 res를 업데이트
            curMax = max(tep, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)
        return res
