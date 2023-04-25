import heapq

# Create an empty heap
heap = []

# Add elements to the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)

# Peek at the smallest element in the heap
print(heap[0])  # Output: 1

# Remove the smallest element from the heap
smallest = heapq.heappop(heap)

# Peek at the new smallest element in the heap
print(heap[0])  # Output: 3

# Convert a list to a heap
list_to_heap = [5, 3, 8, 1]
heapq.heapify(list_to_heap)
print(list_to_heap)

# Peek at the smallest element in the new heap
print(list_to_heap[0])  # Output: 1
