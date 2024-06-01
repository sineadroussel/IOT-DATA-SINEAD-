import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import utime
import random

rouge = PWM(Pin(17,mode=Pin.OUT)) # emplacement pin Led rouge

rouge.freq(1_000) # dont la frequence est de 1000 (default)
rouge.duty_u16(0000) # faire changer l'intensité 

vert = PWM(Pin(18,mode=Pin.OUT))# emplacement pin Led verte

vert.freq(1_000) # dont la frequence est de 1000 (default)
vert.duty_u16(0000) #changement d'intensité 

bleu = PWM(Pin(19,mode=Pin.OUT))# emplacement Led pin rouge

bleu.freq(1_000) # dont la frequence est de 1000 (default)
bleu.duty_u16(0000) #changement d'intensité 

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'Pixel_7deLivia' #nom de la connexion
password = 'Marionchou' #mot de passe de la connexion
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.lainocs.fr/characters" #Url de l'endroit ou se trouve les cartes Harry Potter 



colors = {"Gryffindor":(30000,000,000), #couleur rouge
          "Slytherin":(1000, 30000, 1000), #couleur verte
          "Hufflepuff":(int((22730000)/255), 20000, 1000), #couleur bleu
          "Ravenclaw":(int((3030000)/255), int((144*30000)/255), 30000), #couleur jaune
          "":(30000, 30000, 30000)}#default #couleur blanche par défaut quand le personnage n'a pas de maisons 
 
while not wlan.isconnected(): #boucle
    print("pas co") #envoyer sur la console pas co si la connexion ne se connecte pas
    utime.sleep(1)
    pass

while(True):
    try:
        print("GET") #envoyer GET si la connexion est réussi 
        r = urequests.get(url) # lance une requete sur l'url
        name = r.json()[11]["name"] #lance la requette sur l'url du nom 
        house = r.json()[11]["house"] #lance la roquette sur l'url de la maison
        #print(r.json()) # traite sa reponse en Json
        print(name) #envoyer dans la console le nom
        print(house) #envoyer dans la console la maison 
        
        rouge.duty_u16(colors[house][0]) #couleur rouge en fonction du tableau
        vert.duty_u16(colors[house][2]) #couleur verte en fonction du tableau 
        bleu.duty_u16(colors[house][1][2][3]) #couleur bleu en fonction du tableau 
        utime.sleep (1)
    
        r.close() # ferme la demande
        utime.sleep(1)
    
        
    except Exception as e:
        print(e)
    

    
    
