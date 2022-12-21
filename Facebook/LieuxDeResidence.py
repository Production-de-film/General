from ConnexionFacebook import *
from __init__ import *

def configResidence():
    valide = True

    villeActuelle = str(input("Saisir la ville actuelle : "))
    if villeActuelle == "":
        valide = False
        print("La ville actuelle doit être renseigné")

    # on va encoder en utf8 les données qui ne sont pas en utf8
    types_of_encoding = ["utf8", "cp1252"]
    for encoding_type in types_of_encoding:
        # on va ouvrir le fichier en encodant chaque donnée en utf8
        with codecs.open("ville_de_france.csv", encoding = encoding_type, errors ='replace') as csvfile:
            spamreader = csv.reader(csvfile)
            for row in spamreader:
                if villeActuelle in row[3]:
                    return valide, villeActuelle

    return print("La ville n'existe pas, merci de saisir une ville française")

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
