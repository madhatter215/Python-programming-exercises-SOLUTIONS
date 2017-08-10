# # write a loop from 1 to 100 
# # if the number is a multiple of 3 print fizz
# # if the number is a multiple of 5 print buzz
# # if the number is a multiple of 3 and 5 print fizzbuzz

DEBUG = 0
 
 for i in range(1,100):
     if DEBUG: print (i)#debug
     output = ''
     
     if i % 3 == 0:
         output += 'fizz'
         #print ('fizz')
     if i % 5 == 0:
         output += 'buzz'
         #print ('buzz')
         
     if output: print (i,output)

#
