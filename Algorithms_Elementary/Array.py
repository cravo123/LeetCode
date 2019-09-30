# 1. Sorting
# https://en.wikipedia.org/wiki/Sorting_algorithm
# Implement various sorting algorithms, here sorting is increasing sorting

# 1.1 Bubble Sort
# Compare values in neighbor, and move larger to the right, 
# After one iteration, the largest value will move to the rightmost.
# After n iteration, the array will be sorted.
# Time Complexity, O(n ^ 2)
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1): # since we compare arr[j] and arr[j + 1], so range(n - i - 1) here
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# 1.2 Insertion Sort
# Maintain an invariant here, so for the k-th iteration, we make sure arr[:k] is sorted.
# For each iteration, we find the place where the value should be inserted.
# So after n iterations, the array will be sorted.
# Time Complexity, O(n ^ 2)
def insertion_sort(arr):
    arr = arr.copy()
    n = len(arr)

    for i in range(1, n):
        j = i - 1
        v = arr[i]
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j] # move this element one position right by copying arr[j] to arr[j + 1]
            j -= 1
        arr[j + 1] = v
    
    return arr

# 1.3 Merge Sort
# Merge sort uses the idea of recursion and Divide and Conquer.
# We solve the problem of size n by first solving the problem of size n / 2, and then merge them together.
# Here we sort the array of length n by first assuming we have sorted sub-array of length n / 2.
# Remember in order for recursion to work, we need to have a base-case that can be solved without calling 
# recursion function. For the array sorting problem, the base case is if array length is less than or equal to 1
# Time Complexity, O(n log n)
def merge_sort(arr):
    arr = arr.copy()
    n = len(arr)

    _merge_sort_helper(arr, 0, n - 1)

    return arr

def _merge(arr, start, mid, end):
    auxilliary = arr.copy()
    curr = start
    i, j = start, mid + 1
    while curr <= end:
        if i <= mid and j <= end:
            if auxilliary[i] < auxilliary[j]:
                v = auxilliary[i]
                i += 1
            else:
                v = auxilliary[j]
                j += 1
        elif i <= mid:
            v = auxilliary[i]
            i += 1
        else:
            v = auxilliary[j]
            j += 1
        arr[curr] = v
        curr += 1

def _merge_sort_helper(arr, start, end):
    # Base case: if length <= 1
    if start >= end:
        return
    
    mid = (start + end) // 2
    _merge_sort_helper(arr, start, mid)
    _merge_sort_helper(arr, mid + 1, end)
    _merge(arr, start, mid, end)

# 1.4 Quick Sort
# Quick sort also uses the idea of Divide and Conquer. 
# We first find a pivot value, and then 
# put every value < pivot value to the left,
# put every value >= pivot value to the right.
# Variant of this algorithm can be applied to 
#   1) Find the largest k-th value in O(n) time,
#   2) Two-pointer, Three-pointer problem, like Dutch national flag problem，
#      Notice that the find_pivot() function uses the idea of two-pointer.
# Time Complexity, worst-case O(n ^2), average O(n Log n), 
# But in most cases, quick sort is the fastest
def quick_sort(arr):
    arr = arr.copy()

    quick_sort_helper(arr, 0, len(arr) - 1)

    return arr

def quick_sort_helper(arr, start, end):
    # base case when length <= 1
    if start >= end:
        return

    idx = find_pivot(arr, start, end)
    quick_sort_helper(arr, start, idx - 1)
    quick_sort_helper(arr, idx + 1, end)

def find_pivot(arr, start, end):
    mid = (start + end) // 2
    v = arr[mid]
    arr[mid], arr[end] = arr[end], arr[mid]

    j = start
    i = start
    while i < end:
        if arr[i] <= v:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1
    arr[j], arr[end] = arr[end], arr[j]

    return j

# 1.5 Heap Sort
# TODO:

# 1.6 Counting Sort
# TODO:



if __name__ == '__main__':
    import random

    arr = list(range(10))
    random.shuffle(arr)
    print('Before:         ', arr)

    print('Bubble Sort:    ', bubble_sort(arr))
    print('Insertion Sort: ', insertion_sort(arr))
    print('Merge Sort:     ', merge_sort(arr))
    print('Quick Sort:     ', quick_sort(arr))

