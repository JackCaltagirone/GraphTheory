#Name: Jack Caltagirone
#Number: G00349976

#this is my graph theory project. Please check read me about running the
#program along for notes on it. 

#I'll have most of the code comments here for single lines and methods but 
#most of the explantion will be done in the read me.

#basic input and puts the expression from infix to profix.
def shunt(infix):

    specials = {'*': 50, '.': 40, '|': 30}
    # creates dictionary
    # prioritize *, then . , then | 

    postfix = ""
    stack = ""

    #for statment
    for c in infix:

        #if statment with elifs and else at the bottom.
        if c == '(':
            stack = stack + c
            #adds the open braket to the stack
        elif c == ')':
            #if the input is a close braket then part of the expression is complete
            #it has to take the two brakets off and just add the alphbet t
            while stack[-1] != '(':
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            stack = stack[:-1]
        elif c in specials:
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            stack = stack + c
        else:
            postfix = postfix + c

    while stack:
        postfix = postfix + stack[-1]
        stack = stack[:-1]

    return postfix

print(shunt("(a.b)|(a*.b*)"))