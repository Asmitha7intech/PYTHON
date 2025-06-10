def evaluate_postfix(expression):
    # Stack to store operands
    stack = []
    
    # Split the expression by spaces to handle multi-digit numbers and operators
    tokens = expression.split()

    # Traverse each token in the expression
    for token in tokens:
        # If the token is a number (operand), push it to the stack
        if token.isdigit():
            stack.append(int(token))
        else:
            # Ensure there are enough operands to apply the operator
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression. Not enough operands for operator.")
            
            # Pop operands for the operation
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Apply the operator
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                # Handle division carefully to avoid division by zero
                if operand2 == 0:
                    raise ValueError("Cannot divide by zero.")
                result = operand1 / operand2
            else:
                raise ValueError(f"Unknown operator: {token}")
            
            # Push the result back to the stack
            stack.append(result)
    
    # The result should be the only element left in the stack
    if len(stack) != 1:
        raise ValueError("Invalid postfix expression. The stack should contain exactly one result.")
    
    return stack.pop()

# Example usage
try:
    expression = input("Enter a postfix expression (with spaces between operands and operators): ")
    result = evaluate_postfix(expression)
    print("Result:", result)
except Exception as e:
    print("Error:", e)
