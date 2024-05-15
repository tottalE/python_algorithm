class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        
        for i in range(n+1):
            cnt, r = 0, 0
            while i > 0:
                r = i % 2
                if r == 1:
                    cnt += 1
                i = i // 2
                if i == 1:
                    cnt += 1
                    break
            res.append(cnt)

        return res
