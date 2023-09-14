# all functions

import cv2
import math
import time
from random import *
import numpy as np
from PIL import Image


def concatArr(arr, i, j, size):
    str_con = ""
    for row in range(i, i+size):
        for column in range(j, j+size):
            # checking whether 3-digit number or 2-digit number or 1-digit number and concatenating them with 0 in the beginning to make them 3-digit numbers
            if int(arr[row][column]/100) !=0:
                num_str = str(arr[row][column])
            elif int(arr[row][column]/100) ==0 and int(arr[row][column]/10) !=0:
                num_str = "0"+str(arr[row][column])
            else:
                num_str = "00"+str(arr[row][column])
            str_con = str_con + num_str
    return int(str_con)

def digits(num):
    count=0
    while(num!=0):
        num //= 10
        count += 1
    return count

def zero_num(size,number):
    s=size*size*3-1
    while s>0:
        number=number+'0'
        s-=1
    return number

def convert_to_matrix(matrices,size,newRow,newColumn):
    matrix_nxn = [[0 for _ in range(newColumn)] for _ in range(newRow)]
# Append the mini matrices to the empty matrix
    n = newRow-size
    m = newColumn-size
    p = 0
    q = 0
    k = 0
    while k < ((n//10)+1) * ((m//10)+1):
        for i in range(size):
            for j in range(size):
               matrix_nxn[p+i][q+j] = matrices[k][i][j]
        k += 1
        q += size
        if q > m:
            q = 0
            p += size

    # for k in range(len(matrices)):
    #     for i in range(size):
    #         for j in range(size):
    #             matrix_nxn[i+size*(k//int(newRow/size))][j+size*(k%int(newColumn/size))] = matrices[k][i][j]
    return matrix_nxn

def convertListToMatrix(newRow,newColumn,size,list):
    matrices=[]
    for count in range(int(newRow*newColumn/(size*size))):
        enc_blockMatrix=[]
        number=str(list[count])
        # print(number)
        while len(number)!=size*size*3:
            number='0'+number
        # print(number)
        counter=0
        for row in range(size):
            a=[]
            for column in range(size):
                x=counter*3
                mat_num=int(number[x:x+3])
                counter+=1
                a.append(mat_num)
            enc_blockMatrix.append(a)
        matrices.append(enc_blockMatrix)
    return matrices

# functions for paillier

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    lcm(a, b)

    returns Lowest Common Multiple of a and b
    """
    return (a * b) // gcd(a, b)

def multiplicative_inverse(a, modulus):
    """
    multiplicative_inverse(a, modulus)

    returns x: multiplicative inverse of a
    such that, a * x = 1 (mod modulus)
    """
    if math.gcd(a, modulus) != 1:
        raise Exception('modular inverse does not exist')
    else:
        return pow(a, -1, modulus)
