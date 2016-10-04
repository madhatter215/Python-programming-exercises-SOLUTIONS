#given an input such as 'aaaabbbbbcccddddddaa' the output is 'a4b5c3d6a2'
#write the program

def rle(myinput):
    myinput = ''.join((myinput, ' ')) #appends white space at end
    output=''
    count=1
    lastSeen=''
    for i in myinput:
        print i,lastSeen
        if i == lastSeen:
            count += 1
        else:
            if not lastSeen=='':
                output += ''.join([lastSeen, str(count)])
            lastSeen=i
            count=1

    print output

rle('aaaabbbbbcccddddddaa')
