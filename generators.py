#----------------------------------------#

#----------------------------------------#
##Question 20
##Level 3
##
##Question:
##Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
##

def divisible_by_seven(num):
    #Test 0-num, skip to 7 since nothing <7 is divisible
    for i in range(7, num+1):
        if i%7==0:
            yield i

for i in divisible_by_seven(14):
    print i
