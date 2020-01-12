def getlist(keys,val,num):
    listname = ["","","","","","","","","",""]
    Data = {keys:val}
    if listname[num] == "":
        listname[num]=Data
    else:
        count = -1
        for i in listname:
            count+= 1
            if i == "":
                listname[count] = Data
                break
    return listname
def xhash(Keys):
    index = hash(Keys)%10
    if index >= 10 :
        index = index % 10
    print(index)
    return index
listname = ["","","","","","","","","",""]
yes = "Y"
while yes.upper() == "Y":
    print("1.INPUT")
    print("2.SEARCH")
    print("3.EXIT")
    enter = input("Enter number: ")
    if enter == "1":
        yes1 = "Y"
        while yes1.upper() == "Y":
            if "" not in listname:
                print("List Full.")
                yes1 ="N"
            keys = input("Enter your name :")
            val = input("Student ID :")
            num = xhash(keys)
            getlist(keys,val,num)
            yes1 = input("Do you want to input again? (Y or N): ")
    elif enter == '2':
        yes2= "Y"
        while yes2.upper() == 'Y':
            keys = input('Enter your name :')
            num = xhash(keys)
            if keys in listname[num]:
                print("This is Student ID:",listname[num].get(keys))
            else:
                for i in listname:
                    if keys in i:
                        print("This is Student ID",i.get(keys))
                        break
            yes2 = input("Do you want to search again? (Y or N): ")
    else:
        yes = "N"