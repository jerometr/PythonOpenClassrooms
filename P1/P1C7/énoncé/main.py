fruits = { "pomme": "rouge", "banane": "jaune", "orange": "orange" }
fruits["kiwi"] = "vert"
couleur_banane = fruits.get("banane")
fruits["pomme"] = "vert"
fruits.pop("banane", None)
print(list(fruits.keys())
