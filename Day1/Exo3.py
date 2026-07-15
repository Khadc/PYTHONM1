def Exo3():
    """
    Exo 3 : Fonction volBoite
    """
    def volBoite(x1, x2=None, x3=None):
        """
        Calcule le volume selon le nombre d'arguments :
            1 argument : cube (arête)
            2 arguments : prisme à base carrée (côté, hauteur)
            3 arguments : parallélépipède (longueur, largeur, hauteur)
        """
        if x2 is None and x3 is None:
            return x1 ** 3
        elif x3 is None:
            return x1 * x1 * x2
        else:
            return x1 * x2 * x3

    choix = int(input("Choisissez le type de boîte (1 = cube, 2 = prisme, 3 = parallélépipède) : "))

    if choix == 1:
        x1 = float(input("Entrez l'arête du cube : "))
        print(f"Volume du cube : {volBoite(x1):.2f}")
    elif choix == 2:
        x1 = float(input("Entrez le côté du carré : "))
        x2 = float(input("Entrez la hauteur du prisme : "))
        print(f"Volume du prisme : {volBoite(x1, x2):.2f}")
    elif choix == 3:
        x1 = float(input("Entrez la longueur : "))
        x2 = float(input("Entrez la largeur : "))
        x3 = float(input("Entrez la hauteur : "))
        print(f"Volume du parallélépipède : {volBoite(x1, x2, x3):.2f}")
    else:
        print("Choix invalide.")


# %% zone du main
if __name__ == '__main__':
    Exo3()