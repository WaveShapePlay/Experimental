print("Example 1")
userInput = input("Would you like to contine through the loop? Type y for yes:  ")

while(userInput == 'y'):
    print('Keep looping')
    userInput = input("Continue? Type y for yes or any key for no")
else:
    print('Good bye')
    
    
print("Example 2")
response = 1

while(response):
    userInput = input("Continue looping? Type y for yes or n for no ")

    if userInput == 'n':
        response = 0
        print("Good bye")

    else:
        response = 1

print("Example 3")
response = 1
while(response):
    userInput = input("Continue looping? Type y for yes or any key for no ")

    if userInput == 'y':
        print("keep looping")

    if userInput == 'n':
        print("Incorrect Key")
        break

    
print("Example 4")
response = 1
while(response):
    userInput = input("Continue looping? Type y for yes or any key for no ")

    if userInput != 'y':
        pass
    else:
        print("you selected y")
