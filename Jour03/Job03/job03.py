def Numerotation():                     # On crée une fonction (Ici, on l'appelle Numération)
    for i in range(101):                # On demande les 100 premiers chiffres (Ne pas dépasser 101)
        if i!=26 and i!=37 and i!=88:   # Les chiffres 26, 37 et 88 doivent être enlevés de la liste
            print(i)                    # On imprime le résultat
Numerotation()                          # On a terminé, on ferme la fonction...