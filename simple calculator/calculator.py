a=int(input("Enter first number: "))    
b=int(input("Enter second number: "))

print("-----------SIMPLE CALCULATOR-----------")

print("1. Addition")
print("2. Subtraction") 
print("3. Multiplication")
print("4. Division")        
choice = input("Select operation (1/2/3/4): ")

if choice == "1":
    print("result:","\n", a, "+", b, "=", a + b)

elif choice == "2":
    print("result:","\n", a, "-", b, "=", a - b)        

elif choice == "3":
    print("result:","\n", a, "*", b, "=", a * b)

elif choice == "4":
    print("result:","\n", a, "/", b, "=", a / b)