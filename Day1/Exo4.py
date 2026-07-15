def eleMax(liste, debut=None, fin=None):
    """
    Retourne l'élément maximum d'une liste entre les indices debut et fin.
    Si debut est omis, la recherche commence à l'indice 0.
    Si fin est omis, la recherche s'étend jusqu'à la fin de la liste.
    """
    if debut is None:
        debut = 0
    if fin is None:
        fin = len(liste)

    if debut < 0:
        debut = 0
    if fin < 0:
        fin = max(0, len(liste) + fin)

    if fin < debut:
        return None

    sous_liste = liste[debut:fin]
    return max(sous_liste) if sous_liste else None


def Exo4():
    """
    Exo 4 : Fonction eleMax
    """
    serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
    print(eleMax(serie))
    print(eleMax(serie, 2, 5))
    print(eleMax(serie, 2))
    print(eleMax(serie, fin=3, debut=1))


# %% zone du main
if __name__ == '__main__':
    Exo4()