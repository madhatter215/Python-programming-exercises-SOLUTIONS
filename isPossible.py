#/usr/bin/python3

#https://codereview.stackexchange.com/questions/49418/determining-if-an-answer-can-be-generated

#not used
def transformation1(x,y):
    return (x+y,y)

#not used    
def transformation2(x,y):
    return (x,x+y)

def  isPossible(a, b, c, d):
    seen = [] #list
    print ("({},{}) ({},{})".format(a,b,c,d))#debug
    ###
    #code
    x = c
    y = d
    while (x >= 1) and (y >= 1):
        if x >= y:
            print ("subtract x from y")
            x = x - y
        else: 
            print ("subtract y from x")
            y = y - x
        print ('\t',x,y)
        seen.append( (x,y) )
    ###
    if (a,b) in seen:
        return "Yes"
    else:
        return "No"



print (isPossible(1,4,5,9),'\n')
print (isPossible(1,2,3,6),'\n')
print (isPossible(3,7,27,17),'\n')
