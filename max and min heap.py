# Heap Sort Program (Max-Heap and Min-Heap)

def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def max_heap_sort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
    # Extract elements (ascending order)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

def min_heap_sort(arr):
    n = len(arr)
    # Build min heap
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)
    # Extract elements (descending order)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        min_heapify(arr, i, 0)

# Get user input
user_input = input("Enter numbers separated by spaces: ")
original = list(map(int, user_input.split()))

# Sort using max-heap (ascending)
ascending = original.copy()
max_heap_sort(ascending)

# Sort using min-heap (descending)
descending = original.copy()
min_heap_sort(descending)

print("\nOriginal array:", original)
print("Max-Heap Sorted (Ascending):", ascending)
print("Min-Heap Sorted (Descending):", descending)
