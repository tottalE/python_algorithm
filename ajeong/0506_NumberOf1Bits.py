class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt, r = 0, 0

        while n > 0:
            r = n % 2
            if r == 1:
                cnt += 1
            n = n // 2

            if n == 1:
                cnt += 1
                break

        return cnt
