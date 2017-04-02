"""
Problem 3: Find the missing element

Consider an array of non-negative integers.
A second array is formed by shuffling the elements of the first array and deleting a random element.
Given these two arrays, find which element is missing in the second array.
Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:
missing([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output:
5 is the missing number

"""

def missing(list1, list2):

    d = {}
    for i in list2:
        count = 1
        if i in d: d[i] += 1
        else: d[i] = count

    for j in list1:
        if j in d: d[j] -= 1
        else: return str(j) + " is the missing number"

    for k in d:
        if d[k] < 0: return str(k) + " is the missing number"

print(missing([5,5,7,7],[5,7,7]))
