class Solution(object):
    def search(self, nums, target):

        n = len

        l=0
        r=len(nums)-1
        m=(l+r)//2

        # 만약 l,m,r 이 target 이면 바로 리턴
      
        if nums[l]==target : return l
        if nums[r]==target: return r
        if nums[m] ==target: return m
        
        while l<m<r:
            if l <0 or r>=len(nums): break

            # 만약 l,m,r 이 target 이면 바로 리턴

            if nums[l]==target : return l
            if nums[r]==target: return r
            if nums[m] ==target: return m
          

            # m이 target 보다 작은 경우는 오른쪽 절반으로 탐색함
            if nums[m]<target:
                l=m+1
                m=(l+r)//2
              # m이 target 보다 큰 경우에는 비교함
            elif nums[m]>target:
              # 만약 l 이 target 보다 작으면 l 과 m 사이에 있다고 생각하고 거기를 탐색
                if nums[l]<target:
                    r=m-1
                    m=(l+r)//2
                #만약 l 이 target 보다 크면 rotation 된 거라고 생각해서 오른쪽 절반을 탐색
                elif nums[l]>target:
                    l=m+1
                    m=(l+r)//2

        if nums[l]==target : return l
        if nums[r]==target: return r
        if nums[m] ==target: return m  
        
        return -1

      # 못 찾아낸 엣지 케이스: rotation 된 게 l과 m 사이이고 target 이 그 값 사이이면 그거를 못 잡아냄


        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
