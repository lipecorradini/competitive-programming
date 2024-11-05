import bisect

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
           # itera por cada par de tras pra frente
           # se xi-1 < xi
           # entao xi-1 nao pode ser final
           # inserimos ordenado xi em finais
           # diff = finais[-1] - (xi-1)
            finais = []
            best_diff = 0
            for i in range(len(prices) - 1, 0, -1):     
                if prices[i-1] < prices[i]:
                    bisect.insort(finais, prices[i])
                    if finais[-1] - prices[i-1] > best_diff: #maior elemento depois - elemento atual
                        best_diff = finais[-1] - prices[i-1]
            
            return best_diff


# Optimal solution
# Apenas itera, coloca como potencial buyer, e compara com os prices 

class Solution:
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit