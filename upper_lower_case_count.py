#Question 14
#Level 2
#Question:
#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

#Python 3.5.2

myList = input('> ')
upperCount = 0
lowerCount = 0
for letter in myList:
  if letter.isupper():
    upperCount += 1
  elif letter.islower():
    lowerCount += 1
  else:
    print ('letter "{}" is neither upper or lower case'.format(letter))

print ('\nUPPERCASE = "{0}"\nlowercase = "{1}"'.format(upperCount, lowerCount))

