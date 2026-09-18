def est_echec(ligne):
    if "Failed" in ligne :
        return True
    else :
        return False

def extraire_ip(ligne):
    mots = ligne.split()
    return mots[10]


compteur = {}
with open("auth.log", "r") as file:
    for line in file:
        line = line.strip()
        if est_echec(line):
            ip = extraire_ip(line)
            if ip in compteur: 
                compteur[ip] = compteur[ip] +1
            else: 
               compteur[ip] = 1 

for ip, nombre in compteur.items():
    if nombre >= 3:
        print("WARNING, suspected ip", ip, "with", nombre, "tries" )