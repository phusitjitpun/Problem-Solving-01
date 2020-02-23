L = ['A','B','C','D','E','F']
a = len(L)
y = 'Y'

A = []

J = int(input('Enter Number : '))

while len(L) != 1 :
    I = J - 1
    while I >= len(L) :
        if I >= len(L) :
            I = I - len(L)
    k = L.index(L[I])
    L.remove(L[I])
    for i in range (k,len(L)) :
        A.append(L[i])
    for i in range (0,k) :
        A.append(L[i])
    print(A)
    L = A
    A = []

'''while len(L) != 1 :
    I = J - 1
    if a == len(L) :
        while I >= len(L) :
            if I >= len(L) :
                I = I - len(L)
        print(L[I])
        k = L.index(L[I]) 
        L.remove(L[I])
        print(I)
        print(L)
    else :
        if k == 0 :
            pass
        else :
            I = J + k - 1
        while I >= len(L) :
            if I >= len(L) :
                I = I - len(L)
        print(I)
        print(L[I])
        k = L.index(L[I])
        L.remove(L[I])
        print(I)
        print(L)'''