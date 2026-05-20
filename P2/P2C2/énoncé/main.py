# Ecrivez votre code ici !
nombres = input("saisie une liste de nombres séparés par des virgules:")

liste = nombres.split(",")

liste_entiers = []
for x in range(len(liste)):
    nombre_entier = int(liste[x])
    liste_entiers.append(nombre_entier)


print (liste_entiers)

#calculer la somme

resultat = 0
for x in range(len(liste_entiers)):
    resultat += liste_entiers[x] 

print(f"le resultat de la somme est :{resultat}")

#calculer la moyenne 

moyenne = 0
moyenne = resultat / len(liste_entiers)

print(f"la moyenne des nombre de la liste est : {moyenne}")

#calculer le nombre de nombres dans la liste qui sont supperieur a la moyenne 

nombres_supperieurs = 0

for n in range(len(liste_entiers)):
    if liste_entiers[n] > moyenne :
        nombres_supperieurs+=1


print(f"le nombre de nombres dans la liste qui sont supérieurs à la moyenne est : {nombres_supperieurs}")




