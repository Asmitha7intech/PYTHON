from collections import deque

def is_palindrome(s):
    # Clean the string: lowercase and remove spaces
    s = s.replace(" ", "").lower()

    # Create deque with characters of the string
    char_deque = deque(s)

    while len(char_deque) > 1:
        front = char_deque.popleft()
        rear = char_deque.pop()
        if front != rear:
            return False
    return True

# Main Program
user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")
