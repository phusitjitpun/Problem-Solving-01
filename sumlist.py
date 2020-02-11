ListA = [8, 12, 24, 3, 16, 10, 41]
ListB = ['C', 'B', 'F', 'K', 'Y', 'Z', 'G']
ListC = []
suma = 0
sumb = 0
sumc = 0

for i in ListB:
    suma = sum(ListA)
    x = ord(i)
    sumb += x
    sumc = suma + sumb
for i in range(len(ListB)):
    ListC.append(ListA[i]+x[i])
print('Result Sum ListA: ', suma)
print('Result Sum ListB: ', sumb)
print('Resulr Sum ListC: ', sumc)
print('Result ListC: ', ListC)
print(type(ListA))