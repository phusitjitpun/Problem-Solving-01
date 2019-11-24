import time

def exV3(word):
    b = 0
    word1 = word.split()
    for i in word1:
        for x in i:
            a = ord(x)
            b += a
    return b
word = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
start = time.time()
print('answerV3: ', exV3(word))
print('timeV3: ', (time.time()-start)*1000)
