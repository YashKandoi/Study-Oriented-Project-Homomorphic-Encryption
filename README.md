# Study-Oriented-Project-Homomorphic-Encryption
Please note that this code is for educational purposes and lacks security considerations for real-world cryptographic applications.

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

# 2. elgamal_Multiplication.py
    This has the added functionality of homomorphic multiplication to elgamal encryption.The code illustrates a basic cryptographic scheme involving key generation, encryption, decryption, and multiplication of encrypted values, all using modular arithmetic.  

    The code is structured into several sections:

    1. Key generation
    2. First Encryption and Decryption
    3. Second Encryption and Decryption
    4. Multiplication of Encrypted Values
    5. Decryption of the final value

    **a. Variables**

    p: A prime number 
    g: A base value 
    x: A secret exponent
    message: The message to be encrypted.
    m: integer representation of the message.
    r: A random value
    t1, t2: Time variables used for measuring execution time.
    c1mult: The result of modc1 * modc11 (encrypted values multiplication).
    c2mult: The result of modc2 * modc22 (encrypted values multiplication).

   **b. General Instructions**
        The values of p, g, x, and r can be changed as per user requirements.
        The code demonstrates the ElGamal encryption process for two different messages, and the results are multiplied.

    **c. Output**
        The program starts 
        The message is 11
        The value of c1 is : 15 mod 257
        The value of c2 is : 222 mod 257
        The value of revModulo is: 242
        The value of decrypted message is : 11
        The message is 7
        The value of c1 is : 15 mod 257
        The value of c2 is : 188 mod 257
        The value of revModulo is: 242
        The value of decrypted message is : 7
        The result of multiplication are:
        The value of c1mult is : 225 mod 257
        The value of c2mult is : 102 mod 257
        The value of revModulo is: 225
        The value of decrypted message is : 77
        The tasks took 2.0265579223632812e-05 seconds to execute

# 3. code_1.py
    

    c. Output
        The encryption tasks took 0.036595821380615234 seconds to execute
        [[169 315 177 ... 239 103 226]
        [346  86  23 ...  39 279 178]
        [ 79 221 302 ... 337 183 216]
        ...
        [ 29 308  11 ...  51 174 260]
        [160 316 315 ... 177 344 268]
        [218  73 270 ...  19 327 292]]
        The value of c1 is : 269 mod 349
        The value of c2 is : 31 mod 349
        The decryption tasks took 0.00875401496887207 seconds to execute
        [[218 219 219 ... 209 212 213]
        [218 218 218 ... 217 205 204]
        [217 217 217 ... 206 217 220]
        ...
        [142 152 164 ... 115 118 119]
        [151 153 176 ... 118 121 121]
        [153 167 185 ... 123 124 121]]



# 4. Function uses for functions defined in functions.py
    * def concatArr(arr, i, j, size):
    * def digits(num): returns number of digits
    * def zero_num(size,number): 
    * def convert_to_matrix(matrices,size,newRow,newColumn):
    * def convertListToMatrix(newRow,newColumn,size,list):
