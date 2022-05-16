hrs = float(input("Enter Hours:"))
xx = input("Enter the rate:")
x = float(xx)
if hrs <= 40:
    print( hrs * x)
elif hrs > 40:
        print(40* x + (hrs-40)*1.5*x)