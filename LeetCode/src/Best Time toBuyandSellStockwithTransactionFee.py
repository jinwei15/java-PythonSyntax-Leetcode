class Solution:
    def maxProfit(self, stock: 'List[int]', fee: 'int') -> 'int':
        cash, hold = 0, stock[0]
        for i in range(1, len(stock)):
            cash = max(cash, stock[i] - hold - fee)
            hold = min(hold, stock[i] - cash)
        return cash
