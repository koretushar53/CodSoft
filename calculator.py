import math as mt

while True:
    a = int(input("Enter the 1 st value :"))
    b = int(input("Enter the 2 nd value :"))
    print("\n+.Addition\n-.Subtraction\n*.Multiplication\n/.Division\n**.Exponational\n//.Floor Division\n%.Remainder\n_/.Square root\n!.Factorail\n")
    ch = input("Enter the operation:")
    while(ch=='+' or ch=='-' or ch=='*' or ch=='/' or ch=='**' or ch=='//' or ch=='_/' or ch=='!' or ch=='%'):
    
        if (ch=='+'):
            print("Addition:",a+b)
            break
        elif(ch=='-'):
            print("Subtraction:",a-b)
            break
        elif(ch=='*'):
            print("Multiplication:",a*b)
            break
        elif(ch=='/'):
            print("Division:",a/b)
            break
        elif(ch=='**'):
            print("Exponational:",a**b)
            break
        elif(ch=='//'):
            print("Floor Division :",a//b)
            break
        elif(ch=='%'):
            print("Remainder",a%b)
            break
        elif(ch=='_/'):
            print("Squrare root",int(mt.sqrt(a)))
            break
        elif(ch=='!'):
            print("Factorail :",mt.factorial(a))
            break
        else:
            print("Invalid Input")
            break