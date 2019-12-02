def main():
    line()
    sentence()
    word()
    letter()
    character_upper()
    character_lower()
    special_alphabet()
def line():
    infile = open('text.txt', 'r')
    line = infile.readlines()
    infile.close()
    print('Total line:', len(line))

def sentence():
    infile = open('text.txt', 'r')
    file_contents = infile.read()
    infile.close()
    sentence = file_contents.split('.')
    print('Total sentence:', len(sentence)-1)
    
def word():
    infile = open('text.txt', 'r')
    file_contents = infile.read()
    infile.close()  
    word = 0
    word += len(file_contents.split())
    print('Total word:', word)

def letter():
    infile = open('text.txt', 'r')
    file_contents = infile.read()
    infile.close()
    letter1 = 0
    for i in file_contents:
        if i.isalpha() == True:
            letter1 += 1
    print('Total leter:', letter1)

def character_upper():
    infile = open('text.txt', 'r')
    file_contents = infile.read()
    infile.close()
    upper = 0
    for i in file_contents:
        if i.isupper() == True:
            upper += 1
    print('Total chalacter upper:', upper)

def character_lower():
    infile = open('text.txt', 'r')
    file_contents = infile.read()
    infile.close()
    lower = 0
    for i in file_contents:
        if i.islower() == True:
            lower += 1
    print('Total character lower:', lower)

def special_alphabet():
    infile = open('text.txt', 'r')
    file_contents = infile.read()
    infile.close()
    special = 0
    for i in file_contents:
        if i == "," or i == "/" or i == "(" or i == ")":
            special += 1
    print('Total special alpdabet:', special)

main()