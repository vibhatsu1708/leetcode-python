# Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit (prices) :
    buy = prices[0]
    sell = 0
    for i in range (len(prices)) :
        if prices[i] > buy :
            sell = max(sell, prices[i] - buy)
        buy = min(buy, prices[i])
    return sell
print(maxProfit(prices = [7,6,4,3,1]))