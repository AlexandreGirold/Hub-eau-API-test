import requests
from test import *

# url = "http://hubeau.eaufrance.fr/api/vbeta/qualite_eau_potable/communes_udi"

# response = requests.post(url, stream = True)

def API_response(url):

    """Retourne la réponse des API de hub'eau

    Returns:
        class 'requests.models.Response': valeur de la réponse
    """
    try:
        response = requests.post(url, stream = True)
        return response
    except :
        pass#TODO send to contrendu

# print(API_response("http://hubeau.eaufrance.fr/api/vbeta/qualite_eau_potable/communes_udi"))
# print(API_response("http://hubeau.eaufrance.fr/api/v1/hydrometrie/referentiel/stations"))

def get_api_keys(url):

    """ Recupere les clés des APIs de hub'eau

    Returns:
        list: liste des clés des API de hub'eau
    """
    try:
        response = requests.post(url, stream = True)
        contenu = response.json()
        json_data = contenu["data"]
        liste_fin = []
        

        for x in json_data: 
            for k in x.keys():
                liste_fin.append(k)
            return(liste_fin)
    except:
        pass#TODO send to contrendu

# print(get_api_keys("http://hubeau.eaufrance.fr/api/v1/niveaux_nappes/chroniques_tr"))
# print(get_api_keys("http://hubeau.eaufrance.fr/api/v1/hydrometrie/obs_elab"))