class Solution(object):
    def maxProfit(self, prices):

        buy=prices[0]
        sell=prices[0]

        #일단 buy 와 sell 을 정해놓고 시작한다.
         
        answerList=[]
        
        for i in prices:
            if i<buy:  #더 싼 가격이 나오면 그걸로 buy를 바꿔준다.
                buy=i
                sell=i #대신 sell은 buy보다 높아야 하니까 같이 바꿔준다.
            elif i>sell: #만약 더 비싼 가격이 나오면 그걸로 sell을 바꿔준다.
                sell=i
                answerList.append(sell-buy)

        if answerList : return max(answerList) #만약 answerList가 비어있지 않다면 그 중에서 가장 큰 값을 반환한다.
        else: return 0 #비어있다면 0을 반환한다.
        
        # print(prices1,prices2,prices3)
        # print([sell2-buy,sell-buy2, sell3-buy3])

        """
        :type prices: List[int]
        :rtype: int
        """
        