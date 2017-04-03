"""
Problem 7: Merge Sorted Arrays

Given two sorted arrays/lists as input, return a merge sorted array of the given arrays.
Example:
input   => [2,3,5,7], [1,4,6,8]
output  => [1,2,3,4,5,6,7,8]
"""

def merge_sorted_arrays(arr1, arr2):

    merge_sorted_array = [0] * (len(arr1)+len(arr2))

    current_arr1_index = 0
    current_arr2_index = 0
    current_merged_index = 0

    while current_merged_index < len(merge_sorted_array):

        #check if arr1 is exhausted
        if current_arr1_index == len(arr1):
            merge_sorted_array[current_merged_index] = arr2[current_arr2_index]
            current_arr2_index += 1

        #check if arr2 is exhausted
        elif current_arr2_index == len(arr2):
            merge_sorted_array[current_merged_index] = arr1[current_arr1_index]
            current_arr1_index += 1

        elif arr1[current_arr1_index] < arr2[current_arr2_index]:
            merge_sorted_array[current_merged_index] = arr1[current_arr1_index]
            arr1[current_arr1_index] = 0
            current_arr1_index += 1

        else:
            merge_sorted_array[current_merged_index] = arr2[current_arr2_index]
            arr2[current_arr2_index] = 0
            current_arr2_index += 1

        current_merged_index += 1

    return merge_sorted_array

print(merge_sorted_arrays([2,5,7,9], [1,3,4,11, 18]))
