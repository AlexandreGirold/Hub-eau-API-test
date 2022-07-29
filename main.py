from test import *
from api import *
from time import sleep
from contrendu import *


def main():
    print("Testing ...")
    contrendu()

    list_to_csv = find_csv()
 
    
    for link in list_to_csv:
        trigger = False
        url = get_url(link)
        write_contrendu("* Résumé pour l'API " + link + " :")

        if type(url) == float:
            write_contrendu("URL abscent\n")
        elif url[0] != 'h' or url[1] != 't' or url[2] != 't':
            write_contrendu ("URL incomplet\n")
        else :
            sortie_csv = get_nom_colonne(link)
            res = API_response(url)
            # print(res)
            if res.status_code == 404 : 
                # print("wrong url") #TODO add this to final output
                # print(url)
                write_contrendu("l'URL suivant ne fonctionne pas ou est incorrect: " + url + " le code d'erreur est:" + str(res) + "\n")

                
            else :
                csv_en_trop = []
                api_en_trop = []

                sortie_api = get_api_keys(url)
                # print (sortie_api)
                for ele in sortie_csv:
                    if ele in sortie_api:
                        sortie_api.remove(ele)
                        # print("success") # a chaque fois que le match est correct 
                    else:
                        csv_en_trop.append(ele)
                
                for api in sortie_api:
                    api_en_trop.append(api)


                if (len(csv_en_trop)>0):
                    write_contrendu("\nListe des éléments en trop dans le excel (ou manquantent dans l'api):")
                    write_contrendu(url)
                    trigger = True

                    for n in csv_en_trop:
                        
                        write_contrendu("   " + n)

                if (len(api_en_trop)>0):
                    trigger = True
                    write_contrendu("\nListe des éléments manquantent dans l'excel (ou en trop dans l'API):")
                    write_contrendu(url)

                    for m in api_en_trop:
                        write_contrendu("   " + m)
                if trigger == False:
                    write_contrendu("====> Aucun problème <====\n")
                else :
                    write_contrendu("")
    print("Test over")  

main()
