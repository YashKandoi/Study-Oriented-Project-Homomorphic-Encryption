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


if __name__ == "__main__":

    n = cv2.imread("i3.jpeg", cv2.IMREAD_GRAYSCALE)
    Row = len(n)
    Column = len(n[0])

    print("The original matrix:")
    print(n)

    matrix = []
    print("The program starts ")
    print("The size of image is ", Row, "X", Column, " pixels")
    p = 531872289054204184185084734375133399408303613982130856645299464930952178606045848877129147820387996428175564228204785846141207532462936339834139412401975338705794646595487324365194792822189473092273993580587964571659678084484152603881094176995594813302284232006001752128168901293560051833646881436219
    g = 2585
    x = 47
    r = 65
# defines the size of the block (size*size)
    size = 10

# rounds up the number to the nearest 10
    newRow = math.ceil(Row / 10) * 10
    newColumn = math.ceil(Column / 10) * 10

    print("The new size of image is ", newRow, "X", newColumn, " pixels")

# Dummy
    np.save('code2_dummy.npy', n)
    dummy_matrix = np.load('code2_dummy.npy')
    dum = Image.fromarray(dummy_matrix, "L")
    dum.save('code2_dummy.png')

# filling data into the newMatrix plus padding it with random numbers
    newMatrix = np.zeros((newRow, newColumn), dtype=int)
    for row in range(0, Row):
        for column in range(0, Column):
            newMatrix[row][column] = n[row][column]

    for row in range(Row, newRow):
        for column in range(Column, newColumn):
                newMatrix[row][column] = rand.randint(0, 255)


# preparing the original array concatenation
    original_concat = []
    for row in range(0, newRow, size):
        for column in range(0, newColumn, size):
            original_con = fe.concatArr(newMatrix, row, column, size)
            original_concat.append(original_con)

    print("The original array concated form is:")
    print(original_concat)
# ---------------------------------------------------------------------------------
# Key generation
    t1 = time.time()
    mody = pow(g, x, p)  # a=2585,b=47
    # print("The value of y is :", mody, "mod", p)
    t2 = time.time()
    time_taken = t2 - t1
    print("The key generation task took", time_taken, "seconds to execute")
    # Public key (p,g,mody)

# ---------------------------------------------------------------------------------
    # Encryption
    modc11 = []
    modc1 = pow(g, r, p)
    c3 = 0
    c3 = pow(modc1, -x, p)
    enc_concat = []
    t1 = time.time()

# encrypting the block matrix
    for row in range(len(original_concat)):
        r = randint(1, 349-2)
        modc2 = pow(g, r, p)
        enc_con = pow((original_concat[row]+1)*pow(mody, r, p), 1, p)
        enc_concat.append(enc_con)
        modc11.append(modc2)

    t2 = time.time()
    time_taken = t2 - t1
    print("The encryption tasks took", time_taken, "seconds to execute")

    print("The encrypted array concated form is:")
    print(enc_concat)


# putting encrypted block to matrix form
    matrices = fe.convertListToMatrix(newRow, newColumn, size, enc_concat)
    # print(len(matrices))
    # print(matrices[0])
        # initializing the 2d matrix with 0
    matrix_nxn = [[0 for _ in range(newColumn)] for _ in range(newRow)]
    # print("The size of matrix_nxn is ", len(matrix_nxn), "X", len(matrix_nxn[0]), " pixels")
    # print(matrix_nxn[0])
    # print(len(matrix_nxn[0]))
    # print(len(matrices))
    # print(matrices[0])
        # Append the mini matrices to the new matrix (matrix_nxn)
    matrix_nxn = fe.convert_to_matrix(matrices, size, len(matrix_nxn), len(matrix_nxn[0]))
    # print(matrix_nxn)
    matrix_nxn = np.array(matrix_nxn)
    # print(matrix_nxn)

# normalizing the matrix
    a_min = np.min(matrix_nxn)
    a_max = np.max(matrix_nxn)
    matrix_nxn = (((matrix_nxn - a_min) * 255) /
                  (a_max - a_min)).astype(np.uint8)

    # print(matrix_nxn)
    enc = n
    for row in range(Row):
        for column in range(Column):
            enc[row][column] = matrix_nxn[row][column]

    np.save('code2_image1_encrypted.npy', enc)
    encrypted_matrix = np.load('code2_image1_encrypted.npy')
    encrypted_image = Image.fromarray(encrypted_matrix, "L")
    encrypted_image.save('code2_encrypted_image.png')

    print("Encrypted matrix is:")
    print(enc)

# ---------------------------------------------------------------------------------
# Decrypting the concatenated matrix

    # dec_concat=np.zeros(len(enc_concat))
    dec_concat = []
    t1 = time.time()

# block decryption

    for row in range(len(enc_concat)):
        # print("Thevalue of rev pow is:",c3)
        c3 = pow(modc11[row], -x, p)
        value = enc_concat[row]
        dec_con = pow(value * c3, 1, p)-1
        dec_concat.append(dec_con)

    print("The decrypted array concated form is:")
    print(dec_concat)


# ---------------------------------------------------------------------------------
# to convert from list form to matrix form
    matrices = fe.convertListToMatrix(newRow, newColumn, size, dec_concat)
    matrix_nxn = [[0 for _ in range(newColumn)] for _ in range(newRow)]
    matrix_nxn = fe.convert_to_matrix(
        matrices, size, len(matrix_nxn), len(matrix_nxn[0]))
    # print(matrix_nxn)
    matrix_nxn = np.array(matrix_nxn)

    # print(matrix_nxn)
    t2 = time.time()
    time_taken = t2 - t1
    print("The decryption tasks took", time_taken, "seconds to execute")

    dec = n
    # print(n)
    # print("The size of n is ", len(n[0]), "X", len(n), " pixels")
    for row in range(Row):
        for column in range(Column):
            dec[row][column] = matrix_nxn[row][column]

    # print(dec)
    np.save('code2_image1_decrypted.npy', dec)
    decrypted_matrix = np.load('code2_image1_decrypted.npy')
    decrypted_image = Image.fromarray(decrypted_matrix, "L")
    decrypted_image.save('code2_decrypted_image.png')
