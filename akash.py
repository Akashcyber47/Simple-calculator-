
print("SIMPLE CALCULATOR")

print("OPERATORS")
print("1. ADDITION")
print("2. SUBSTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. EXIT")

print("ENTER CORRECT OPTION")
option=float(input())
print("ENTER FIRST NUMBER")
num1=int(input())
print("ENTER SECOND NUMBER")
num2=int(input())

if option==1:
    print(num1+num2)
    
elif option==2:
    print(num1-num2)
   
elif option==3:
    print(num1 *num2)
elif option==4:
    print(num1/num2)
elif option==5:
    Break
else:
    Print("invalid option")
    
    
    
    
    