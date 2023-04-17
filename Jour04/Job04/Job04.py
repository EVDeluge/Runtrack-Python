def Ajout_Fruit():                                  # Création d'une fonction ajoutant un fruit
    fruits = ["pomme", "cerise", "orange", "Melon"] # Création d'une variable pour stocker les fruits
    fruits.insert(4, "Mangue")                      # Insertion le nouveau fruit (Je change en fin de liste)
    return fruits
Tous_Fruits = Ajout_Fruit()                         # Création d'une variable pour tous les fruits
print(Tous_Fruits)                                  # Afficher l'ensemble des fruits