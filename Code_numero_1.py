#Lecture d'un fichier csv

import pandas as pd
df = pd.read_csv("EIVP/EIVP_KM.csv")
df.head()

import csv

# Ouverture du fichier source.
# D'après la documentation, le mode ''b'' est
# *obligatoire* sur les plate-formes où il est
# significatif. Dans la pratique, il est conseillé
# de toujours le mettre.
fname = "table.csv"
file = open(fname, "rb")

try:
    # Création du ''lecteur'' CSV.
    reader = csv.reader(file)
    # Le ''lecteur'' est itérable, et peut être utilisé
    # dans une boucle ''for'' pour extraire les
    # lignes une par une.
    for row in reader:
	print row
finally:
    # Fermeture du fichier source
    file.close()


#CODE LECTURE ET EXTRACTION Résolu

import pandas as pd
importation=r"C:\Users\hicha\OneDrive\Documents\Bureau\EIVP_KM.csv"
Tableau_csv = pd.read_csv(importation, engine = "python", sep=";", skiprows=2)
print(Tableau_csv)

>>> print(Tableau_csv)
      1  44.5  25.5  55.0  288  429  2020-09-11 18:03:03 +0200
0     1  34.5  25.5  55.0  286  417  2020-09-11 18:18:03 +0200
1     1  37.5  25.5  54.5  282  433  2020-09-11 18:33:03 +0200
2     1  36.0  25.3  55.0  274  403  2020-09-11 18:48:03 +0200
3     1  30.0  25.3  55.0  254  410  2020-09-11 19:03:03 +0200
4     1  33.0  25.3  55.5  234  407  2020-09-11 19:18:03 +0200
...  ..   ...   ...   ...  ...  ...                        ...
7873  6  41.0  21.3  44.5  728  479  2019-08-25 10:45:51 +0200
7874  6  41.0  21.3  44.0  270  482  2019-08-25 11:00:52 +0200
7875  6  42.0  21.3  44.0  302  475  2019-08-25 11:15:52 +0200
7876  6  39.5  21.3  43.5  336  478  2019-08-25 11:30:54 +0200
7877  6  38.5  21.3  43.5  366  459  2019-08-25 11:45:54 +0200

[7878 rows x 7 columns]

#courbes

import pandas as pd
import matplotlib as plt

fn = importation
df = pd.read_csv(fn, names=['lum','humidity']).set_index('lum')
df.plot(kind='bar')
plt.show()

