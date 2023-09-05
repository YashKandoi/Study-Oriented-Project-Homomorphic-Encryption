import math
import time
from functions import *

if __name__ == "__main__":
    
    print("The program starts ")
    p = 257
    g = 2585
    x = 47
    message = '11'
    m = int(message)
    r = 65

    print("The message is", m)
    # to compute y= g^x = 2585^47(mod 2879) = 2826(mod 2879)
    mody = pow(g, x, p)  # a=2585,b=47
    # print("y= g^x is %d mod %d" % (mody,p))
    modc1 = pow(g, r, p)
    print("The value of c1 is :", modc1, "mod", p)
    modc2 = pow(m*pow(mody, r, p), 1, p)
    print("The value of c2 is :", modc2, "mod", p)
    c3 = pow(modc1, -x, p)
    print("The value of revModulo is:", c3)
    m2 = pow(modc2 * c3, 1, p)  # decrypted message
    print("The value of decrypted message is :", m2)

    # p = 107
    # g = 2
    # x = 67
    # m = 13
    # r = 45

    p = 257
    g = 2585
    x = 47
    message = '7'
    m = int(message)
    r = 65
    print("The message is", m)
    # to compute y= g^x = 2585^47(mod 2879) = 2826(mod 2879)

    mody = pow(g, x, p)  # a=2585,b=47
    # print("y= g^x is %d mod %d\n",mody,p);
    modc11 = pow(g, r, p)
    print("The value of c1 is :", modc11, "mod", p)
    modc22 = pow(m*pow(mody, r, p), 1, p)
    print("The value of c2 is :", modc22, "mod", p)
    c3 = pow(modc11, -x, p)
    print("The value of revModulo is:", c3)
    m2 = pow(modc22 * c3, 1, p)  # decrypted message
    print("The value of decrypted message is :", m2)

    # Multiplication
    t1 = time.time()
    c1mult = pow(modc1*modc11, 1, p)
    c2mult = pow(modc2*modc22, 1, p)
    print("The result of multiplication are:")
    print("The value of c1mult is :", c1mult, "mod", p)
    print("The value of c2mult is :", c2mult, "mod", p)
    c3 = pow(c1mult, -x, p)
    print("The value of revModulo is:", c3)
    m2 = pow(c2mult * c3, 1, p)  # decrypted message
    print("The value of decrypted message is :", m2)

    t2 = time.time()
    time_taken = t2 - t1
    print("The tasks took", time_taken, "seconds to execute")