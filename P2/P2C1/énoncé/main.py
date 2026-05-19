# Ecrivez votre code ici !
number1= input("enter the first number:")
number2= input("enter the second number:")

if not number1.isnumeric() or not number2.isnumeric():
    print("error")
    raise SystemExit("Fin du programme")

number1= int(number1)
number2= int(number2)

operation = input("enter the operation you want to do (+, -, *, /):")

if operation not in ["+", "-", "*", "/"]:
    print("error")
    raise SystemExit("Fin du programme")

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    if number2 ==0:
        print("error: division by zero")
        raise SystemExit("Fin du programme")    
    else:
        resul= number1 / number2
      

print(f"the result of the operation is : {round(result, 2)}")
