userInput = input("Example 1: Type a letter further along than 'h'")

if userInput > 'h':
    print('good job!')
else:
    print('Sorry! You are incorrect!')

userInput = input("Example 2: Type a letter further along than 'h'")
if userInput > 'h':
    print('good job!')
elif userInput > 'e':
    print("Close! Try again")
else:
    print('Sorry! You are incorrect!')

userInput = input("Example 3: Type a letter further along than 'h'")
if userInput > 'h':
    print('good job!')
elif userInput > 'i':
    print("Will not reach this statement!")
elif userInput > 'e':
    print("Close! Try again")

else:
    print('Sorry! You are incorrect!')
