#lunch_money2.py
#http://www.ardendertat.com/2011/09/17/programming-interview-questions-1-array-pair-sum/

#Find pairs or people who have $1.00 for lunch and match them up
#given a list, find matches (pairs) that add up to 100; reject ones that don't have a match or odd numbers

def pairSum2(arr, k):
    if len(arr)<2:
        return
    seen=set()
    output=set()
    for num in arr:
        target=k-num
        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target), max(num, target)) )
            
    print '\n'.join( map(str, list(output)) )


myarray=[50,50,60,40,90,20,10,80,13,12,10,87,97,3,50,80,20]
pairSum2(myarray, k=100)
##Note, even though 80/20 are in the list twice, it only gets printed once because output is a set
