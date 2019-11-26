N = int(input("Enter Factorial: "))
def main():
    NFactorial = Factorial(N)
    print(NFactorial)

def Factorial(N):
    if N > 1:
        NFactorial = N * Factorial(N - 1)
    else:
        NFactorial = 1
    return NFactorial
    
main()