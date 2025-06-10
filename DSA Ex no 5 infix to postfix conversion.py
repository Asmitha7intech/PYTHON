def isOperator(ch):
    return (ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '%' or ch == '^')
    
def getPrecedence(op):
    if op=='^':
        return 3
    elif(op=='*' or op=='/' or op=='%'):
        return 2
    elif(op=='+' or op=='-'):
        return 1 
    else: 
        return -1

N = int(input())
infix = input()
postfix = ''
stack = []

for i in infix:
    #isalnum function returns true if the char is alphanumeric (alphabet or a number)
    if i.isalnum():
        postfix+=i 
    #Complete this code to get the postfix expression in the the postfix string

while(len(stack)!=0):
    postfix+=stack.pop()

print(postfix)
