class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_dic = {}
        for num in nums:
            if duplicate_dic.get(num):
                return True
            else:
                duplicate_dic[num] = 1
        
        return False
