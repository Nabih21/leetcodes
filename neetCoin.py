class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        left, right = 0, 1
        profit = 0
        while right < len(prices) : 
            if prices[left] < prices[right] : 
                temp = prices[right] - prices[left] 
                profit = max(profit, temp) 
            else : 
                left = right
            right += 1 
        
        return profit


                 


if __name__ == "__main__":
    solution = Solution()
    # prices = [7,1,5,3,6,4]
    prices=[5,1,5,6,7,1,10]

    print(solution.maxProfit(prices))  # Output the result

                