# Study-Oriented-Project-Homomorphic-Encryption

# 1. Elgamal.py
    This document provides detailed documentation for the code implementation for Elgamal algorithm used for encryption. The code is designed to demonstrate a basic cryptographic scheme involving key generation, encryption, and decryption. It uses modular arithmetic to perform these operations.

    This Python code demonstrates a basic cryptographic scheme using modular arithmetic. It involves key generation, encryption, and decryption. The code uses predefined values for p, g, x, and a sample message 'message'.

    The code is structured into several sections:

    1. Key generation
    2. Encryption
    3. Decryption

    **a. Variables**

    p: A prime number
    g: A base value
    x: A secret exponent
    message: The message to be encrypted
    m: An integer representation of the message
    r: A random value
    t1, t2: Time variables to measure execution time
    mody: The result of g^x mod p or y=g^x
    modc1: The result of g^r mod p or c1=g^r
    modc2: The result of ((m+1) * (mody^r)) mod p or (s=y^r and c2=m*s)
    c3: The result of modc1^-x mod p or (t=c^x and c3=t^-1)
    m2: The decrypted message or (m2= c2 * t^-1)

   **b. General Instructions**
        i.(g,y) is used as public key.
        ii.x is a private key and must be kept secret.
        iii. Values of p,g,x and r can be changed as per the user requirement.

    **c. Output**
        The program starts 
        The value of r is:  65
        The message is 105
        The value of y is : 137 mod 257
        The tasks took 1.0013580322265625e-05 seconds to execute
        The length of modc1 is: 2
        The value of c1 is : 15 mod 257
        The value of c2 is : 130 mod 257
        The length of modc2 is: 3
        The tasks took 2.7894973754882812e-05 seconds to execute
        The value of revModulo is: 242
        The value of decrypted message is : 105
        The tasks took 1.0013580322265625e-05 seconds to execute

# 2. Function uses for functions defined in functions.py
    * def concatArr(arr, i, j, size):
    * def digits(num): returns number of digits
    * def zero_num(size,number): 
    * def convert_to_matrix(matrices,size,newRow,newColumn):
    * def convertListToMatrix(newRow,newColumn,size,list):
