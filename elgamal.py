import math
import time
from random import *

if __name__ == "__main__":
    print("The program starts ")
    p = 257
    g = 2585
    x = 47
    message = '105'
    m = int(message)
    r = 65
    # r=randint(1,p-2)
    print("The value of r is: ",r)
    

    print("The message is", m)
    # to compute y= g^x = 2585^47(mod 2879) = 2826(mod 2879)

    # Key generation
    t1 = time.time()
    mody = pow(g, x, p)  # a=2585,b=47
    print("The value of y is :", mody, "mod", p)
    t2 = time.time()
    time_taken = t2 - t1
    print("The tasks took", time_taken, "seconds to execute")
    # print("y= g^x is %d mod %d" % (mody,p))

    # Encryption
    t1 = time.time()
    modc1 = pow(g, r, p)
    print("The length of modc1 is:",len(str(modc1)))
    print("The value of c1 is :", modc1, "mod", p)
    modc2 = pow((m+1)*pow(mody, r, p), 1, p)
    print("The value of c2 is :", modc2, "mod", p)
    print("The length of modc2 is:",len(str(modc2)))
    t2 = time.time()
    time_taken = t2 - t1
    print("The tasks took", time_taken, "seconds to execute")

    # Decryption
    t1 = time.time()
    c3 = pow(modc1, -x, p)
    print("The value of revModulo is:", c3)
    m2 = pow(modc2 * c3, 1, p)-1  # decrypted message
    print("The value of decrypted message is :", m2)
    t2 = time.time()
    time_taken = t2 - t1
    print("The tasks took", time_taken, "seconds to execute")
