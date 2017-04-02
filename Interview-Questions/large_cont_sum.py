"""
Problem 4: Largest Continuous Sum
Given an array of integers (positive and negative)
find the largest continuous sum.
"""

def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
    # We loop through the given array and add every number to the previous sum
    # and also keep track of the largest Continuous sum at every iteration
    num = arr[0]
    large_cont_sum = arr[0]
    for i in range(1, len(arr)):
        num += arr[i]
        large_cont_sum = max(large_cont_sum, num)
    return large_cont_sum

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
