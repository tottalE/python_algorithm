class Solution(object):
    def hammingWeight(self, n):

        arr = []

        while n >1:
            if n%2 ==1 : arr.append(1)
            else: arr.append(0)
            n=n//2

        if n == 0 : arr.append(0)
        else: arr.append(1)

        return arr.count(1)

            

        """
        :type n: int
        :rtype: int
        """
        
