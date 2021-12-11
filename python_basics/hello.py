#This program says Hello, and asks for a name.

print('Hello World!')
print('What is your name?')
userName = input()
print("It's good to meet you, " + userName)
print('Your name appears to be ' + str(len(userName)) + ' letters long.')
print('How old are you? (In years)')
userAge = input()
print("Huh... ...It looks like you'll be " + str(int(userAge) + 1) + ' a year from now.')
