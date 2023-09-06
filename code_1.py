import cv2
import math
import time
from random import randint
import numpy as np
from PIL import Image

if __name__ == "__main__":
    n = cv2.imread("i3.jpeg", 0)
    Row = len(n)
    Column = len(n[0])
    matrix = []
    print("The program starts ")
    print("The size of the image is ", Row, "X", Column, " pixels")
    p = 349
    g = 2585
    x = 47
    r = 65

    # Dummy
    np.save('dummy.npy', n)
    dummy_matrix = np.load('dummy.npy')
    dum = Image.fromarray(dummy_matrix, "L")
    dum.save('code1_dummy.png')

    # Original matrix
    print(n)

    # Key generation
    t1 = time.time()
    mody = pow(g, x, p)  # a=2585,b=47
    t2 = time.time()
    time_taken = t2 - t1
    print("The key generation task took", time_taken, "seconds to execute")
    # Public key (p,g,mody)

    # Encryption
    modc11 = []
    modc1 = pow(g, r, p)
    enc = n.copy()
    enc1 = np.zeros((Row, Column), dtype=np.int64)
    t1 = time.time()
    # for loop matrix
    for row in range(Row):
        a = []
        b = []
        for column in range(Column):
            r = randint(1, p - 2)
            modc2 = pow(g, r, p)
            b1 = pow(int((n[row][column] + 1) * pow(mody, r, p)), 1, p)
            enc[row][column] = b1
            b.append(b1)
            a.append(modc2)
        modc11.append(a)
        enc1[row] = b

    t2 = time.time()
    time_taken = t2 - t1
    print("The encryption tasks took", time_taken, "seconds to execute")

    # Encrypted matrix
    # enc is just for representation (mod by 256 already done)
    # enc1 contains actual encrypted values
    # print(enc)
    enc1 = np.array(enc1)
    print(enc1)

    # Homomorphic multiplication
    num = 1
    Nmodc1 = pow(g, r, p)
    print("The value of c1 is :", Nmodc1, "mod", p)
    Nmodc2 = pow(num * pow(mody, r, p), 1, p)
    print("The value of c2 is :", Nmodc2, "mod", p)
    # Encrypted value of num is stored in Nmodc2
    for row in range(Row):
        for column in range(Column):
            modc11[row][column] = (Nmodc1 * modc11[row][column]) % p
            enc1[row][column] = (Nmodc2 * enc1[row][column]) % p

    # matrix2=np.array(matrix)
    # Encrypted matrix
    # print(matrix2)
    np.save('code_1_image1_encrypted.npy', enc)
    encrypted_matrix = np.load('code_1_image1_encrypted.npy')
    encrypted_image = Image.fromarray(encrypted_matrix, "L")
    encrypted_image.save('code_1encrypted_image.png')

    # Decryption

    # decrypt=[]
    # Row=len(matrix2)
    # Column=len(matrix2[0])
    dec = n.copy()

    t1 = time.time()
    # Loop
    for row in range(Row):
        # a=[]
        for column in range(Column):
            c3 = pow(modc11[row][column], -x, p)
            dec[row][column] = pow(int(enc1[row][column] * c3), 1, p) - num
        #     a.append(m2)
        # decrypt.append(a)

    t2 = time.time()
    time_taken = t2 - t1
    print("The decryption tasks took", time_taken, "seconds to execute")
    # Decrypt2=np.array(n)
    # Decrypted matrix
    print(dec)
    np.save('code_1_image1_decrypted.npy', dec)
    decrypted_matrix = np.load('code_1_image1_decrypted.npy')
    decrypted_image = Image.fromarray(decrypted_matrix, "L")
    decrypted_image.save('code_1_decrypted_image.png')
