from kivy.app import App #importe la bibliothèque graphique kivy
from kivy.uix.button import Button #importe le bouton pour l'interface
import RPi.GPIO as GPIO #importe la bibliotheque pour controler la carte

LED = 17 #numéro de broche GPIO pour la LED
GPIO.setmode(GPIO.BOARD) #utilisation de la numérotation BOARD pour les broche
GPIO.setup(LED, GPIO.OUT)  #configuration de la broche LED en sortie

class BoutonApp(App): #définition de la classe principale de l'application
  def build(self): #contruit l'interface du bouton
    self.led_state = False #état initial de la LED # Initialisation de l'état de la LED 
    self.button = Button(text="Allumer la LED", font_size=24, on_press=self.toggle_led) #création d'un bouton interactif avec texte
    return self.button #retourne le bouton
  def toggle_led(self, instance): #change d'état lors d'un appui sur le bouton
    self.led_state = not self.led_state #inverse létat de la led
    GPIO.output(LED, self.led_state) #applique l'état à la broche GPI
    instance.text = "Éteindre la LED" if self.led_state else "Allumer la LED" #change le texte en fonction de l'état de la led

def on_stop(self): #fonction appelé à l'arret de l'application
    GPIO.cleanup() #nettoie les GPIO



def destroy():
    #Turn Off LED
    #GPIO.output(ledPin, GPIO.LOW)
    #Release resource
    GPIO.cleanup()

#If run this script directly, do:
if __name__ == '__main__':
    destroy()
    try:
        ButtonApp().run()
    #When 'Ctrl+C' is pressed, the child program 
    # destroy() will be  executed
    except KeyboardInterrupt:
        destroy()
    finally:
        print("destroy")
        destroy()
