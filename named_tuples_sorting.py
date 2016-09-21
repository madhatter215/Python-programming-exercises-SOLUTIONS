#----------------------------------------#

#----------------------------------------#
##Question 19
##Level 3
##
##Question:
##You are required to write a program to sort the (name, age, height[sic. 'score']) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
##1: Sort based on name;
##2: Then sort based on age;
##3: Then sort by score.
##The priority is that name > age > score.
##If the following tuples are given as input to the program:
##Tom,19,80
##John,20,90
##Jony,17,91
##Jony,17,93
##Json,21,85
##Then, the output of the program should be:
##[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

import operator
import collections

Student=collections.namedtuple('Student', 'name age score')
record=[]

def add_and_sort_students(user_input):
    #TODO: do some checking
    global record
    new_stu=Student(name=user_input[0], age=user_input[1], score=user_input[2])
    record.append(new_stu)
    print "Record added"
    print record
    record=sorted(record, key=operator.attrgetter('name', 'age', 'score'))
    print "Sorted list"
    print record



###########################
# Start of program
###########################
while True:
    USER_INPUT = raw_input('> ')
    if USER_INPUT=='': raise SystemExit
    myinput=USER_INPUT.split(',')
    add_and_sort_students(user_input=myinput)
