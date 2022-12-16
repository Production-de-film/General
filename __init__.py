from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchWindowException
from PIL import Image

# on config la page de façon à ce que le bandeau "chrome is being controlled by automated test software" ne soit pas affiché
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
# on lance le driver avec la config
driver = webdriver.Chrome(options=chrome_options)
# mettre la page en grand écran
driver.maximize_window()

# delay va servir si au bout de 10sec aucune réponse de la page alors on coupe 
delay = 10