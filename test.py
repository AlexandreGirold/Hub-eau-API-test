import os
import pandas as pd


liste = os.listdir(os.path.join('Hubeau specification'))

def rm_liste(l):
    """Enleve 1er element de la liste

    Args:
        l (list): liste 

    returns l (list): liste sans premier element
    """

    l.pop(0)
    return l
    

def find_csv(): 

    """Cette fonction renvoie une liste des urls tout les fichier csv, attention 2 de profondeur

    Args:
        filepath (string): list des noms des path des dossiers "Hubeau specification"

    Returns:
        list: liste des urls
    """

    csv_list = [] #list of of the CSV files
    l = rm_liste(liste)
    for i, nom in enumerate(l):
        for file in os.listdir(r'Hubeau specification/' + os.path.join(l[i])) :
            name, ext = os.path.splitext(file)
            if ext == '.csv':
                c = r"Hubeau specification/" + nom + r"/" + file #j'aurais du faire ca au lieu de les renommer manuellement.
                csv_list.append(c)
    return csv_list


def get_url (filepath):

    """Returns the API url

    Args:
        filepath (string): path jusqu'au fichier csv
        
    Returns:
        string: API's url
    """

    df = pd.read_csv(filepath, encoding = "unicode_escape", sep = ";", skipinitialspace = True) #skip_blank_lines=True peut etre utile
    link = df.iat[0,1]
    if link == None : 
        return 1 #TODO send to contrendu not raising error as we want to continue de process
    else :
        return link

#   df = pd.read_csv(filepath, encoding = "unicode_escape", sep = ";")
#     link = df.iat[0,1]
#     if link[0] == "h" and link[1] == "t" and link[2] == "t":
#         return link
#     else:
#         return None


def acces_nom_hubeau(filepath):
    
    """Revoie le nom des colonnes

    Args:
        filepath (string): path jusqu'au fichier csv

    Returns:
        list: liste des noms des colonnes
    """

    df = pd.read_csv(filepath, encoding = "unicode_escape", sep = ";", header = 11)
    return list(df.columns)
    

def len_api(filepath):

    """revoie le nombre de lignes

    Args:
        filepath (string):  path jusqu'au fichier csv

    Returns:
        int: nombre de lignes
    """

    df = pd.read_csv(filepath, encoding = "unicode_escape", sep = ";", header = 11)
    m = df.shape
    return m[0] #starting positions 


def get_nom_colonne (filepath):

    """_summary_

    Args:
        filepath (string): path jusqu'au fichier csv

    Yields:
        string: nom de chaque sortie Hubeau
    """

    df = pd.read_csv(filepath, encoding = "unicode_escape", sep = ";", header = 11)
    liste = []
    for i in range (0, len_api(filepath)):
        
        val = df.at[i, "nom Hubeau sortie"]
        if val == '-' or type(val) == float:
            pass
        else:
            liste.append(val)

    return liste

# print(get_nom_colonne("/Users/alexgirold/Desktop/csv/Hubeau specification/03-Hubeau_template_specifications_API_piezoTR_v2.xlsx/03-Hubeau_template_chroniques.csv"))