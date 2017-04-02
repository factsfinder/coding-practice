"""
Problem 2: Array Pair Smm
Given an integer array, output all the unique pairs that
sum up to a specific value 'sum'.

So the input:
pair_sum([1,3,2,2],4) would return 2 pairs:
 (1,3)
 (2,2)

"""

def pair_sum(arr, sum):

    # The list below is the one we will return.
    # It contains the array pairs that satisfies the given sum
    pairs = []

    # convert the given list/array into a dictionary
    d = {}
    for n in arr:
        count = 0
        if n in d: continue
        else: d[n] = "Unchecked"

    for k in d:
        if (sum-k) in d:
            if d[sum-k] is "checked":
                continue
            else:
                d[sum-k] = "checked"
                d[k] = "checked"
                pairs.append((sum-k, k))

    return "Number of Pairs: " + str(len(pairs)) + "\n" + str(pairs)

print(pair_sum([1,3,2,2],4))
