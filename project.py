# Name: Jack Caltagirone
#Number: G00349976

# create a python program that lets the user input an expression, and a string. the program will create a NFA from the
# expression, and compare it against the string

# i'll comment all unobvious lines of code. for more information please see readme


# these two lines just ask the user for and expression to make
# into a NFA, and get a string to compare against
#userExpression = input("Please enter a infix Expression: ")
#userString = input("Please enter a string to compare against the NFA: ")


def shunt(infix):

    specials = {'*': 3, '.': 2, '|': 1}
    # creates dictionary

    # making the profix and stack variales
    postfix = ""
    stack = ""

    # forloop that will parse the expression
    for c in infix:
        # first if takes the opening bracket for the equation and adds it to the stack
        if c == '(':
            stack = stack + c
        # since the open bracket is on the stack, if the for loop encounters a close bracket we check the stack
        # going to then check the stack all the way down until we find the open braket in the stack.
        elif c == ')':
            # while loops through the stack until it meets a the open bracket. it also adds everything that it meets along
            # the way to to the postfix variable.
            while stack[-1] != '(':
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            # line below gets rid of the open bracket that we just read in.
            stack = stack[:-1]
        elif c in specials:
            # if theres anything on the stack, this while will run.
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                postfix = postfix + stack[-1]
                stack = stack[:-1]
            stack = stack + c
        else:
            postfix = postfix + c

    # if there is anything on the stack after running through the for loop, you need to add them to the
    # end of the postfix.
    while stack:
        postfix = postfix + stack[-1]
        stack = stack[:-1]

    compile(postfix)

    return postfix


#############################################################################################################################
# above is the shunting. works by taking in the infix expression and parsing it through to postfix

class state:
    label = None
    edge1 = None
    edge2 = None

# this class just makes the variables for the nfa. the accept state and the initial state


class nfa:
    initial = None
    accept = None

    def __init__(self, initial, accept):  # first argument is 'self'
        self.initial = initial
        self.accept = accept


def compile(postfix):
    nfstack = []

    for c in postfix:

        if c == '.':
            # pop two nfas off the stack
            nfa2 = nfstack.pop()
            nfa1 = nfstack.pop()
            # connect first nfas accept state to the seconds intial
            nfa1.accept.edge1 = nfa2.initial
            # push nfa to the stack
            newNfa = nfa(nfa1.initial, nfa2.accept)
            nfstack.append(newNfa)

        elif c == '|':
            # pop two nfas off the stack
            nfa2 = nfstack.pop()
            nfa1 = nfstack.pop()
            # create a new initial state, connect it to initial states
            # of the two nfas popped from the stack
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            # create a new accept state, connecting the accept states
            # of the two nfa's popped of the stack, to the new state
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge2 = accept
            # push new nfa to the stack
            newNfa = nfa(nfa1.initial, nfa2.accept)
            nfstack.append(newNfa)

        elif c == '*':
            # pop a single nfa from the stack
            nfa1 = nfstack.pop()
            # create new initial and accpet states
            initial = state()
            accept = state()
            # join the new initial state to nfas initial state and the new acept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # join old accept state to the new accept state and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            # push the new nfa to the stack
            newNfa = nfa(nfa1.initial, nfa2.accept)
            nfstack.append(newNfa)

        else:
            accept = state()
            initial = state()
            initial.label = c
            initial.edge1 = accept
            nfstack.append(nfa(initial, accept))

    # should only have a single nfa
    return nfstack.pop()

#############################################################################################################################
# above is the code for the thompsons. chaning the postfix from shunting into an nfa


def followes(state):
    # return the set of states that can be readed from the state following e arrows
    # create a new set as state as its only member

    states = set()
    states.add(state)

    # check is state has arrows labelled e from it
    if state.label is None:
        # check if edge is a state
        if state.edge1 is not None:
            # if therse an edge1, foolow it
            states |= followes(state.edge1)
        if state.edge2 is not None:
            # if therse an edge1, foolow it
            states |= followes(state.edge2)

    return states


def match(userExpression, userString):

    # compiles the postfix from the shunting algorithum
    postfix = shunt(userExpression)
    nfa = compile(postfix)

    # current set of states and the next set of states
    current = set()
    nexts = set()

    # add the initial state to the current set
    current |= followes(nfa.initial)

    # loop through each char in string
    for s in userString:
        for c in current:
            # check if that state is labeled s
            if c.label == s:
                # add the edge1 state to the next set, including all the other sets that you've followed
                nexts |= followes(c.edge1)
        # set current to next, and clear out next
        current = nexts
        nexts = set()

    # check is accept state is in the set of the current states
    return(nfa.accept in current)


infixes = ["a.b.c", "a.(b).c*", "(a.(b|d))*","a.(b.b)*.c*"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]


#infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*","a.(b.b)*.c*"]
#strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

for i in infixes:
    for s in strings:
        print(match(i, s), i ,s)
