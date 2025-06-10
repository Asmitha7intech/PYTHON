
user_input = input("Enter numbers separated by spaces: ")


numbers = list(map(int, user_input.split()))


for i in range(1, len(numbers)):
    key = numbers[i]
    j = i - 1
    
    
    while j >= 0 and key < numbers[j]:
        numbers[j + 1] = numbers[j]
        j -= 1
    numbers[j + 1] = key


print("Sorted list:", numbers)
