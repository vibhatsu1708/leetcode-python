# Buy Two Chocolates
# You are given an integer array prices representing the prices of various chocolates in a store. You are also given a single integer money, which represents your initial amount of money.
# You must buy exactly two chocolates in such a way that you still have some non-negative leftover money. You would like to minimize the sum of the prices of the two chocolates you buy.
# Return the amount of money you will have leftover after buying the two chocolates. If there is no way for you to buy two chocolates without ending up in debt, return money. Note that the leftover must be non-negative.

def buyChoco(prices, money):
	leftover = money
	minSum = float('inf')

	for i in range(len(prices)):
		for j in range(i + 1, len(prices)):
			sumPrices = prices[i] + prices[j]
			if sumPrices <= money:
				minSum = min(minSum, sumPrices)

	if minSum == float('inf'):
		return money
	else:
		leftover -= minSum
		return leftover
print(buyChoco(prices = [1,2,2], money = 3))