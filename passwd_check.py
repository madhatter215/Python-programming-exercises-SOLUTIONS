##https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
##Question 18
##Level 3

##Question:
##A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
##Following are the criteria for checking the password:
##1. At least 1 letter between [a-z]
##2. At least 1 number between [0-9]
##3. At least 1 letter between [A-Z]
##4. At least 1 character from [$#@]
##5. Minimum length of transaction password: 6
##6. Maximum length of transaction password: 12
##Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
##Example
##If the following passwords are given as input to the program:
##ABd1234@1,a F1#,2w3E*,2We3345
##Then, the output of the program should be:
##ABd1234@1
##                              
##

##Python 2.7
##Requires enum-0.4.6 ("pip install enum")
from enum import Enum
class VERBOSITY(Enum):
    DEBUG=  5
    FULL=   4
    HIGH=   3
    MEDIUM= 2
    LOW=    1
    NONE=   0


myVerbo=VERBOSITY.NONE
print 'VERBOSITY = %s' %myVerbo

####################################
#Check for upper case character, lower case character, or digit
def check_chars(myinput, casecheck=''):
    if (myVerbo>=VERBOSITY.HIGH): print 'inside body of check_chars -> %s  casecheck -> %s' %(myinput, casecheck)
    if casecheck=='upper': myrange=(ord('a'), ord('z'))     #ASCII DEC 97-122
    elif casecheck=='lower': myrange=(ord('A'), ord('Z'))   #ASCII DEC 65-90
    elif casecheck=='digit': myrange=(ord('0'), ord('9'))   #ASCII DEC 48-57
    else:
        print 'unsupported parameter to check_lowercase function'; raise SystemExit
    if (myVerbo>=VERBOSITY.HIGH): print myrange
    x,y=myrange
    for i, j in ((i, j) for i in range(len(myinput)) for j in range(x,y+1)):
        if (myVerbo>=VERBOSITY.DEBUG): print 'i = %d  j = %d' %(i,j)
        if (myVerbo>=VERBOSITY.DEBUG): print 'myinput[i] = %s   chr(j) = %s' %(myinput[i], chr(j))
        if myinput[i] == chr(j): return True
        else: continue
    return False

####################################
#Check for a special character $#@
def check_special_char(myinput):
    if (myVerbo>=VERBOSITY.HIGH): print 'inside body of check_special_char -> %s' %myinput
    if '$' in myinput or '#' in myinput or '@' in myinput: return True
    else: return False

####################################
#Check passwd length at least 6 but no more than 12
def check_length(myinput):
    if (myVerbo>=VERBOSITY.HIGH): print 'inside body of check_length -> %s' %myinput
    if (6 <= len(myinput) <= 12): return True
    else: return False


###########################
# Start of program
###########################
USER_INPUT = raw_input('> ')
myinput=USER_INPUT.split(',')
for passwd in myinput:
    if check_chars(passwd, 'upper') and check_chars(passwd, 'lower') and check_chars(passwd, 'digit') and check_special_char(passwd) and check_length(passwd): print passwd
