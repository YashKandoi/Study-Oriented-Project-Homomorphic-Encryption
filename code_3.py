import cv2
import math
import time
import random as rand
import numpy as np
from PIL import Image
from array import *
import elgamal as elg
import functions as fe
from random import *

if __name__ == "__main__":

    n = cv2.imread("img_color3.jpg")
    n = cv2.cvtColor(n, cv2.COLOR_BGR2RGB)
    Row = n.shape[0]
    Column = n.shape[1]

    matrix = []
    print("The program starts ")
    print('Image Dimensions :', n.shape)
    n_blue = n[:, :, 0]
    n_green = n[:, :, 1]
    n_red = n[:, :, 2]
    p = 531872289054204184185084734375133399408303613982130856645299464930952178606045848877129147820387996428175564228204785846141207532462936339834139412401975338705794646595487324365194792822189473092273993580587964571659678084484152603881094176995594813302284232006001752128168901293560051833646881436219
    g = 2585
    x = 47
    r = 65
# defines the size of the block (size*size)
    size = 5

# rounds up the number to the nearest sizeth block
    newRow = math.ceil(Row / size) * size
    newColumn = math.ceil(Column / size) * size

    print("The new size of image is ", newRow, "X", newColumn, " pixels")

# Dummy

    np.save('code3_dummy.npy', n)
    dummy_matrix = np.load('code3_dummy.npy')
    dum = Image.fromarray(dummy_matrix, "RGB")
    dum.save('code3_dummy.png')

# original matrix
    # print(n)

# filling data into the newMatrix plus padding it with random numbers
    newMatrix_blue = np.zeros((newRow, newColumn), dtype=int)
    newMatrix_green = np.zeros((newRow, newColumn), dtype=int)
    newMatrix_red = np.zeros((newRow, newColumn), dtype=int)
    for row in range(0, Row):
        for column in range(0, Column):
            newMatrix_blue[row][column] = n_blue[row][column]
            newMatrix_green[row][column] = n_green[row][column]
            newMatrix_red[row][column] = n_red[row][column]

    for row in range(0, newRow):
        for column in range(0, newColumn):
            if row >= Row or column >= Column:
                newMatrix_blue[row][column] = rand.randint(0, 255)
                newMatrix_green[row][column] = rand.randint(0, 255)
                newMatrix_red[row][column] = rand.randint(0, 255)

    # print(newMatrix)


# preparing the original array concatenation
    original_concat_blue = []
    original_concat_green = []
    original_concat_red = []
    for row in range(0, newRow, size):
        for column in range(0, newColumn, size):
            original_con = fe.concatArr(newMatrix_blue, row, column, size)
            original_concat_blue.append(original_con)
            original_con = fe.concatArr(newMatrix_green, row, column, size)
            original_concat_green.append(original_con)
            original_con = fe.concatArr(newMatrix_red, row, column, size)
            original_concat_red.append(original_con)
    # print("The original array concated form is:")
    # print(original_concat)

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
    modc11_blue = []
    modc11_green = []
    modc11_red = []
    modc1 = pow(g, r, p)
    c3 = 0
    c3 = pow(modc1, -x, p)
    enc_concat_blue = []
    enc_concat_green = []
    enc_concat_red = []
    t1 = time.time()

# encrypting the block matrix
    for row in range(len(original_concat_blue)):
        r = randint(1, 349-2)
        modc2 = pow(g, r, p)
        enc_con = pow((original_concat_blue[row]+1)*pow(mody, r, p), 1, p)
        enc_concat_blue.append(enc_con)
        modc11_blue.append(modc2)

    for row in range(len(original_concat_green)):
        r = randint(1, 349-2)
        modc2 = pow(g, r, p)
        enc_con = pow((original_concat_green[row]+1)*pow(mody, r, p), 1, p)
        enc_concat_green.append(enc_con)
        modc11_green.append(modc2)

    for row in range(len(original_concat_red)):
        r = randint(1, 349-2)
        modc2 = pow(g, r, p)
        enc_con = pow((original_concat_red[row]+1)*pow(mody, r, p), 1, p)
        enc_concat_red.append(enc_con)
        modc11_red.append(modc2)

    t2 = time.time()
    time_taken = t2 - t1
    print("The encryption tasks took", time_taken, "seconds to execute")

    # print("The encrypted array concated form is:")
    # print(enc_concat)


# putting encrypted block to matrix form
    print("Encrypting a")
    matrices = fe.convertListToMatrix(newRow, newColumn, size, enc_concat_blue)
    print("Encrpting a.1")
    matrix_nxn_blue = [[0 for _ in range(newColumn)] for _ in range(newRow)]
    print("Encrpting a.2")
    matrix_nxn_blue = fe.convert_to_matrix(
        matrices, size, len(matrix_nxn_blue), len(matrix_nxn_blue[0]))
    print("Encrpting a.3")
    matrix_nxn_blue = np.array(matrix_nxn_blue)
    print("Encrpting a.4")

    matrices = fe.convertListToMatrix(newRow, newColumn, size, enc_concat_green)
    matrix_nxn_green = [[0 for _ in range(newColumn)] for _ in range(newRow)]
    matrix_nxn_green = fe.convert_to_matrix(matrices, size, len(
        matrix_nxn_green), len(matrix_nxn_green[0]))
    matrix_nxn_green = np.array(matrix_nxn_green)

    matrices = fe.convertListToMatrix(newRow, newColumn, size, enc_concat_red)
    matrix_nxn_red = [[0 for _ in range(newColumn)] for _ in range(newRow)]
    matrix_nxn_red = fe.convert_to_matrix(
        matrices, size, len(matrix_nxn_red), len(matrix_nxn_red[0]))
    matrix_nxn_red = np.array(matrix_nxn_red)

# normalizing the matrix
    print("Encrpting b")
    a_min = np.min(matrix_nxn_blue)
    a_max = np.max(matrix_nxn_blue)
    matrix_nxn_blue = (((matrix_nxn_blue - a_min) * 255) /
                       (a_max - a_min)).astype(np.uint8)

    a_min = np.min(matrix_nxn_green)
    a_max = np.max(matrix_nxn_green)
    matrix_nxn_green = (((matrix_nxn_green - a_min) * 255) /
                        (a_max - a_min)).astype(np.uint8)

    a_min = np.min(matrix_nxn_red)
    a_max = np.max(matrix_nxn_red)
    matrix_nxn_red = (((matrix_nxn_red - a_min) * 255) /
                      (a_max - a_min)).astype(np.uint8)

    print("Encrpting c")
    enc_blue = n_blue
    for row in range(Row):
        for column in range(Column):
            enc_blue[row][column] = matrix_nxn_blue[row][column]

    enc_green = n_green
    for row in range(Row):
        for column in range(Column):
            enc_green[row][column] = matrix_nxn_green[row][column]

    enc_red = n_red
    for row in range(Row):
        for column in range(Column):
            enc_red[row][column] = matrix_nxn_red[row][column]

    enc = cv2.merge([enc_blue, enc_green, enc_red])

# saving the encrypted image
    print("Encrpting d")
    np.save('code3_image1_encrypted.npy', enc)
    encrypted_matrix = np.load('code3_image1_encrypted.npy')
    encrypted_image = Image.fromarray(encrypted_matrix, "RGB")
    encrypted_image.save('code3_encrypted_image.png')

# ---------------------------------------------------------------------------------
# Decrypting the concatenated matrix

    # dec_concat=np.zeros(len(enc_concat))
    dec_concat_blue = []
    dec_concat_green = []
    dec_concat_red = []
    t1 = time.time()

# block decryption
    print("DEcrypting a")
    for row in range(len(enc_concat_blue)):
        # print("Thevalue of rev pow is:",c3)
        c3 = pow(modc11_blue[row], -x, p)
        value = enc_concat_blue[row]
        dec_con = pow(value * c3, 1, p)-1
        dec_concat_blue.append(dec_con)

    for row in range(len(enc_concat_green)):
        # print("Thevalue of rev pow is:",c3)
        c3 = pow(modc11_green[row], -x, p)
        value = enc_concat_green[row]
        dec_con = pow(value * c3, 1, p)-1
        dec_concat_green.append(dec_con)

    for row in range(len(enc_concat_red)):
        # print("Thevalue of rev pow is:",c3)
        c3 = pow(modc11_red[row], -x, p)
        value = enc_concat_red[row]
        dec_con = pow(value * c3, 1, p)-1
        dec_concat_red.append(dec_con)

    # print("The decrypted array concated form is:")
    # print(dec_concat)

# ---------------------------------------------------------------------------------
# to convert from list form to matrix form
    print("DEcrypting b")
    matrices = fe.convertListToMatrix(newRow, newColumn, size, dec_concat_blue)
    matrix_nxn_blue = [[0 for _ in range(newColumn)] for _ in range(newRow)]
    matrix_nxn_blue = fe.convert_to_matrix(
        matrices, size, len(matrix_nxn_blue), len(matrix_nxn_blue[0]))
    matrix_nxn_blue = np.array(matrix_nxn_blue)

    matrices = fe.convertListToMatrix(newRow, newColumn, size, dec_concat_green)
    matrix_nxn_green = [[0 for _ in range(newColumn)] for _ in range(newRow)]
    matrix_nxn_green = fe.convert_to_matrix(matrices, size, len(
        matrix_nxn_green), len(matrix_nxn_green[0]))
    matrix_nxn_green = np.array(matrix_nxn_green)

    matrices = fe.convertListToMatrix(newRow, newColumn, size, dec_concat_red)
    matrix_nxn_red = [[0 for _ in range(newColumn)] for _ in range(newRow)]
    matrix_nxn_red = fe.convert_to_matrix(
        matrices, size, len(matrix_nxn_red), len(matrix_nxn_red[0]))
    matrix_nxn_red = np.array(matrix_nxn_red)

    t2 = time.time()
    time_taken = t2 - t1
    print("The decryption tasks took", time_taken, "seconds to execute")

    print("DEcrypting c")
    dec_blue = n_blue
    dec_green = n_green
    dec_red = n_red
    for row in range(Row):
        for column in range(Column):
            dec_blue[row][column] = matrix_nxn_blue[row][column]
            dec_green[row][column] = matrix_nxn_green[row][column]
            dec_red[row][column] = matrix_nxn_red[row][column]

    dec = cv2.merge([dec_blue, dec_green, dec_red])

    # print(dec)
    np.save('code3_image1_decrypted.npy', dec)
    decrypted_matrix = np.load('code3_image1_decrypted.npy')
    decrypted_image = Image.fromarray(decrypted_matrix, "RGB")
    decrypted_image.save('code3_decrypted_image.png')
