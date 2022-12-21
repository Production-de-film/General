from ConnexionFacebook import *
from __init__ import *

def configResidence():
    valide = True

    villeActuelle = str(input("Saisir la ville actuelle : "))
    if villeActuelle == "":
        valide = False
        print("La ville actuelle doit être renseigné")

    with open('ville_de_france.json') as json_file:
        json_data = json.load(json_file)

    # on parcours tout le fichier ce qui nous donne une liste des pays
    for i in json_data:
        # on parcours tous les pays un par un 
        for j in json_data[i]:
            # si la ville saisie est dans la liste des villes d'un pays alors on return le tout 
            if villeActuelle in j:
                valide = True
                return valide, villeActuelle

    return print("La ville n'existe pas, veillez à saisir l'orthographe exacte de la ville")

def ajouterResidence(driver, villeActuelle):
    try:
        delay = 1000
        
        connexionFacebook(driver, "ducorney.michel.le0@gmail.com", "azertyuiop013*")

        # on va cliquer sur "a propos"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div'))).click()

        try:
            # on va cliquer sur "ajouter la ville actuelle"
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div/div[2]/span'))).click()
        except:
            modifierResidence(driver, villeActuelle)

        # on saisie la ville actuelle puis séletionne la ville qui correspond  
        villeActuelleInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div[1]/div/div/div/div/div/label/div/div/input')))
        villeActuelleInput.click()
        villeActuelleInput.send_keys(Keys.DELETE)
        villeActuelleInput.send_keys(villeActuelle)
        time.sleep(5)
        villeActuelleInput.send_keys(Keys.DOWN)
        villeActuelleInput.send_keys(Keys.ENTER)

        # on clique sur le bouton "enregistrer"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div[3]/div[2]/div[2]/div/div[1]/div/span/span'))).click()

        driver.quit()

    except TimeoutException:
        print("Le chargepment de la page a pris trop de temps")
    except NoSuchWindowException:
        print("La page demandé n'a pas été trouvé")
    except ElementNotInteractableException:
        print("Un composant n'a pas pu être trouvé")



def modifierResidence(driver, villeActuelle):
    try:
        delay = 10000
        
        connexionFacebook(driver, "ducorney.michel.le0@gmail.com", "azertyuiop013*")
        
        # on va cliquer sur "a propos"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div'))).click()

        # on clique sur les 3 points pour faire apparaitre la liste des choix
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]/div'))).click()

        # on va cliquer sur "modifier la ville actuelle"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[1]/div[2]'))).click()

        # on saisie la ville actuelle puis séletionne la ville qui correspond  
        villeActuelleInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div[1]/div/div/div/div/div/label/div/div/input')))
        villeActuelleInput.click()
        villeActuelleInput.send_keys(Keys.DELETE)
        villeActuelleInput.send_keys(villeActuelle)
        time.sleep(5)
        villeActuelleInput.send_keys(Keys.DOWN)
        villeActuelleInput.send_keys(Keys.ENTER)

        # on clique sur le bouton "enregistrer"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div[3]/div[2]/div[2]/div/div[1]/div/span/span'))).click()

        driver.quit()

    except TimeoutException:
        print("Le chargepment de la page a pris trop de temps")
    except NoSuchWindowException:
        print("La page demandé n'a pas été trouvé")
    except ElementNotInteractableException:
        print("Un composant n'a pas pu être trouvé")

def supprimerResidence(driver):
    try:
        delay = 10000
        
        connexionFacebook(driver, "ducorney.michel.le0@gmail.com", "azertyuiop013*")

        # on va cliquer sur "a propos"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div'))).click()

        # on clique sur les 3 points pour faire apparaitre la liste des choix
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div/div[4]/div/div/div[2]/div'))).click()

        # on va cliquer sur "supprimer la ville actuelle"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[2]'))).click()

        # on clique sur le bouton "confirmer"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div/div[1]/div/div'))).click()

        driver.quit()

    except TimeoutException:
        print("Le chargepment de la page a pris trop de temps")
    except NoSuchWindowException:
        print("La page demandé n'a pas été trouvé")
    except ElementNotInteractableException:
        print("Un composant n'a pas pu être trouvé")
