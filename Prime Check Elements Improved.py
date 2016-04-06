'prime check with pascals elements + smarter loop, no nesting and less multiplication'

def checkprimeelements(p):

    last=1

    for i in range (1,(((p-1)//2)+1)):

        new=(last*(p-i+1)//i)

        if new%p==0:

            last=new
            continue

        else:

            return

    print(p,'is prime')
    

def primecheck1(p):

    if pow(2,p,p) == 2:

        'print("{} is probable prime".format(p))'
        checkprimeelements(p)

    else:

        'print("{} is composite".format(p))'

from datetime import datetime

print(str(datetime.now()))

for p in range (3,100001,2):

    primecheck1(p)

print(str(datetime.now()))
