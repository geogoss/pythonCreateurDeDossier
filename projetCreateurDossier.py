# Dans cet exercice, vous allez devoir utiliser le dictionnaire d et la variable chemin pour créer la structure de dossiers contenue dans le dictionnaire à l'intérieur du dossier contenu dans la variable chemin.

# chemin = "ENTREZ UN CHEMIN DE DOSSIER DANS LEQUEL CRÉER LA STRUCTURE"
 
# d = {"Films": ["Le seigneur des anneaux",
#                "Harry Potter",
#                "Moon",
#                "Forrest Gump"],
#      "Employes": ["Paul",
#                   "Pierre",
#                   "Marie"],
#      "Exercices": ["les_variables",
#                    "les_fichiers",
#                    "les_boucles"]}
# Vous devez donc avoir un dossier Films qui contient les sous-dossiers Le seigneur des anneaux, Harry Potter, Moon et Forrest Gump.

# Pareil pour Employes et Exercices.

# Bonne chance !

from pathlib import Path


d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}


chemin = Path.cwd()

for dossier_principal, sous_dossiers in d.items():
    for dossier in sous_dossiers:
        chemin_dossier = Path(chemin) / dossier_principal / dossier
        chemin_dossier.mkdir(exist_ok=True, parents=True)





