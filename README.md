# GraphTheory
G00349976 graph theory Project

Running the project: 
Download the script and open the containing folder in cmd. run "python project.py", then enter your expression and String as prompted.




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

made the profix and stack variables. the stack is for the all the special characters as well as the open brackets.
shunting adds all the special charaters and brackets to the stack. when it encounters a close bracket, it must have encountered an open bracket. therefore when it encounters a closed braket it will add everything to the postfix until it reaches the open bracket. 
it then repeats this until there are no bracket.

The while at lines 42 to 45 have a while that will loop through the stack at the end of the expression and add all the remaining items to the expression.
thats basicly how the shunting works and the first part of the project. I will take that post fix notation  expression and push it through to the thompsons which is step 3


Step 3: With the third step, I'm taking the postfix from step 2 and turning it into a non deterministic finite automata.
to do this we made a state of edge1, edge2 and a label.
in essence this step is a big if else statement. looping though the string and checking each character if its in the special character.
i wont go threw all of them but an example is the '.' or follows.
nfa2 is popped first, then nfa1. as then it'll be the actual way its popped off. then its new nfa = nfa, which creates the new nfa.


step 4: Now that we have the NFA from step 3, we need to take in a string a match it with the nfa. but first we'll make a followEs method. this is going to follow any E's in the nfa. 

the match function at line 191 is what I'm going to use to check the nfa against the string. starts by making postfix equal shunt(infix), takes the infix that the user inputs and parses it into postfix.
nfa = compile(postfix) then takes that postfix notation into the compilers and created the nfa. we'll be using nfa for this method.
then its just a python method that compares the strings against each other. 
final print(match) at line 219 prints out if the string match


Process:
I had alot a problems with the start of this project. from the start i just started rewatching the videos coding along. the shunting was fine, i understood it. but when it came to thompsons it took me watching through the hand written video at least 4 time and doing it out myself before i fully understood it. 
When it came to coding i was commenting as i went.  it really helped as alot when i was going back over it. 
for putting it all together it was good with the help of peers helping out.
it was a final rush on the last day that i managed to fix everything working


Referances: 
I gave a look online for thompsons and shunting.I got these slides on thomspons that helped me
http://cse.iitkgp.ac.in/~bivasm/notes/scribe/11CS10055.pdf

I didnt find anything useful on shunting as i was very well informed with the videos.
