class Solution:
    def countBits(self, n: int) -> List[int]:
        answers = []
        for i in range(n+1):
            answers.append(bin(i).count("1"))
        return answers
