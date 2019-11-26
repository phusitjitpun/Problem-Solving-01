principal = int(input("Enter Principal: "))
interest = float(input("Enter Interest Rate: "))
year = int(input("Enter Number Of Year: "))
time = int(input("Enter Compounding time: "))
amount = principal * ((1 + (interest/time)) ** (year * time))

def read():
    global principal, interest, year, time

def calc():
    global principal, interest, year, time, amount

def Print(principal, interest, year, time, amount):
    print("Principal = ", principal)
    print("Interest = ", interest)
    print("Number Of Year = ", year)
    print("Number Of Time = ", time)
    print("Amount = ", amount)
Print(principal, interest, year, time, amount)

