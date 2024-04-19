import RPi.GPIO as GPIO
import time
import threading

# Importer le module pour exécuter le code en parallèle
from concurrent.futures import ThreadPoolExecutor

# Définir les broches GPIO pour les feux de signalisation
RED_PIN1 = 21
RED_PIN2 = 20

Y_PIN1 = 16
Y_PIN2 = 12


# Initialiser la bibliothèque GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_PIN1, GPIO.OUT)
GPIO.setup(RED_PIN2, GPIO.OUT)
GPIO.setup(Y_PIN1, GPIO.OUT)
GPIO.setup(Y_PIN2, GPIO.OUT)

def transition_lights():
    time.sleep(1)
    all_lights_off()
    
def all_lights_off():
    GPIO.output(RED_PIN1, GPIO.LOW)
    GPIO.output(RED_PIN2, GPIO.LOW)
    GPIO.output(Y_PIN1, GPIO.LOW)
    GPIO.output(Y_PIN2, GPIO.LOW)

def traffic_light_cycle():
    try:
        while True:
            # Feu rouge
            GPIO.output(RED_PIN1, GPIO.HIGH)
            GPIO.output(RED_PIN2, GPIO.HIGH)
            time.sleep(5)

            # Feu rouge clignotant (transition)
            GPIO.output(RED_PIN1, GPIO.LOW)
            GPIO.output(RED_PIN2, GPIO.LOW)
            time.sleep(1)
            
            transition_lights()
            
           # Feu rouge
            GPIO.output(Y_PIN1, GPIO.HIGH)
            GPIO.output(Y_PIN2, GPIO.HIGH)
            time.sleep(5)

            # Feu rouge clignotant (transition)
            GPIO.output(Y_PIN1, GPIO.LOW)
            GPIO.output(Y_PIN2, GPIO.LOW)
            time.sleep(1)

            # Réinitialiser tous les feux
            all_lights_off()

    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    traffic_light_cycle()
