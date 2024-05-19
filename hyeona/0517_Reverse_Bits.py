class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[:1:-1]
        
        for i in range(32-len(s)):
            s+='0'

        return int(s,2)
