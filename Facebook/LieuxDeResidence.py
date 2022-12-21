from ConnexionFacebook import *
from __init__ import *

def configResidence():
    valide = True

    villeActuelle = str(input("Saisir la ville actuelle : "))
    if villeActuelle == "":
        valide = False
        print("La ville actuelle doit être renseigné")

    return valide, villeActuelle

def ajouterResidence(driver, villeActuelle):
    try:
        delay = 1000
        
        connexionFacebook(driver, "ducorney.michel.le0@gmail.com", "azertyuiop013*")
        print("ok")
        # on va cliquer sur "a propos"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div'))).click()
        print("ok1")
        # on va cliquer sur "Lieux de résidence"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[4]/a'))).click()
        print("ok2")

        # on va cliquer sur "ajouter la ville actuelle"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div'))).click()
        print("ok3")

        # on saisie la ville actuelle puis séletionne la ville qui correspond  
        villeActuelleInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/label/div/div/input')))
        villeActuelleInput.Send_Keys(villeActuelle)
        villeActuelleInput.Send_Keys(Keys.DOWN)
        villeActuelleInput.Send_Keys(Keys.ENTER)
        print("ok4")

        # on clique sur le bouton "enregistrer"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[3]/div[2]/div[2]/div'))).click()

    except TimeoutException:
        print("Le chargepment de la page a pris trop de temps")
    except NoSuchWindowException:
        print("La page demandé n'a pas été trouvé")
    except ElementNotInteractableException:
        print("Un composant n'a pas pu être trouvé")



def modifierResidence(driver, villeActuelle):
    try:
        delay = 1000
        
        connexionFacebook(driver, "ducorney.michel.le0@gmail.com", "azertyuiop013*")
        
        # on va cliquer sur "a propos"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div'))).click()

        # on va cliquer sur "Lieux de résidence"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[4]/a/span'))).click()

        # on clique sur les 3 points pour faire apparaitre la liste des choix
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]/div'))).click()

        # on va cliquer sur "modifier la ville actuelle"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div[2]'))).click()

        # on saisie la ville actuelle puis séletionne la ville qui correspond  
        villeActuelleInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/div/div/div/label/div/div/input')))
        villeActuelleInput.Send_Keys(villeActuelle)
        villeActuelleInput.Send_Keys(Keys.DOWN)
        villeActuelleInput.Send_Keys(Keys.ENTER)

        # on clique sur le bouton "enregistrer"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div[3]/div[2]/div[2]/div'))).click()

    except TimeoutException:
        print("Le chargepment de la page a pris trop de temps")
    except NoSuchWindowException:
        print("La page demandé n'a pas été trouvé")
    except ElementNotInteractableException:
        print("Un composant n'a pas pu être trouvé")

# def supprimer():
#     cs.config()
    
#     try:
#         # on va cliquer sur "a propos"
#         WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div'))).click()

#         # on va cliquer sur "Lieux de résidence"
#         WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[4]/a/span'))).click()

#         # on clique sur les 3 points pour faire apparaitre la liste des choix
#         WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]/div'))).click()

#         # on va cliquer sur "supprimer la ville actuelle"
#         WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[2]'))).click()

#         # on clique sur le bouton "confirmer"
#         WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[1]/div/div'))).click()

#     except TimeoutException:
#         print("Le chargepment de la page a pris trop de temps")
#     except NoSuchWindowException:
#         print("La page demandé n'a pas été trouvé")
#     except ElementNotInteractableException:
#         print("Un composant n'a pas pu être trouvé")