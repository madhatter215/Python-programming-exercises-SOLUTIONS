###----------------------------------------#
##
###----------------------------------------#
##Question 22
##Level 3
##
##Question:
##Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
##Suppose the following input is supplied to the program:
##> the quick brown fox fox apple apple apple pear
##brown:1
##apple:3
##pear:1
##fox:2
##quick:1

mydict={}
def f(sentence):
    global mydict
    for word in sentence:
        if word not in mydict:
            #add it and set val to 1
            mydict[word] = 1
        else:
            #+1 value
            mydict[word] = mydict[word] + 1



###########################
# Start of program
###########################
USER_INPUT = raw_input('> ')
f(USER_INPUT.split(' '))
for i in mydict:
    print '%s:%d' %(i,mydict[i])
