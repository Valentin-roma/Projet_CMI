import RPi.GPIO as GPIO #contrôle des GPIO du Raspberry Pi
from kivy.app import App #créer l'application Kivy
from kivy.uix.button import Button#importe le bouton pour l'interface graphique
from kivy.clock import Clock #importe Clock pour exécuter une fonction régulièrement


CLK = 12 #broche pour le signal de l'horloge
DT = 11 #broche pour le signal de données
SW =13 #broche pour le bouton poussoir

def setup():
    GPIO.setmode(GPIO.BOARD) #Utilise la numérotation physique des broches
    GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Entrée avec résistance pull-up
    GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Entrée avec résistance pull-up
    GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Entrée avec résistance pull-up
    self.counter = 0  #valeur initiale du compteur
    self.last_clk_state = GPIO.input(CLK)  #état initial de la broche CLK

class EncoderApp(App):
    def build(self): #contruit l'interface du bouton
        self.button = Button(text=str(self.counter), font_size=150) #création d'un bouton Kivy qui affiche la valeur du compteur
        Clock.schedule_interval(self.update, 0.01)#mise à jour toutes les 10ms
        return self.button #retourne le bouton
        
        
    def update(self, dt):
        clk_state = GPIO.input(CLK)# lit l'état actuel de CLK
        dt_state = GPIO.input(DT)  # lit l'état actuel de DT
        sw_state = GPIO.input(SW)  # lit l'état du bouton poussoir
        if clk_state != self.last_clk_state:#si l'état de CLK a changé
            if dt_state != clk_state: # si DT est différent de CLK, alors:
                counter += 1 #rotation dans un sens
            else:
                counter -= 1 #rotation dans l'autre sens
            self.btn.text = str(counter)#mise à jour du texte du bouton avec la nouvelle valeurdu compteur
            self.last_clk_state = clk_state #mémorise le nouvel état de CLK

        if sw_state == GPIO.LOW:#si le bouton est appuyé
            self.counter = 0 #réinitialise le compteur
            self.btn.text = "0" #met à zéro l'affichage

    def on_stop(self):
        GPIO.cleanup()

if __name__ == '__main__':
    EncoderApp().run()
