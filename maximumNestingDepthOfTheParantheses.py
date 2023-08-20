# Maximum Nesting Depth of the Parentheses
def maxDepth(s):
    max_depth = 0
    stack = 0
    for char in s:
        if char == "(":
            stack += 1
            max_depth = max(max_depth, stack)
        elif char == ")":
            stack -= 1
    return max_depth
print(maxDepth(s = "8*((1*(5+6))*(8/6))"))
    