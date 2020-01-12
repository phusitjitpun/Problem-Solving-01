namelist = ["","","","","","","","","",""]
datarun = "Y"
def get_in_the_list(keys,val,num):
    global namelist
    Data = {keys:val}
    if namelist[num] == "":
        namelist[num]=Data
    else:
        count = -1
        for i in namelist:
            count+= 1
            if i == "":
                namelist[count] = Data
                break
    return namelist
def nathash(Keys):
    numindex = hash(Keys)%10
    if numindex >= 10 :
        numindex = numindex % 10
    print(numindex)
    return numindex
while datarun == "Y":
    print("1.INPUT")
    print("2.SEARCH")
    print("3.EXIT")
    enter = input("Enter number(1,2 or 3): ")
    if enter == "1":
        doit = "Y"
        while doit == "Y":
            if "" not in namelist:
                print("FULL LIST SORRY T-T")
                doit ="N"
            keys = input("Enter your name :")
            val = input("number ID :")
            num = nathash(keys)
            get_in_the_list(keys,val,num)
            doit = input("want more(Y = Yes,N = No)")
    elif enter == '2':
        doit2= "Y"
        while doit2 == 'Y':
            keys = input('Enter your name :')
            num = nathash(keys)
            if keys in namelist[num]:
                print("This is your ID:",namelist[num].get(keys))
            else:
                for i in namelist:
                    if keys in i:
                        print("This is your ID",i.get(keys))
                        break
            doit2 = input("want more(Y = Yes,N = No): ")
    else:
        datarun = "N"
        
                






    

