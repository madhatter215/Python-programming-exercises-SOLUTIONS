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


a = "the quick brown fox fox apple apple apple pear"
a = a.split()
b = {x:a.count(x) for x in a}
print b

#note, the example is not sorted
