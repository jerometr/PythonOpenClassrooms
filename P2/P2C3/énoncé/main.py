# Consignes

#    Créez une fonction appelée  salaire_mensuel(salaire_annuel)  qui prend en paramètre un salaire annuel et retourne le salaire mensuel correspondant en divisant le salaire annuel par 12.
def salaire_mensuel(salaire_annuel):
  salaire_mensuel = salaire_annuel / 12
  return salaire_mensuel
  
#    Créez une fonction appelée  salaire_hebdomadaire(salaire_mensuel)  qui prend en paramètre un salaire mensuel et retourne le salaire hebdomadaire correspondant en divisant le salaire mensuel par 4.
def salaire_hebdomadaire(salaire_mensuel):
  salaire_hebdomadaire = salaire_mensuel / 4
  return salaire_hebdomadaire
  
#    Créez une fonction appelée  salaire_horaire(salaire_hebdomadaire, heures_travaillees)  qui prend en paramètres un salaire hebdomadaire et le nombre d'heures travaillées par semaine, et retourne le salaire horaire correspondant en divisant le salaire hebdomadaire par le nombre d'heures travaillées par semaine.
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
  if heures_travaillees != 0:
    salaire_horaire = salaire_hebdomadaire / heures_travaillees
  else:
    salaire_horaire = 0
  return salaire_horaire

#    Demandez à l'utilisateur de saisir son salaire annuel.
salaire_annuel = float(input ("Salaire annuel :"))

#    Demandez à l'utilisateur de saisir le nombre d'heures travaillées par semaine.
heures_travaillees = float(input ("Nombre d'heures travaillées par semaine :"))

#    Appelez les fonctions précédemment créées pour calculer le salaire horaire correspondant.
print(f"Votre salaire horaire est de {salaire_horaire(salaire_hebdomadaire(salaire_annuel),heures_travaillees)} euros")

#    Affichez le résultat sous la forme : "Votre salaire horaire est de XX euros".Ecrivez votre code ici
