def binary_search(arr, target):
    # Set initial left and right boundaries
    left, right = 0, len(arr) - 1
    
    # Loop until the left boundary is greater than the right
    while left <= right:
        # Find the middle element
        mid = (left + right) // 2
        
        # Check if the target is at the mid
        if arr[mid] == target:
            return mid  # Target found, return the index
        
        # If target is smaller, ignore the right half
        elif arr[mid] > target:
            right = mid - 1
        
        # If target is larger, ignore the left half
        else:
            left = mid + 1
    
    return -1  # Target not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = int(input("Enter the number to search: "))

# Ensure the input is an integer and the list is sorted
if not arr:  # Check if array is empty
    print("Array is empty.")
else:
    result = binary_search(arr, target)

    if result != -1:
        print(f"Target found at index {result}")
    else:
        print("Target not found in the array")
