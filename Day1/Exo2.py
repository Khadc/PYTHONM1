def Exo2():
    """
    Exo 2 : Maximun et Minimum
    """
    nombre1 = int(input("Entrez le premier nombre1 : "))
    nombre2 = int(input("Entrez le deuxième nombre2 : "))
    if nombre1 > nombre2:
        maximum = nombre1
        minimum = nombre2
        print(f"Le maximum entre {nombre1} et {nombre2} est : {maximum}")
        print(f"Le minimum entre {nombre1} et {nombre2} est : {minimum}")
    elif nombre1 < nombre2:
        maximum = nombre2
        minimum = nombre1
        print(f"Le maximum entre {nombre1} et {nombre2} est : {maximum}")
        print(f"Le minimum entre {nombre1} et {nombre2} est : {minimum}")
    else:
        print(f"Les deux nombres sont égaux : {nombre1} = {nombre2}")

# %% zone du main
if __name__ == '__main__':
    Exo2()