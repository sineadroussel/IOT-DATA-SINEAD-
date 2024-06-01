import utime

print("ok")
utime.sleep(1)
print("delay de 1")
from machine import Pin # importe dans le code la lib qui permet de gerer les Pins de sortie
import utime # importe dans le code la lib qui permet de gerer le temps

pinNumber = 17 # declaration d'une variable pinNumber à 17
pinNumber2 = 14
pinNumber3 = 10

led = Pin(pinNumber, mode=Pin.OUT)# declaration d'une variable de type pin ici la 17                                    #et on prescise que c'est une pin de sortie de courant (OUT)
led2 = Pin(pinNumber2, mode=Pin.OUT) #Couleur numéro 2 
led3 = Pin(pinNumber3, mode=Pin.OUT) #Couleur numéro 3

while True:          # boucle infini
    led.toggle()     # change l'etat de la led
    utime.sleep(0.2) #0.2 secondes de différences
    led2.toggle()
    utime.sleep(0.3) #0.3 secondes de différences
    led3.toggle()
    utime.sleep(0.2) #0.2 secondes de differneces
    # attendre 1 seconde 
    #led.on()        allume la led 
    #led.off()       eteind la led  