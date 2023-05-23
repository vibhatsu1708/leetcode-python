# Summary Ranges
# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element ofnums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:
# "a->b" if a != b
# "a" if a == b

def summaryRanges(nums):
    ranges = []
    first, second = 0, 1
    while (second < len(nums)):
        if (nums[second] - nums[second-1]) == 1:
            second += 1
        else:
            if first == second - 1:
                ranges.append(f"{nums[first]}")
            else:
                ranges.append(f"{nums[first]}->{nums[second-1]}")
            first = second 
            second += 1
    if first == second-1:
        ranges.append(str(nums[first]))
    else:
        ranges.append(f"{nums[first]}->{nums[second-1]}")
    return ranges
print(summaryRanges(nums = [0,2,3,4,6,8,9]))