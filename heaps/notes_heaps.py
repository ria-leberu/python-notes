# Heaps are a tree data structure that satisfy the heap property:
# Min Heaps are when the parent node is less than or equal to a child, the minimum value at the root
# Max Heaps are when the parent is greater than or equal to a child, the maximum value at the root
# Binary heaps are the most common
# A priority queue is an abstract data type, and a heap is the implementation of it

# Heaps are implemented using an array and not a tree structure

# Heaps are used for finding the smallest or largest item in a dataset quickly
# When you see problems like "Kth" in the title, consider heaps

# Important areas where heaps are used:
# Heap sort, Graph algorithms (to find the shortest path, like Djikstras or Prim's MST), Selection algorithms (find median in data stream, find kth element in a list), K-way merge (merging data sets)

# Time Complexity of Heaps
# heappush(name_of_heap, val) -> Insert O(log N)
# heappop (name_of_heap) -> Pop O(log N)
# name_of_heap[0] -> Peek O(1)
# Remove Min O(log N)
# Heapify O(N)

from heapq import heapify, heappush, heappop

nums = [5, 4, 22, 8, 15, 11, 16, 101, 23, 42]

# heapify(nums)  # in place convert to heap
# print(heappop(nums))

# for max heap, negate all elements before inserting into heap
heapify(nums)

print("The five smallest numbers are: ", end="")
for i in range(5):
    print(f"{heappop(nums)}", end=" ")


# heapify(nums)
# print(-heappop(nums))
