from __init__ import *
import re

# fonction qui va etre utilisé pour rentré les identifiants etc du compte pour se connecter 
# PAS UTILISE POUR LE MOMENT CAR FLEMME DECRIRE A CHAQUE FOIS
# def infoFacebook():
#     while True:
#         try:
#             regexMail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
            
#             mail = str(input("Saisir l'adresse mail du compte : "))
#             mdp = str(input("Saisir le mot de passe du compte : "))

#             if re.fullmatch(regexMail, mail):
#                 return mail, mdp
#             else:
#                 print("Le mail saisie n'est pas correcte")
#                 False

#             if mail and mdp == "":
#                 print("le mot de passe ou l'adresse mail ne peut pas être vide")
#                 False
#         except:
#             print("le mot de passe ou l'adresse mail n'est pas valide !")

def connexionFacebook(driver, mail, mdp) :
    try:
        # ouvrir le la page de connexion de Facebook
        driver.get("https://www.facebook.com/")

        # delay va servir si au bout de 10sec aucune réponse de la page alors on coupe 
        delay = 1000

        # entrer l'adresse mail (a renseigner)
        inputMail = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'email')))
        inputMail.send_keys(mail)

        inputPass = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'pass')))
        inputPass.send_keys(mdp)

        # on clique sur accepter les cookies necessaires
        # obligatoir pour pouvoir cliquer sur se connecter
        # ciox de xpath car l'id du bouton change
        btnCookies = WebDriverWait(driver, 10000).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[1]')))
        btnCookies.click()

        # on clique sur se connecter
        btnConnect = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'login')))
        btnConnect.click()

        #cliquer sur son profil
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div'))).click()

        if driver.current_url == "https://www.facebook.com/login/?privacy_mutation_token=eyJ0eXBlIjowLCJjcmVhdGlvbl90aW1lIjoxNjcxNTUzODQyLCJjYWxsc2l0ZV9pZCI6MzgxMjI5MDc5NTc1OTQ2fQ%3D%3D":
            print("Le mot de passe ou l'adresse mail n'est pas valide")
            driver.quit()

    except TimeoutException:
        print("Le chargepment de la page a pris trop de temps")
    except NoSuchWindowException:
        print("La page demandé n'a pas été trouvé")
    except ElementNotInteractableException:
        print("Un composant n'a pas pu être trouvé")

        
# connexionFacebook("ducorney.michel.le0@gmail.com", "azertyuiop013*")
