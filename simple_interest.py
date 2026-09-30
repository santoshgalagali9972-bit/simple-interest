def calc(principal, rate, time):
   
    return (principal * rate * time) / 100

if __name__ == "__main__":
    principal = int(input("Enter the principal amount: "))
    rate = int(input("Enter the rate of interest: "))
    time = int(input("Enter the time in years: "))
    print("The simple interest is:", calc(principal, rate, time))