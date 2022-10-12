#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes 
def tempsEnSeconde(temps: tuple) -> int:
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
mon_temps = (3, 23, 1, 34)
print(type(mon_temps))
print(tempsEnSeconde(mon_temps))

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // 86400
    reste = seconde % 86400

    heure = reste // 3600
    reste = reste % 3600

    minute = reste // 60
    reste = reste % 60

    return (jour, heure, minute, reste)

temps = secondeEnTemps(100000)
print(temps[0],"jour",temps[1],"heure",temps[2],"minute",temps[3],"seconde")



def affichePluriel(mot: str, nombre: int) -> None: 
    """Affiche (ou non) un mot en fonction du paramètre nombre.
       Met le mot au pluriel si nécessaire."""
    if nombre > 0:
        print(" ", nombre, mot, end="")
    if nombre > 1:
        print("s",end="")
    
def affichetemps(temps: tuple) -> None:
    """"Affiche le tuple temps sous la forme :
        X jours(s), X heures(s), X minute(s), X seconde(s)"""
    affichePluriel("jour", temps[0])
    affichePluriel("heure", temps[1])
    affichePluriel("minute", temps[2])
    affichePluriel("secondes", temps[3])
    print()

affichetemps((1, 0, 14, 23))




def demandeTemps():
    """Demande à l'utilisateur un nombre de jours, d'heures, de minutes 
    et de secondes et les renvoie sous la forme d'un tuple de temps"""
    jours = -1
    heures = -1
    minutes = -1
    secondes = -1

    while (jours < 0):
        jours = int(input("Entrez un nombre de jour "))
    while (heures < 0 or heures >=24):
        heures = int(input("Entrez un nombre d'heures "))
    while (minutes < 0 or minutes >= 60):
        minutes = int(input("Entrez un nombre de minutes "))
    while (secondes < 0 or secondes >= 60):
        secondes = int(input("Entrez un nombre de secondes "))
    return (jours, heures, minutes, secondes)

affichetemps(demandeTemps())