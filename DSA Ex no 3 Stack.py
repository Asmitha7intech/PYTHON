def reverse_string(input_string):
    # Create an empty stack
    stack = []
    
    # Push all characters of the string onto the stack
    for char in input_string:
        stack.append(char)
    
    # Pop characters from the stack to reverse the string
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage
input_string = input("Enter a string to reverse: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)
