from bs4 import BeautifulSoup
import requests
import time
import telegram

#paso 1 = colocar la url con un nombre especifico
#paso 2 = crear variable donde estara el precio utilizar extraerprecios y añadimos la variable url
#paso 3 = crear variable precio bajo = al precio en el momento
#paso 4 = cambiar x por y
#paso 5 = crear crear precio == precio bajox
#paso 6 = cambiar en botsend en el str el precio del producto despues en los /n/ poner la url


#[[[[nuevo nombre variable]]]] = ' [[[[url aqui]]]] '
#[[[[nombre del la variable ejemplo preciobajo]]]]= [[[[precio en el momento del producto]]]]
#[[[[PRECIO + NOMBRE DE LA URL]]]] = int(extraerprecios(URL).replace('$',''))
#idProducto[[[[x]]]]=[[[[url]]]] .split('/')[-1]
#print(idProducto)
#if [[[[nombre variable del precio del momento]]]] == nombre del la variable ejemplo preciobajo :
#    bot = telegram.Bot(TELEGRAM_TOKEN)
#    bot.send_message(chat_id=idtelegram, text=f"Hay oferta bb\nId producto: {idProducto}\nEl precio esta en: {'$'+str([[[[nombre variable del precio del momento]]]])}\n{[[[[url]]]]}\nId producto:{idProducto}")


idtelegram= '-755461465'
TELEGRAM_TOKEN= '1034610233:AAEzLizs7SMDLOGLpDf2hvLyXihTnnP9Bsg'

def extraerprecios(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, "html.parser")
    ExtraccionLineaPrecio = soup.find("p", {"class":"price"}).text

    return ExtraccionLineaPrecio

#
while True:
    
        leche= "https://www.lider.cl/supermercado/product/Lider-Leche-Natural-Entera/3091"
        sibajadeesto1= 820
        precioleche = int(extraerprecios(leche).replace('$',''))
        idProducto1= leche.split('/')[-1]

        if precioleche < sibajadeesto1:
            bot = telegram.Bot(TELEGRAM_TOKEN)
            bot.send_message(chat_id=idtelegram, text=f"Hay oferta bb\nId producto: {idProducto1}\nEl precio esta en: {'$'+str(precioleche)}\n{leche}\nId producto:{idProducto1}")
            time.sleep(5)
        ##################################2#####################################################################################


        descremada = 'https://www.lider.cl/supermercado/product/Lider-Leche-Blanca-Descremada-Caja/3095'
        sibajadeesto2 = 840
        precioDescremada = int(extraerprecios(descremada).replace('$',''))
        idProducto2 = descremada.split('/')[-1]

        if precioDescremada < sibajadeesto2 :
            bot = telegram.Bot(TELEGRAM_TOKEN)
            bot.send_message(chat_id=idtelegram, text=f"Hay oferta bb\nId producto: {idProducto2}\nEl precio esta en: {'$'+str(precioDescremada)}\nBajo un: {(((int(precioDescremada))-int(sibajadeesto2))/int(sibajadeesto2))*-100} {'%'} \n{descremada}")
            time.sleep(5)
        ##################################3####################################################################################

        semidrescremada= 'https://www.lider.cl/supermercado/product/Lider-Leche-Semidescremada/5797'
        sibajadeesto3= 840
        preciosemidescremada= int(extraerprecios(semidrescremada).replace('$',''))
        idProducto3 = semidrescremada.split('/')[-1]

        if preciosemidescremada < sibajadeesto3 :
            bot = telegram.Bot(TELEGRAM_TOKEN)
            bot.send_message(chat_id=idtelegram, text=f"Hay oferta bb\nId producto: {idProducto3}\nEl precio esta en: {'$'+str(preciosemidescremada)}\nBajo un: {(((int(preciosemidescremada))-int(sibajadeesto3))/int(sibajadeesto3))*-100} {'%'} \n{semidrescremada}")
            time.sleep(5)

#################################4######################################################################################

