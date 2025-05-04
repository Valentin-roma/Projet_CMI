from kivy.app import App     #Importe la classe de base pour une application Kivy
from kivy.uix.button import Button     #Importe le widget bouton
import RPi.GPIO as GPIO     #Importe la bibliothèque GPIO pour contrôler les broches du Raspberry Pi

# Configuration du GPIO   
buzz = 11    #Numéro de la broche utilisée pour le buzzer (en mode BOARD)  
GPIO.setmode(GPIO.BOARD)    #Utilise la numérotation physique des broches
GPIO.setup(buzz, GPIO.OUT)    #Configure la broche comme une sortie

class BuzzApp(App):
    def build(self):
        self.buzz_state = False    #État initial du buzzer (éteint)
        #Création du bouton avec un texte et une taille de police, et liaison de l'action au clic
        self.button = Button(text="Allumer le buzzer", font_size=24, on_press=self.toggle_buzz) 
        return self.button    #Retourne le bouton comme widget principal

    def toggle_buzz(self, instance):    #Inverse l'état du buzzer (ON/OFF)
        self.buzz_state = not self.buzz_state    #Met à jour la sortie GPIO en fonction de l'état
        GPIO.output(buzz, self.buzz_state)    #Met à jour le texte du bouton en fonction de l'état du buzzer
        instance.text = "Éteindre le buzzer" if self.buzz_state else "Allumer le buzzer"

#Nettoyage des GPIO à la fermeture de l'application
def on_stop(self):
    GPIO.cleanup()    #Nettoie les GPIO à la fermeture

#Lancement de l'application si le script est exécuté directement
if __name__ == "__main__":
    BuzzApp().run()
