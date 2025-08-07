def maxProfit(self, prices):

        '''

        Initialize left and right pointers
        
        if R - L < 0:
            move both pointers 1 position
        else:
            while right < len(prices):
                move right by 1

        
    
        '''

        left, right = 0, 1

        maxprofit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
            else:
                left = right
            right += 1
        return maxprofit