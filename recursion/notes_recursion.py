'''
How to reason with recursion:

    Use Induction
        State what your function should do/return
        Assume that it works before writing the function
        Write the function under this assumption
    
    Idea (Mergesort):
        Given a list, sort the first half recursively, sort the second half recursively, then merge the two sorted halves

        1. State the function and what it does
            def mergeSort(arr): # sorts arr

        2. Assume there is a function that will do what its supposed to
            def mergeSort(arr): # sorts arr
                if len(arr) == 1: return
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]
            L = TRUE_Sort(L) #imaginary function that does what its supposed to
            R = TRUE_Sort(R)
            return merge(L,R)

'''

random_list = [15, 10, 7, 6, 5, 3, 17, 19,
               9, 4, 2, 0, 1, 16, 11, 18, 8, 14, 12, 13]


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    def merge(left, right):
        res = []
        idx_left, idx_right = 0, 0
        while idx_left < len(left) and idx_right < len(right):
            if left[idx_left] <= right[idx_right]:
                res.append(left[idx_left])

    return merge(left, right)
