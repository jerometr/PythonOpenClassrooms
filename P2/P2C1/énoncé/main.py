#Consignes

#    Demandez à l'utilisateur de fournir deux nombres avec la fonction input. Stockez ces valeurs dans  nombre1 et  nombre2.

#    nombre1 et  nombre2 sont des chaînes de caractères (str). Utilisez la méthode isnumeric pour vérifier que ce sont des nombres.

#    Si ce n'est pas le cas, sortez du programme en générant une exception avec le mot clé raise: raise SystemExit("Fin du programme")

#    Sinon, convertissez les deux nombres en nombres entiers avec la fonction  int.

#    Créez une variable operation et utilisez input pour obtenir l'opération souhaitée par l'utilisateur.

#    Vérifiez que l'opération est valide (+, -, * ou /). Sinon, quittez le programme.

#    Effectuez le calcul en fonction de la valeur de operation (par exemple en utilisant if - elif - else) et stockez le résultat dans la variable resultat.

#    Attention, il est impossible de diviser un nombre par 0, il faut donc prévoir une structure conditionnelle supplémentaire pour quitter le programme si le deuxième nombre est 0.

#    Astuce : lors de la division, utilisez la fonction round pour arrondir le résultat et le rendre plus lisible !

#    Affichez le resultat.

nombre1 = input("Entrez un nombre entier: ")
nombre2 = input("Entrez un nombre entier: ")

if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Erreur: les deux nombres doivent être des nombres entiers")
    raise SystemExit("Fin du programme")
else:
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

operation = input("Quelle opération souhaitez-vous réaliser : ")

if operation not in ["+", "-", "*", "/"]:
    print("Erreur: l'opération doit être +, -, * ou /")
    raise SystemExit("Fin du programme")
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
  resultat = nombre1 - nombre2
elif operation == "*":
  resultat = nombre1 * nombre2
elif operation == "/":
  if nombre2 == 0:
    print("Erreur : le diviseur est nul")
    raise SystemExit("Fin du programme")
  else:
  resultat = round(nombre1 / nombre2, 2)

print(f"Le résultat de l'opération est: {round(resultat, 2)}")

  

