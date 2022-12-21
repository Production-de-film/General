from ConnexionFacebook import *
from __init__ import *

# mail, mdp = infoFacebook()

def configPhoto():
    listeformatImg = ["jpg", "jpeg", "jfif", "pjpeg", "pjp", "png", "svg", "webp", "gif", "avif", "apng"]
    valide = True

    lienImg = input("Saisir le chemin absolu de l'image : ")
    # on va split le chemin pour obtenir que le nom de limage
    splitLienImg = lienImg.split('\\')
    # on va split le nom de limage
    splitNomImg = splitLienImg[-1].split('.')
    # on va regarder si le liien n'est pas vide
    if lienImg != "":
        # on regarde si le format de l'image correspond à un des formats répertoriés dans la liste
        if splitNomImg[-1] in listeformatImg:
            valide = True
        else:
            valide = False
            print("Le format de l'image n'est pas accepté (jpg, jpeg, jfif, pjpeg, pjp, png, svg, webp, gif, avif, apng)")

    img = Image.open(lienImg)
    width = img.width
    if width > 180:
        valide = True
    else:
        valide = False
        print("L'image doit être suppérieur à 180px de large")

    donnerDescription = str(input("Voulez-vous donner une description à votre photo de profil ? o/n"))
    if donnerDescription == 'o':
        description = str(input("Saisir une descritpion allant avec la photo de profil : "))
        valide = True
        if description == "":
            valide = False
            print("La description ne peut pas être vide")
        else:
            valide = True
    else:
        description = ""

    return valide, lienImg, donnerDescription, description

def ajouterPhoto(driver:object, lienImg:str, donnerDescription:str, description:str):
    try:
        # delay va servir si au bout de 10sec aucune réponse de la page alors on coupe 
        delay = 1000

        # connexionFacebook(driver, mail, mdp)
        connexionFacebook(driver, "ducorney.michel.le0@gmail.com", "azertyuiop013*")

        # on clique sur la photo de profil pour faire apparaitre la liste déroulante pour voir les options qu'on a
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[1]'))).click()

        # si l'option "ajouter une photo" est dispo alors on va cliquer dessus sinon ça veut dire qu'il existe deja une photo donc on doit la modifier donc on va appeler la fonction modifier
        try:
            # on clique sur l'option "ajouter une photo" pour pouvoir faire apparaitre une pop up avec les options qu'on a
            WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[1]'))).click()
        except:
            modifierPhoto(driver, lienImg, donnerDescription, description)

        # on va chercher le chemin de l'image pour l'insérer directement dans le input
        inputImg = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/input')))
        inputImg.send_keys(lienImg)

        # on rempli la description de l'image directement dans le input
        inputDescrption = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div/label/div/div/textarea')))
        inputDescrption.send_keys(description)

        # on va cliquer sur "enregistre"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[5]/div[2]/div'))).click()

        driver.quit()

    except TimeoutException:
        print("Le chargepment de la page a pris trop de temps")
    except NoSuchWindowException:
        print("La page demandé n'a pas été trouvé")
    except ElementNotInteractableException:
        print("Un composant n'a pas pu être trouvé")

def modifierPhoto(driver:object, lienImg:str, donnerDescription:str, description:str):
    # si la description n'est pas vide et que valide est à true alors on execute le programe
    try:
        # delay va servir si au bout de 10sec aucune réponse de la page alors on coupe 
        delay = 1000

        # connexionFacebook(driver, mail, mdp)
        connexionFacebook(driver, "ducorney.michel.le0@gmail.com", "azertyuiop013*")
        
        # on clique sur la photo de profil pour faire apparaitre la liste déroulante pour voir les options qu'on a
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[1]'))).click()

        # on clique sur l'option "mettre a jour la photo de profil" pour pouvoir faire apparaitre une pop up avec les options qu'on a
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[1]'))).click()
        
        # on va chercher le chemin de l'image pour l'insérer directement dans le input
        inputImg = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div/div[1]/input')))
        inputImg.send_keys(lienImg)

        # on rempli la description de l'image directement dans le input
        inputDescrption = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div/label/div/div/textarea')))
        inputDescrption.send_keys(description)
        
        # on va cliquer sur "enregistre"
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[5]/div[2]'))).click()

        driver.quit()

    except TimeoutException:
        print("Le chargepment de la page a pris trop de temps")
    except NoSuchWindowException:
        print("La page demandé n'a pas été trouvé")
    except ElementNotInteractableException:
        print("Un composant n'a pas pu être trouvé")