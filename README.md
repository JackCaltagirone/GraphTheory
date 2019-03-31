# GraphTheory
G00349976 graph theory Project


When we got the problem i thought about it for a while. didnt understand how i would go about it.
After watching the videos provided, it gave insight on how i should go about it.

I decided to break the project into 4 mains steps.

Step 1: Take in the user input of an expression, and a string

Step 2: shunt the input from infix to postfix

Step 3: turn the postfix input into a NFA

Step 4: Compare the newly created NFA to the user entered String


Step 1: Wishing the other steps were as easy as this one. It was a simple two lines.
the the lines are located @ lines 12 and 13. simple takes input and assings them to two variables 
approately named

Step 2: I now take the user entered expression and parse it through the shunting yard algoritim. 
Parsing it through the algoritim will change the user inputed infix notation expression to a postfix notation expression.
I started of by creating the dictionary of the operaters. the special characters have
precedence in the order of: * . | ? +. we do this because the * is always counted first, much
like bimdas that there is precedence in it.

made the profix and stack variables. the stack is for the all the special characters as well as the open brackets.
shunting adds all the special charaters and brackets to the stack. when it encounters a close bracket, it must have encountered an open bracket. therefore when it encounters a closed braket it will add everything to the postfix until it reaches the open bracket. 
it then repeats this until there are no bracket.

The while at lines 42 to 45 have a while that will loop through the stack at the end of the expression and add all the remaining items to the expression.
thats basicly how the shunting works and the first part of the project. I will take that post fix notation  expression and push it through to the thompsons which is step 3


Step 3: With the third step, I'm taking the postfix from step 2 and turning it into a non deterministic finite automata.
to do this 
