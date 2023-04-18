# Find the Maximum Divisibility Score
# You are given two 0-indexed integer arrays nums and divisors. The divisibility score of divisors[i] is the number
# of indices j such that nums[j] is divisible by divisors[i]. Return the integer divisors[i] with the maximum
# divisibility score. If there is more than one integer with the maximum score, return the minimum of them.
def maxDivScore(nums, divisors):
    maxScore, maxDivisor = -1, -1
    for divisor in divisors:
        score = 0
        for num in nums:
            if num % divisor == 0:
                score += 1
        if score > maxScore or (score == maxScore and divisor < maxDivisor):
            maxScore = score
            maxDivisor = divisor
    return maxDivisor


print(maxDivScore(nums=[20, 14, 21, 10], divisors=[5, 7, 5]))
