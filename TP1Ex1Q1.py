"""
Created on Fri Mar 11 11:28:33 2022

@author: David LACAN
"""

VENTES={"Martin":38, "Dupont":52, "Durand":26, "Perrin":64,"Blanc":42}
somme = 0

for cle, valeur in VENTES.items():
    somme += valeur
print(somme)


