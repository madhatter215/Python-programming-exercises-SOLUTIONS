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
  ## upper check
  if not re.search("[A-Z]", p):
    myflag = 0
  ###############################
  ## digit check
  elif not re.search("[0-9]", p):
    myflag = 0
  ###############################
  ## lower check
  elif not re.search("[a-z]", p):
    myflag = 0
  ###############################
  ## special char check
  elif not re.search("[$#@]", p):
    myflag = 0
  ###############################
  ## length check
  elif not (6 <= len(p) <= 12):
    myflag = 0
  ###############################
  ##debug statement
  if (myVerbo.value>=VERBOSITY.HIGH.value): print myflag
  ###############################
  # if 'p' passed all checks, add to the list
  if (myflag):
    value.append(p)
  

print ",".join(value)
