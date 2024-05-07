class Solution:
    def getSum(self, a: int, b: int) -> int:
        # add = (a^b)
        # carry = (a&b) << 1

        # while ((add & carry) != 0):
        #     temp = add ^ carry
        #     carry = (add & carry) << 1
        #     add = temp

        #return (add|carry)

        return sum([a,b])
