#MATRIX CALCULATOR by sina honarvar (https://github.com/aqaSina)

import numpy as np
import random as rnd

#Functiom for matrix oprations & menu : 
def matops (mat1 , mat2):
    global uoc

    print("\n ====== OK now heres the MENU of matrix operations ======")
    print("-----")
    print("0 : display both matrices")
    print("1 : multiply (element-wise)")
    print("2 : multiply (matrix multiplication)")
    print("3 : sum of matrixes")
    print("4 : subtraction of matrices (mat1 - mat2)")
    print("5 : division of matrices(mat1 / mat2 _ element-wise)")
    print("write anything letter to : BREAK")

    uoc = int(input("choose the operation u want to do : "))
    if uoc == 0: 
        print(f"mat 1 : \n {mat1}")
        print(f"mat 2 : \n {mat2}")
        input("press ENTER to continue")
    elif uoc == 1:
        print(f" mat 1 * mat 2 (element-wise) = \n {mat1*mat2}")
        input("press ENTER to continue")
    elif uoc == 2:
        print(f" mat 1 * mat 2 (MATRIX mult) = \n {mat1@mat2}")
        input("press ENTER to continue")
    elif uoc == 3:
        print(f" mat 1 + mat 2 = \n {mat1+mat2}")
        input("press ENTER to continue")
    elif uoc == 4:
        print(f" mat 1 - mat 2 = \n {mat1-mat2}")
        input("press ENTER to continue")
    elif uoc == 5:
        print(f" mat 1 / mat 2 = \n {mat1/mat2}")
        input("press ENTER to continue")
    else:
        print("hope u liked it.")
        

# function for using random matrices
def rndmat():
    rmat1 = np.array([[rnd.randint(1,100),rnd.randint(1,100)],[rnd.randint(1,100),rnd.randint(1,100)]])
    rmat2 = np.array([[rnd.randint(1,100),rnd.randint(1,100)],[rnd.randint(1,100),rnd.randint(1,100)]])
    print(f"random mat 1 : \n {rmat1}")
    print(f"random mat 2 : \n {rmat2}")
    input("press ENTER to continue")
    while True:
        matops(rmat1,rmat2)
        if uoc == 666:
            break

# funtion for getting user matrix number 1 (user input matrix 1)
def uimat1():
    global umat1
    print("\n OK THEN.Enter ur FIRST MAT(only (2,2) MATs supported!): \n")
    r0c0m1 = int(input("enter a num for FIRST MATRIX in position(R=0,C=0) : "))
    r0c1m1 = int(input("enter a num for FIRST MATRIX in position(R=0,C=1) : "))
    r1c0m1 = int(input("enter a num for FIRST MATRIX in position(R=1,C=0) : "))
    r1c1m1 = int(input("enter a num for FIRST MATRIX in position(R=1,C=1) : "))
    umat1 = np.array([[r0c0m1,r0c1m1],[r1c0m1,r1c1m1]])
    print(f"\n ur first MATRIX: \n {umat1}")
    print("-"*10)
    return umat1

# function for editing user matrix number 1 
def mat1edit():
    global umat1
    print("\n OK THEN.Enter ur FIRST MAT to EDIT(only (2,2) MATs supported!): \n")
    r0c0m1 = int(input("enter a num to EDIT FIRST MATRIX in position(R=0,C=0) : "))
    r0c1m1 = int(input("enter a num to EDIT FIRST MATRIX in position(R=0,C=1) : "))
    r1c0m1 = int(input("enter a num to EDIT FIRST MATRIX in position(R=1,C=0) : "))
    r1c1m1 = int(input("enter a num to EDIT FIRST MATRIX in position(R=1,C=1) : "))
    umat1 = np.array([[r0c0m1,r0c1m1],[r1c0m1,r1c1m1]])
    print(f"\n ur first MATRIX(EDITED): \n {umat1}")
    return umat1

# funtion for getting user matrix number 2 (user input matrix 2)
def uimat2():
    global umat2
    print("\n Well.Enter ur SECOND MAT(only (2,2) MATs supported!): \n")
    r0c0m2 = int(input("enter a num for SECOND MATRIX in position(R=0,C=0) : "))
    r0c1m2 = int(input("enter a num for SECOND MATRIX in position(R=0,C=1) : "))
    r1c0m2 = int(input("enter a num for SECOND MATRIX in position(R=1,C=0) : "))
    r1c1m2 = int(input("enter a num for SECOND MATRIX in position(R=1,C=1) : "))
    umat2 = np.array([[r0c0m2,r0c1m2],[r1c0m2,r1c1m2]])
    print(f"\n ur second MATRIX: \n {umat2}")
    return umat2

# function for editing user matrix number 2 
def mat2edit():
    global umat2
    print("\n Enter ur first MAT to EDIT(only (2,2) MATs supported!): \n ")
    r0c0m2 = int(input("enter a num to EDIT SECOND MATRIX in position(R=0,C=0) : "))
    r0c1m2 = int(input("enter a num to EDIT SECOND MATRIX in position(R=0,C=1) : "))
    r1c0m2 = int(input("enter a num to EDIT SECOND MATRIX in position(R=1,C=0) : "))
    r1c1m2 = int(input("enter a num to EDIT SECOND MATRIX in position(R=1,C=1) : "))
    umat2 = np.array([[r0c0m2,r0c1m2],[r1c0m2,r1c1m2]])
    print(f"\n ur second MATRIX(EDITED): \n {umat2}")
    return umat2

# function to start the programm with just matrix 1 edited (lvl 1/4)
def start_m1_edited():
    print(f"\n ur first MATRIX(EDITED): \n {umat1}")
    print(f"\n ur second MATRIX: \n {umat2}")
    input("press ENTER to continue")
    while True:
        matops(umat1,umat2)
        if uoc == 666:
            break

# function to start the programm with no matrix edited (lvl 2/4)
def start_no_edited():
    print(f"\n ur first MATRIX: \n {umat1}")
    print(f"\n ur second MATRIX: \n {umat2}")
    input("press ENTER to continue")
    while True:
        matops(umat1,umat2)
        if uoc == 666:
            break    
            

# function to start the programm with just matrix 2 edited (lvl 3/4)
def start_m2_edited():
    print(f"\n ur first MATRIX: \n {umat1}")
    print(f"\n ur second MATRIX(EDITED): \n {umat2}")
    input("press ENTER to continue")
    while True:
        matops(umat1,umat2)
        if uoc == 666:
            break

# function to start the programm with both matrices edited (lvl 4/4)
def start_both_edited():
    print(f"\n ur first MATRIX(EDITED): \n {umat1}")
    print(f"\n ur second MATRIX(EDITED): \n {umat2}")
    input("press ENTER to continue")
    while True:
        matops(umat1,umat2)
        if uoc == 666:
            break

# main function of matrix calculator
def matcal ():
    print("MATRIX calculator using numpy")

    uchoice = int(input("\n wanna input ur own MATRICES or wanna use random MATRICES? \n (1 : OWN MATs / 2 : RANDOM) : "))
    if uchoice == 1: #mat1 enter
        uimat1()
        uedit = int(input(f"\n everythings OK? \n (1 : ENTER SECOND MAT / 2 : EDIT FIRST MAT(u have to enter the whole MAT again)) : "))
        if uedit == 1: #mat1 no edit
            print("-"*10)
            uimat2() #mat2 enter
            uedit2 = int(input("\n OK u wanna edit or start calculating? \n (1 : START / 2 : EDIT SECOND MAT(u have to enter the whole MAT again)) : "))
            if uedit2 == 1: #mat1 _141 & mat2 _145 no edit (-1-)
                start_no_edited()
            elif uedit2 == 2: #mat1 no edit _141 / mat2 edited _150 (-2-)
                mat2edit()
                start_m2_edited()
            # ------------------------------
        elif uedit == 2: #mat1 edited _156
            mat1edit()
            uimat2()
            uedit2 = int(input("\n OK u wanna edit or start calculating? \n (1 : START / 2 : EDIT SECOND MAT(u have to enter the whole MAT again)) : "))
            if uedit2 == 1: #mat1 edited / mat2 no edit _157 (-3-)
                start_m1_edited()
            #--------------------------------            
            elif uedit2 == 2: #mat2 edited _165  / mat1 edited _156   (-4-)
                mat2edit()
                start_both_edited()

        else:
            print("wrong entry! runnin again")
            matcal()

    elif uchoice == 2:
        rndmat()

    else: 
        print(f"wrong entry! runnin again")
        matcal()

matcal()

