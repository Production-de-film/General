# from ConfigSelenium import ConfigSelenium

# cs = ConfigSelenium

# class EmploiScolarite:
#     def ajouter():
#         cs.config()

#         valide = True

#         nomEntreprise = str(input("Saisir le nom de l'entreprise : "))
#         if nomEntreprise == "":
#             valide = False
#             print("Le nom de l'entreprise doit être renseigné")

#         posteOccupe = str(input("Saisir le poste occupé dans l'entreprise : "))
#         if posteOccupe == "":
#             valide = False
#             print("Le poste de l'employé doit être renseigné")

#         villeEntreprise = str(input("Saisir le nom de la ville de l'entreprise : "))
#         if villeEntreprise == "":
#             valide = False
#             print("La ville de l'entreprise doit être renseigné")

#         descriptionTravail = str(input("Saisir la description du métier : "))
#         if descriptionTravail == "":
#             valide = False
#             print("La description du travail doit être renseigné")

#         yTravailActuellement = str(input("Saisir si oui ou non vous y travaillez actuellement (o/n) : "))
#         if yTravailActuellement == "":
#             valide = False
#             print("La description du travail doit être renseigné")

#         if valide:
#             try:
#                # on va cliquer sur "a propos"
#                 WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div'))).click()

#                 # on va cliquer sur "Emploie et sécurité"
#                 WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[3]/a'))).click()

#                 # on va cliquer sur "ajouter un lieu de travail"
#                 WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div/div/div[2]'))).click()

#                 # on saisie le nom de l'entreprise
#                 nomEntrepriseInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div/label/div/div/input')))
#                 nomEntrepriseInput.Send_Keys(nomEntreprise)

#                 # on saisie le poste occupé dans l'entreprise
#                 posteOccupeInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div/label/div/div/input')))
#                 posteOccupeInput.Send_Keys(posteOccupe)

#                 # on saisie la ville de l'entreprise
#                 villeEntrepriseInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div/div/label/div/div/input')))
#                 villeEntrepriseInput.Send_Keys(villeEntreprise)

#                 # on saisie la description du travail
#                 descriptionTravailInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[4]/div/label/div/div/textarea')))
#                 descriptionTravailInput.Send_Keys(descriptionTravail)

#                 # si on y travail pas alors on décoche la case - la case est coché de base
#                 if yTravailActuellement != 'o':
#                     WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[5]/div/div/div[2]/span/div[1]/label/div[1]/input'))).click()

#                 # on clique sur le bouton "enregistrer"
#                 WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[6]/div[2]/div[2]'))).click()

#             except TimeoutException:
#                 print("Le chargepment de la page a pris trop de temps")
#             except NoSuchWindowException:
#                 print("La page demandé n'a pas été trouvé")
#             except ElementNotInteractableException:
#                 print("Un composant n'a pas pu être trouvé")
    
#     def modifier():
#         cs.config()
       
#         valide = True

#         nomEntreprise = str(input("Saisir le nom de l'entreprise : "))
#         if nomEntreprise == "":
#             valide = False
#             print("Le nom de l'entreprise doit être renseigné")

#         posteOccupe = str(input("Saisir le poste occupé dans l'entreprise : "))
#         if posteOccupe == "":
#             valide = False
#             print("Le poste de l'employé doit être renseigné")

#         villeEntreprise = str(input("Saisir le nom de la ville de l'entreprise : "))
#         if villeEntreprise == "":
#             valide = False
#             print("La ville de l'entreprise doit être renseigné")

#         descriptionTravail = str(input("Saisir la description du métier : "))
#         if descriptionTravail == "":
#             valide = False
#             print("La description du travail doit être renseigné")

#         yTravailActuellement = str(input("Saisir si oui ou non vous y travaillez actuellement (o/n) : "))
#         if yTravailActuellement == "":
#             valide = False
#             print("La description du travail doit être renseigné")

#         if valide:
#             try:
#                # on va cliquer sur "a propos"
#                 WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div'))).click()

#                 # on va cliquer sur "Emploie et sécurité"
#                 WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[3]/a'))).click()

#                 # on clique sur les 3 points pour faire apparaitre la liste des choix
#                 WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div'))).click()

#                 # on va cliquer sur "modifier le lieu de travail"
#                 WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[1]'))).click()

#                 # on saisie le nom de l'entreprise
#                 nomEntrepriseInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/div/div/div/div/div/label/div/div/input')))
#                 nomEntrepriseInput.Send_Keys(nomEntreprise)

#                 # on saisie le poste occupé dans l'entreprise
#                 posteOccupeInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/div/label/div/div/input')))
#                 posteOccupeInput.Send_Keys(posteOccupe)

#                 # on saisie la ville de l'entreprise
#                 villeEntrepriseInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[3]/div/div/div/div/div/label/div/div/input')))
#                 villeEntrepriseInput.Send_Keys(villeEntreprise)

#                 # on saisie la description du travail
#                 descriptionTravailInput = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[4]/div/label/div/div/textarea')))
#                 descriptionTravailInput.Send_Keys(descriptionTravail)

#                 # si on y travail pas alors on décoche la case - la case est coché de base
#                 if yTravailActuellement != 'o':
#                     WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[5]/div/div/div[2]/span/div[1]/label/div[1]/input'))).click()

#                 # on clique sur le bouton "enregistrer"
#                 WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[6]/div[2]/div[2]'))).click()

#             except TimeoutException:
#                 print("Le chargepment de la page a pris trop de temps")
#             except NoSuchWindowException:
#                 print("La page demandé n'a pas été trouvé")
#             except ElementNotInteractableException:
#                 print("Un composant n'a pas pu être trouvé")

#     def supprimer():
#         cs.config()
    
#         try:
#             # on va cliquer sur "a propos"
#             WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/a[2]/div'))).click()

#             # on va cliquer sur "Emploie et sécurité"
#             WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[1]/div[3]/a'))).click()

#             # on clique sur les 3 points pour faire apparaitre la liste des choix
#             WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div[3]/div/div/div[2]/div'))).click()

#             # on va cliquer sur "modifier le lieu de travail"
#             WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[2]'))).click()

#             # on clique sur le bouton "confirmer"
#             WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[2]'))).click()

#         except TimeoutException:
#             print("Le chargepment de la page a pris trop de temps")
#         except NoSuchWindowException:
#             print("La page demandé n'a pas été trouvé")
#         except ElementNotInteractableException:
#             print("Un composant n'a pas pu être trouvé")