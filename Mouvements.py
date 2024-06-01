from machine import Pin
import time
 
pir = Pin(22, Pin.IN, Pin.PULL_DOWN) #on defini le branchement du capteur à la PIN 22
n = 0
 
print('Starting up the PIR Module') 
time.sleep(1)
print('Ready') #envoyer ready si ça marche
 
while True: #boucle infini
     if pir.value() == 1: #si la broche PIR est haute (le capteur a détecté un mouvement)
          n = n+1
          print('Motion Detected ',n) #envoyer dans la console motion detected pour savoir si ca marche
     time.sleep(1) #attente d'1 seconde
