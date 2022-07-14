import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import telegram
from anticaptchaofficial.recaptchav2proxyless import *

TELEGRAM_TOKEN= "1034610233:AAEzLizs7SMDLOGLpDf2hvLyXihTnnP9Bsg"

def send_message():
    bot =telegram.Bot(TELEGRAM_TOKEN)
    bot.send_message(chat_id="-1001117671580", text=cecinaFinal)
########################################################################################################################
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36")
s = Service("C:\\Users\\cata\\PycharmProjects\\Selenium\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(service=s)
driver.maximize_window()


driver.get('https://altenens.is/forums/accounts-and-database-dumps.45/'

           )
url= 'https://altenens.is/forums/accounts-and-database-dumps.45/'
#PARAMETROS PARA LOGEAR
login = "moustro3"
password = "xaoxao321"




#PARA LOCALIZAR LAS CAJITAS DE LOS DATOS
input_user = WebDriverWait(driver, 1).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div/div/div[3]/div/div/div[2]/form/div[1]/div/dl[1]/dd/input')))
input_password = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/div[3]/div/div/div[2]/form/div[1]/div/dl[2]/dd/div/div/input')
#PARA ESCRIBIR NUESTRAS CREDENCIALES EN LAS CAJITAS
input_user.send_keys(login)
input_password.send_keys(password)


#captcha

sitekey = driver.find_element(By.XPATH, '//*[@id="top"]/div[4]/div/div/div[3]/div/div/div[2]/form/div[1]/div/dl[3]/dd/div').get_attribute('outerHTML')
sitekey_clean = sitekey.split(" data-invisible=")[0].split(" data-sitekey=")[1].replace('"',' ').replace(' ','')


solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key('987fca8b628be7693d4dd873a115aeb3')
solver.set_website_url(url)
solver.set_website_key(sitekey_clean)

g_response = solver.solve_and_return_solution()


driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')

driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
#CLICK AL BOTON DE LOG IN
driver.find_element(By.XPATH, '//button[@class= "button--primary button button--icon button--icon--login"]').click()

time.sleep(20)



#'//div[@class="structItemContainer-group js-threadList"]//time[@class="u-dt"]').text
time.sleep(1)
driver.execute_script("window.scrollTo(0,1000)")
#driver.refresh()
#time.sleep(5)

#temporalidad=
while True:
    driver.refresh()
    amomentago = ('A moment ago')
    temporalidad_uno= driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[4]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[2]/div[2]/ul/li[2]/a/time').text
    temporalidad_dos= driver.find_element(By.XPATH,
                                       '/html/body/div[1]/div[4]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/div[2]/div[2]/ul/li[2]/a/time').text


    if temporalidad_uno == amomentago:
        TELEGRAM_TOKEN = "1034610233:AAEzLizs7SMDLOGLpDf2hvLyXihTnnP9Bsg"
        clicUsuario_uno =driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[4]/div[1]/div[2]/div[2]/ul/li[2]/a/time')
        clicUsuario_uno.click()
        cecinaFinal_uno = driver.find_element(By.XPATH, '//div[@class="bbWrapper"]').text
        bot =telegram.Bot(TELEGRAM_TOKEN)
        bot.send_message(chat_id="-1001117671580", text=cecinaFinal_uno)
        print(cecinaFinal_uno)
        time.sleep(50)
        driver.back()
    elif temporalidad_dos == amomentago:
        TELEGRAM_TOKEN = "1034610233:AAEzLizs7SMDLOGLpDf2hvLyXihTnnP9Bsg"
        clicUsuario_dos = driver.find_element(By.XPATH,
                                                '/html/body/div[1]/div[4]/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div[4]/div[2]/div[2]/div[2]/ul/li[2]/a/time')
        clicUsuario_dos.click()
        cecinaFinal_dos = driver.find_element(By.XPATH, '//div[@class="bbWrapper"]').text
        bot = telegram.Bot(TELEGRAM_TOKEN)
        bot.send_message(chat_id="-1001117671580", text=cecinaFinal_dos)
        print(cecinaFinal_dos)
        time.sleep(50)
        driver.back()
    else:
        time.sleep(10)



