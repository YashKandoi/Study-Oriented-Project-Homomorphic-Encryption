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
    This code helps in image processing and converts image into an encrypted image and back into decrypted image. 

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

# 5. code_2.py
# Code Documentation: Image Encryption and Decryption with ElGamal

This document provides documentation for the provided Python code, which demonstrates image encryption and decryption using the ElGamal encryption scheme. The code utilizes various Python libraries and modules, including OpenCV, NumPy, and PIL (Python Imaging Library). Below is a detailed explanation of each section of the code:

### Importing Libraries and Modules
```python
import cv2
import math
import time
import random as rand
from random import *
import numpy as np
from PIL import Image
from array import *
import elgamal as elg
import functions as fe
```
- The code begins by importing necessary Python libraries and modules. These libraries include OpenCV for image manipulation, NumPy for numerical operations, PIL for image processing, and custom modules `elgamal` and `functions`.

### Main Function
```python
if __name__ == "__main__":
```
- The main code execution begins with this conditional block. It ensures that the following code runs only if the script is executed as the main program.

### Image Loading and Preparation
```python
    n = cv2.imread("i8.jpeg", cv2.IMREAD_GRAYSCALE)
    Row = len(n)
    Column = len(n[0])
```
- The code loads an image named "i8.jpeg" in grayscale using OpenCV (`cv2`). It then determines the number of rows and columns in the image.

### ElGamal Parameters and Image Block Size
```python
    p = 531872289054204184185084734375133399408303613982130856645299464930952178606045848877129147820387996428175564228204785846141207532462936339834139412401975338705794646595487324365194792822189473092273993580587964571659678084484152603881094176995594813302284232006001752128168901293560051833646881436219
    g = 2585
    x = 47
    r = 65
    size = 10
```
- These variables define the parameters for the ElGamal encryption scheme: `p` (prime modulus), `g` (generator), `x` (private key), and `r` (random number).
- `size` defines the block size for dividing the image.

### Padding and Dummy Image
```python
    newRow = math.ceil(Row / 10) * 10
    newColumn = math.ceil(Column / 10) * 10
```
- The code calculates the new dimensions for the image by rounding up the number of rows and columns to the nearest multiple of 10. This ensures that the image can be divided into blocks evenly.
```python
    np.save('code2_dummy.npy', n)
    dummy_matrix = np.load('code2_dummy.npy')
    dum = Image.fromarray(dummy_matrix, "L")
    dum.save('code2_dummy.png')
```
- The code saves the original image data to a numpy array file ('code2_dummy.npy') and then loads it back into a dummy matrix. It also saves the dummy matrix as 'code2_dummy.png'.

### Filling Data and Block Concatenation
```python
    newMatrix = np.zeros((newRow, newColumn), dtype=int)
```
- A new matrix (`newMatrix`) is created with the dimensions of the padded image, initialized with zeros.
```python
    for row in range(0, Row):
        for column in range(0, Column):
            newMatrix[row][column] = n[row][column]
```
- The original image data is copied into `newMatrix`.
```python
    for row in range(0, newRow):
        for column in range(0, newColumn):
            if row >= Row or column >= Column:
                newMatrix[row][column] = rand.randint(0, 255)
```
- The code pads `newMatrix` with random values where necessary to match the padded dimensions.
```python
    original_concat = []
    for row in range(0, newRow, size):
        for column in range(0, newColumn, size):
            original_con = fe.concatArr(newMatrix, row, column, size)
            original_concat.append(original_con)
```
- The code divides the padded image into blocks of size `size x size` and concatenates them into a 1D list `original_concat`.

### Key Generation
```python
    t1 = time.time()
    mody = pow(g, x, p)
    t2 = time.time()
    time_taken = t2 - t1
    print("The key generation task took", time_taken, "seconds to execute")
```
- The ElGamal public key (`mody`) is generated using the private key `x` and other parameters. The execution time is measured and printed.

### Encryption
```python
    modc11 = []
    modc1 = pow(g, r, p)
    c3 = 0
    c3 = pow(modc1, -x, p)
    enc_concat = []
    t1 = time.time()
```
- The code initializes variables for encryption, including `modc11`, `modc1`, and `c3`. Encryption of the image blocks will take place in the following section.
```python
    for row in range(len(original_concat)):
        r = randint(1, 349-2)
        modc2 = pow(g, r, p)
        enc_con = pow((original_concat[row]+1)*pow(mody, r, p), 1, p)
        enc_concat.append(enc_con)
        modc11.append(modc2)
```
- The code encrypts each block in `original_concat` using ElGamal encryption and appends the encrypted block to `enc_concat`. `modc11` stores intermediate values used in decryption.
```python
    t2 = time.time()
    time_taken = t2 - t1
    print("The encryption tasks took", time_taken, "seconds to execute")
```
- The execution time for the encryption process is measured and printed.

### Matrix Conversion and Normalization
```python
    matrices = fe.convertListToMatrix(newRow, newColumn, size, enc_concat)
    matrix_nxn = [[0 for _ in range(newColumn)] for _ in range(newRow)]
    matrix_nxn = fe.convert_to_matrix(
        matrices, size, len(matrix_nxn), len(matrix_nxn[0]))
    matrix_nxn = np.array(matrix_nxn)
    a_min = np.min(matrix_nxn)
    a_max = np.max(matrix_nxn)
    matrix_nxn = (((matrix_nxn - a_min) * 255) /
                  (a_max - a_min)).astype(np.uint8)
```
- The code converts the 1D list `enc_concat` into a 2D matrix `matrix_nxn`, where each block is represented as a submatrix.
- The matrix is then normalized to the range [0, 255] for image display.

### Saving Encrypted Image
```python
    enc = n
    for row in range(Row):
        for column in range(Column):
            enc[row][column] = matrix_nxn[row][column]
    np.save('code2_image1_enc

rypted.npy', enc)
    encrypted_matrix = np.load('code2_image1_encrypted.npy')
    encrypted_image = Image.fromarray(encrypted_matrix, "L")
    encrypted_image.save('code2_encrypted_image.png')
```
- The code replaces the original image data with the encrypted data in `enc` and saves it as 'code2_image1_encrypted.npy' and 'code2_encrypted_image.png'.

### Decryption
```python
    dec_concat = []
    t1 = time.time()
```
- The code initializes a list `dec_concat` to store the decrypted blocks and measures the start time for decryption.

### Block Decryption
```python
    for row in range(len(enc_concat)):
        c3 = pow(modc11[row], -x, p)
        value = enc_concat[row]
        dec_con = pow(value * c3, 1, p)-1
        dec_concat.append(dec_con)
```
- The code decrypts each block in `enc_concat` using the ElGamal decryption process and appends the decrypted block to `dec_concat`.
```python
    t2 = time.time()
    time_taken = t2 - t1
    print("The decryption tasks took", time_taken, "seconds to execute")
```
- The execution time for the decryption process is measured and printed.

### Converting to Matrix Form and Saving Decrypted Image
```python
    matrices = fe.convertListToMatrix(newRow, newColumn, size, dec_concat)
    matrix_nxn = [[0 for _ in range(newColumn)] for _ in range(newRow)]
    matrix_nxn = fe.convert_to_matrix(
        matrices, size, len(matrix_nxn), len(matrix_nxn[0]))
    matrix_nxn = np.array(matrix_nxn)
    dec = n
    for row in range(Row):
        for column in range(Column):
            dec[row][column] = matrix_nxn[row][column]
    np.save('code2_image1_decrypted.npy', dec)
    decrypted_matrix = np.load('code2_image1_decrypted.npy')
    decrypted_image = Image.fromarray(decrypted_matrix, "L")
    decrypted_image.save('code2_decrypted_image.png')
```
- The code converts the list of decrypted blocks back into matrix form and then replaces the original image data with the decrypted data in `dec`.
- The decrypted image is saved as 'code2_image1_decrypted.npy' and 'code2_decrypted_image.png'.

This code demonstrates the encryption and decryption of an image using the ElGamal encryption scheme and provides detailed comments to explain each step.