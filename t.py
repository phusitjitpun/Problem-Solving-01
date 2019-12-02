def main():
    infile = open('text.txt', 'r')
    cities = infile.read()
    infile.close()
    b = 0
    if cities == " ":
        pass
    elif cities == ".":
        pass
    else:
        b = len(cities)
        print(b)

#main()

def t():
    infile = open('text.txt', 'r')
    cities = infile.read()
    infile.close()
    t1 = len(cities.split('.'))
    t2 = len(cities.split(' '))
    t3 = 0
    if cities == " ":
        pass
    elif cities == ".":
        pass
    else:
        t3 = len(cities)
    t4 = t3 - (t2 - 1) - (t1 - 1)
    print(t1)
    print(t2)
    print(t3)
    print(t4)
#t()

def t1():
    infile = open('text.txt', 'r')
    cities = infile.read()
    infile.close()
    b = 0
    for i in cities:
        if i.isupper() == True:
            b += 1
    print(b)

t1()