import math
import time
from functions import *

if __name__ == "__main__":
    
    print("The program starts ")
    p = 531872289054204184185084734375133399408303613982130856645299464930952178606045848877129147820387996428175564228204785846141207532462936339834139412401975338705794646595487324365194792822189473092273993580587964571659678084484152603881094176995594813302284232006001752128168901293560051833646881436219
    g = 2585
    x = 47
    message = '218219219219219218218217217217218218218218218217217216216216217217217217217217216216216216217217217217217216216216216216217217217218217217216216216216217217217217217217216216216216216216216217216216215215216216215215216216216215214214215215215215215215215215216216212214215215215215215215216216212213'
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

    p = 531872289054204184185084734375133399408303613982130856645299464930952178606045848877129147820387996428175564228204785846141207532462936339834139412401975338705794646595487324365194792822189473092273993580587964571659678084484152603881094176995594813302284232006001752128168901293560051833646881436219
    g = 2585
    x = 47
    message = '2'
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