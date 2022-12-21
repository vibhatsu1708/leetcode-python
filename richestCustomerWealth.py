# Richest Customer Wealth
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
def maximumWealth (accounts) :
    accountMax = 0
    for accountValues in accounts :
        accountSum = 0
        for eachAccountValue in accountValues :
            accountSum += eachAccountValue
            if accountSum > accountMax :
                accountMax = accountSum
    return accountMax
            
print(maximumWealth(accounts=[[1,5],[7,3],[3,5]]))
            