number1 = input("entre le number1:")
number2 = input("entre le number2:")

if not number1.isnymeric() or not number2.isnumeric():
     print("error")
     raise SystemExit("Fin du programme")

  
number1= int(number1)
number1= int(number2)

operation = input("entre l'operation que vous souhaitee effectuer ['+', '-', '*' ou '/'] :")
    if operation not in ["+","-","*","/"] :
      print("error")
        raise SystemExit("Fin du programme")

if operation == "+":
   resultat = number1 + number2
elif operation == "-":
   resultat = number1 - number2
elif operation == "*":
   resultat = number1 * number2
elif operation == "/":  
   if number2 != 0 :
     resultat = number1 / number2
     else :
     print("error!, on peut pas devise par 0 !")
      raise SystemExit("Fin du programme")

print(f"le resultat est : {resultat}")



