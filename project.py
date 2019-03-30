# Name: Jack Caltagirone
#Number: G00349976

# create a python program that lets the user input an expression, and a string. the program will create a NFA from the
# expression, and compare it against the string

# i'll comment all unobvious lines of code. for more information please see readme


# these two lines just ask the user for and expression to make
# into a NFA, and get a string to compare against 
userExpression = input("Please enter a infix Expression: ")
#userString = input("Please enter a string to compare against the NFA: ")


def shunt(infix):

    specials = {'*': 3, '.': 2, '|': 1}
    # creates dictionary

    #making the profix and stack variales
    postfix = ""
    stack = ""

    #forloop that will parse the expression
    for c in infix:
        #first if takes the opening bracket for the equation and adds it to the stack
        if c == '(':
            stack = stack + c
        #since the open bracket is on the stack, if the for loop encounters a close bracket we check the stack
        #going to then check the stack all the way down until we find the open braket in the stack.
        elif c == ')':
            #while loops through the stack until it meets a the open bracket. it also adds everything that it meets along
            #the way to to the postfix variable.
            while stack[-1] != '(':
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            #line below gets rid of the open bracket that we just read in.
            stack = stack[:-1]
        elif c in specials:
            #if theres anything on the stack, this while will run.
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            stack = stack + c
        else:
            postfix = postfix + c

    #if there is anything on the stack after running through the for loop, you need to add them to the 
    #end of the postfix.
    while stack:
        postfix = postfix + stack[-1]
        stack = stack[:-1]
    
    return postfix

print(shunt(userExpression))




