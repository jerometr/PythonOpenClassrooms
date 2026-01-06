#Consignes

#    Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : "1,2,3,4").

#    Stockez cette valeur dans une variable nombres. nombres est une chaîne de caractères (str).

#    Utilisez la fonction split pour transformer cette chaîne de caractères en une variable de type liste liste. liste est une liste de chaîne de caractères.

#    Transformez liste en une liste d'entiers liste_entiers, en utilisant la fonction int. Vous devrez convertir chaque élément un par un ! Utilisez une boucle.

#    Calculez et affichez la somme des nombres dans la liste.

#    Calculez et affichez la moyenne des nombres dans la liste.

#    Calculez et affichez le nombre de nombres dans la liste qui sont supérieurs à la moyenne.

nombres = input("Saisissez une liste de nombres séparés par des virgules (par exemple: "1,2,3,4")

liste = nombres.split(",")
print("Liste des nombres:", liste)

liste_entiers = []
for nombre in liste
  liste_entiers = liste_entiers.append(int(nombre))

somme = 0
for x in liste_entiers
  somme += x
print("Somme des nombres:", somme)

moyenne = somme / len(liste_entiers)
print("Moyenne des nombres:", moyenne)

nombre_de_nombres_superieurs_a_la_moyenne = 0
for x in liste_entiers:
  if x >= moyenne:
    nombre_de_nombres_superieurs_a_la_moyenne += 1
print("Nombre de nombres supérieurs à la moyenne", nombre_de_nombres_superieurs_a_la_moyenne)
