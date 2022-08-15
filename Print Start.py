def starAsc():
    a = eval(input("Enter Star count: "))
    strOutput = ""
    for i in range(0, a, 1):
        for j in range (0, i+1, 1):
            strOutput = strOutput+"*"
        strOutput = strOutput + "\n"
    print(strOutput)

def starDsc():
    a = eval(input("Enter Star count: "))
    strOutput = ""
    for i in range(0, a, 1):
        for j in range (0, a-i, 1):
            strOutput = strOutput+"*"
        strOutput = strOutput + "\n"
    print(strOutput)

def Pyramid():
    a = eval(input("Enter Star count: "))
    strOutput = ""
    for i in range(0, a, 1):
        for j in range (0, a-i, 1):
            strOutput = strOutput+" "
        for j in range (0, i, 1):
            strOutput = strOutput+"*"
        for j in range (0, i+1, 1):
            strOutput = strOutput+"*"
        strOutput = strOutput + "\n"
    print(strOutput)

def InvPyramid():
    a = eval(input("Enter Star count: "))
    strOutput = ""
    for i in range(0, a, 1):
        for j in range (0, i+1, 1):
            strOutput = strOutput+" "
        for j in range (0, a-i-1, 1):
            strOutput = strOutput+"*"
        for j in range (0, a-i, 1):
            strOutput = strOutput+"*"
        strOutput = strOutput + "\n"
    print(strOutput)

def Butterfly():
    a = eval(input("Enter Star count: "))
    strOutput = ""
    for i in range(0, a, 1):
        for j in range (0, a-i, 1):
            strOutput = strOutput+" "
        for j in range (0, i, 1):
            strOutput = strOutput+"*"
        for j in range (0, i+1, 1):
            strOutput = strOutput+"*"
        strOutput = strOutput + "\n"
    for i in range(0, a, 1):
        for j in range (0, i+1, 1):
            strOutput = strOutput+" "
        for j in range (0, a-i-1, 1):
            strOutput = strOutput+"*"
        for j in range (0, a-i, 1):
            strOutput = strOutput+"*"
        strOutput = strOutput + "\n"
    print(strOutput)
