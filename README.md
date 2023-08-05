# Comment bien faire vos fichier excel et CSV.

# ATTENTION CETTE VERSION N'EST PLUS DU TOUT A JOUR

## Points importants :

* L'orthographe, une erreur de frappe mène a une erreur dans les tests (meme les epsaces).
* Le nom, soyez sur que le nom est le meme dans l'api et votre fichier. Exemple : timestamp_maj <====> date_maj est la meme chose mais renvera une erreur lors des tests. 
* Mettez dans le CVS seulement les informations du moment, ainsi créez votre excel avec les informations valide en se moment sauvgardez le en CSV puis ajoutez les info sur les modifications futurs (dans l'excel pas CSV).
* Gardez la **meme structure** pour tout vos excels, (exemple : le tableau commence à la ligne 12), utilisez les excels précédent.


# README pour le programme de tests sur les API de Hub'eau.

## Prérequis :

* Python 3 de preférence version supérieur à 3.7.
* Avoir PIP d'installer.


## Installation : 

```bash
pip3 install pandas
```

```bash
pip3 install requests
```

## Run le test :

```bash
python3 main.py
```

## Contrendu : 

Apres avoir run le test un fichier log daté du jour du test sera créé avaec toute les informations nécessaires.

