##https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
##Question 18
##Level 3
##
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
# Sample input:
#ABd1234@1,a F1#,2w3E*,2We3345,sdfGGK$33


#########################################################
## Debug Class for Verbose Messages (author madhatter215)
#########################################################
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


myVerbo=VERBOSITY.MEDIUM
print 'VERBOSITY = %s' %myVerbo
##################################################
## Start of Program:
##################################################
import re
value = []
items=[x for x in raw_input('> ').split(',')]

if (myVerbo.value>=VERBOSITY.HIGH.value): print items

for p in items:
  myflag = 1
  ###############################
  #upper check
  if not re.search("[A-Z]", p):
    myflag = 0
  ###############################
  #digit check
  elif not re.search("[0-9]", p):
    myflag = 0
  ###############################
  #lower check
  elif not re.search("[a-z]", p):
    myflag = 0
  ###############################
  #special char check
  elif not re.search("[$#@]", p):
    myflag = 0
  ###############################
  #length check
  elif not (6 <= len(p) <= 12):
    myflag = 0
  ##debug statement
  if (myVerbo.value>=VERBOSITY.HIGH.value): print myflag
  ###############################
  # if passed all checks, add to the list
  if (myflag):
    value.append(p)
  

print ",".join(value)
