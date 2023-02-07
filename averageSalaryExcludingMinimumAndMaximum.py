# Average Salary Excluding the Minimum and Maximum Salary
# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

def average (salary) :
    # minSalary = min(salary)
    # maxSalary = max(salary)
    # sum = 0
    # for num in salary :
    #     sum += num
    # return (sum - minSalary - maxSalary)/(len(salary)-2)
    
    minSalary, maxSalary = salary[0], salary[0]
    sumSalary = 0
    for num in salary :
        if num < minSalary :
            minSalary = num
        if num > maxSalary :
            maxSalary = num
        sumSalary += num
    return (sumSalary - minSalary - maxSalary) / (len(salary) - 2)
print(average(salary=[4000,3000,1000,2000]))
