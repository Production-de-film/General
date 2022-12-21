from PhotoDeProfil import *
from FamilleEtRelation import *
from LieuxDeResidence import *
from __init__ import *

# selon le choix de l'action fait pas l'utilisateur alors un module va se lancer - exemple : si on veut modifier la photo de profil alors on se connecter et sélectionner 2 qui fait reference au module pour modifier la photo
def choixOptionFacebook():
    choix = int(input("Saisir le chiffre associé à l'action à faire sur Facebook : \n\t1 Ajouter une photo de profil\n\t2 modifier la photo de profil\n\t3 ajouter une relation amoureuse\n\t4 modifier une relation amoureuse \n\t Votre choix : "))
    
    return choix

# # module pour ajouter une photo de profil
# try:
#     if choixOptionFacebook() == 1:
#         valide, lienImg, donnerDescription, description = configPhoto()

#         # on config la page de façon à ce que le bandeau "chrome is being controlled by automated test software" ne soit pas affiché
#         chrome_options = webdriver.ChromeOptions()
#         # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

#         # pour enlever la popo up de demande de notification
#         chrome_options.add_argument('--disable-notifications')
#         # on lance le driver avec la config
#         driver = webdriver.Chrome(options=chrome_options)
#         # mettre la page en grand écran
#         driver.maximize_window()
        
#         if valide:
#             ajouterPhoto(driver, lienImg, donnerDescription, description)
        
#         print("\nL'ajout de la photo de profil à bien été réalisé\n")
# except:
#     print("\nUne erreur est survenu l'ors de l'ajout d'un photo de profil\n")

# # module pour modifier une photo de profil
# try:
#     if choixOptionFacebook() == 2:
#         valide, lienImg, donnerDescription, description = configPhoto()

#         # on config la page de façon à ce que le bandeau "chrome is being controlled by automated test software" ne soit pas affiché
#         chrome_options = webdriver.ChromeOptions()
#         # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

#         # pour enlever la popo up de demande de notification
#         chrome_options.add_argument('--disable-notifications')
#         # on lance le driver avec la config
#         driver = webdriver.Chrome(options=chrome_options)
#         # mettre la page en grand écran
#         driver.maximize_window()
        
#         if valide:
#             modifierPhoto(driver, lienImg, donnerDescription, description)

#         print("\nLa modification de la photo de profil à bien été réalisé\n")
# except:
#     print("\nUne erreur est survenu l'ors de la modification de la photo de profil\n")

# # module pour ajouter une relation amoureuse
# try:
#     if choixOptionFacebook() == 3:
#         valide, relation, annee = configRelation()

#         # on config la page de façon à ce que le bandeau "chrome is being controlled by automated test software" ne soit pas affiché
#         chrome_options = webdriver.ChromeOptions()
#         # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

#         # pour enlever la popo up de demande de notification
#         chrome_options.add_argument('--disable-notifications')
#         # on lance le driver avec la config
#         driver = webdriver.Chrome(options=chrome_options)
#         # mettre la page en grand écran
#         driver.maximize_window()

#         if valide:
#             ajouterRelation(driver, relation, annee)

#         print("\nL'ajout d'une relation amoureuse\n")
# except:
#     print("\nUne erreur est survenu l'ors de l'ajout d'une relation amoureuse\n")

# # module pour modifier une situation amoureuse
# try:
#     if choixOptionFacebook() == 4:
#         valide, relation, annee = configRelation()

#         # on config la page de façon à ce que le bandeau "chrome is being controlled by automated test software" ne soit pas affiché
#         chrome_options = webdriver.ChromeOptions()
#         # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

#         # pour enlever la popo up de demande de notification
#         chrome_options.add_argument('--disable-notifications')
#         # on lance le driver avec la config
#         driver = webdriver.Chrome(options=chrome_options)
#         # mettre la page en grand écran
#         driver.maximize_window()

#         if valide:
#             modifierRelation(driver, relation, annee)

#         print("\nLa modification d'une relation amoureuse\n")
# except:
#     print("\nUne erreur est survenu l'ors de la modification d'une relation amoureuse\n")

# module pour ajouter une ville de résidence actuel
if choixOptionFacebook() == 5:
    # try:
    valide, villeActuelle = configResidence()

    # on config la page de façon à ce que le bandeau "chrome is being controlled by automated test software" ne soit pas affiché
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

    # pour enlever la popo up de demande de notification
    chrome_options.add_argument('--disable-notifications')
    # on lance le driver avec la config
    driver = webdriver.Chrome(options=chrome_options)
    # mettre la page en grand écran
    driver.maximize_window()

    if valide:
        modifierResidence(driver, villeActuelle)
    
    print("\nL'ajout de la ville a bien été réalisé\n")
    # except:
        # print("\nUne erreur est survenu l'ors de l'ajout de la ville de résidence actuelle\n")
