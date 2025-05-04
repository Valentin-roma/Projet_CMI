import RPi.GPIO as GPIO
import time
import threading
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

CLK = 12    #Broche pour le signal de l'horloge
DT = 11    #Broche pour le signal de données
SW =13    #Broche pour le bouton poussoir


def setup():
    GPIO.setmode(GPIO.BOARD)    #Utilise la numérotation physique des broches
    GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #Entrée avec résistance pull-up
    GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #Entrée avec résistance pull-up
    GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)    #Entrée avec résistance pull-up
    compteur = 0
    last_clk_state = GPIO.input(CLK)


import RPi.GPIO as GPIO
from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock

# --- Broches GPIO ---
CLK = 17
DT = 18
SW = 27

# --- Setup GPIO ---
GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# --- Variables ---
counter = 0
last_clk_state = GPIO.input(CLK)

class EncoderApp(App):
    def build(self):
        self.label = Label(text="0", font_size=1500)
        # Appelle update() toutes les 10 ms
        Clock.schedule_interval(self.update, 0.01)
        return self.label

    def update(self, dt):
        global counter, last_clk_state

        clk_state = GPIO.input(CLK)
        dt_state = GPIO.input(DT)
        sw_state = GPIO.input(SW)

        if clk_state != last_clk_state:
            if dt_state != clk_state:
                counter += 1
            else:
                counter -= 1
            self.label.text = str(counter)
            last_clk_state = clk_state

        if sw_state == GPIO.LOW:
            counter = 0
            self.label.text = "0"

    def on_stop(self):
        GPIO.cleanup()

if __name__ == '__main__':
    EncoderApp().run()
