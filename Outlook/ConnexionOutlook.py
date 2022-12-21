"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Connexion à une boite mail de Outlook afin d'y récupérer l'objet d'un mail

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchWindowException
from selenium import webdriver

def connexionOutlook() :
    try:
        # on config la page de façon à ce que le bandeau "chrome is being controlled by automated test software" ne soit pas affiché
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # on lance le driver avec la config
        driver = webdriver.Chrome(options=chrome_options)
        # mettre la page en grand écran
        driver.maximize_window()

        # ouvrir le la page de connexion de linkedin
        driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1668977536&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3ddf0633dc-1198-a85e-b368-79742f55dbed&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")

        # delay va servir si au bout de 10sec aucune réponse de la page alors on coupe 
        delay = 100

        # entrer l'adresse mail
        mail = ""
        inputMail = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]')))
        inputMail.send_keys(mail)

        # on clique sur suivant
        btnNext = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div/input')))
        btnNext.click()

        # entrer le mot de passe
        password = ""
        inputPwd = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input')))
        inputPwd.send_keys(password)

        # on clique sur s'identifier
        btnConnect = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input')))
        btnConnect.click()

        # on clique le non lors du message si on veut rester connecter
        btnNonResterLog = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input')))
        btnNonResterLog.click()
        
        # on clique sur autre dans la boite de recception
        btnAutreMsg = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div[1]/div[1]/div[1]/div/div[2]/div/div/div[1]/button[2]')))
        btnAutreMsg.click()

        # on clique sur un message
        btnMsg = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]')))
        btnMsg.click()

        contenuMsg = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/div/div[3]/div[3]/div/div/div/div/div[1]/div[1]/div/div/div').text

        print(contenuMsg)
        
    except TimeoutException:
        print("Le chargepment de la page a pris trop de temps")
    except NoSuchWindowException:
        print("La page demandé n'a pas été trouvé")
    except ElementNotInteractableException:
        print("Un composant n'a pas pu être trouvé")

if __name__ == "__main__":
    connexionOutlook()
