fruits=dict()
fruits["pomme"] = "rouge"
fruits["banane"] = "jaune"
fruits["orange"] = "orange"
fruits["kiwi"] = "vert"
couleur_banane = fruits["banane"]
fruits["pomme"] = "vert"
fruits.remove("banane")
print(fruits.keys())
