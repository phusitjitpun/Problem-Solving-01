import time

def exV1(word):
    b = 0
    for i in word:
        if i == " ":
            b += 0
        elif i == "A":
            b += 65
        elif i == "B":
            b += 66
        elif i == "C":
            b += 67
        elif i == "D":
            b += 68
        elif i == "E":
            b += 69
        elif i == "F":
            b += 70
        elif i == "G":
            b += 71
        elif i == "H":
            b += 72
        elif i == "I":
            b += 73
        elif i == "J":
            b += 74
        elif i == "K":
            b += 75
        elif i == "L":
            b += 76
        elif i == "M":
            b += 77
        elif i == "N":
            b += 78
        elif i == "O":
            b += 79
        elif i == "P":
            b += 80
        elif i == "Q":
            b += 81
        elif i == "R":
            b += 82
        elif i == "S":
            b += 83
        elif i == "T":
            b += 84
        elif i == "U":
            b += 85
        elif i == "V":
            b += 86
        elif i == "W":
            b += 87
        elif i == "X":
            b += 88
        elif i == "Y":
            b += 89
        elif i == "Z":
            b += 90
    return b
word = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
start = time.time()
print('answerV1: ', exV1(word))
print('timeV1: ', (time.time()-start)*1000)
