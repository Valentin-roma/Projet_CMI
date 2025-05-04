from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_on_touch')
Config.set('input', 'touch', 'hidinput')

from kivy.app import App
from kivy.uix.button import Button

import RPi.GPIO as GPIO

# Configuration du GPIO
buzz = 11 # Modifier si nécessaire
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buzz, GPIO.OUT)

class BuzzApp(App):
    def build(self):
        self.buzz_state = False # État initial du buzzer
        self.button = Button(text="Allumer le buzzer", font_size=24, on_press=self.toggle_buzz)
        return self.button
    def toggle_buzz(self, instance):
        self.buzz_state = not self.buzz_state
        GPIO.output(buzz, self.buzz_state)
        instance.text = "Éteindre le buzzer" if self.buzz_state else "Allumer le buzzer"

def on_stop(self):
    GPIO.cleanup() # Nettoie les GPIO à la fermeture

if __name__ == "__main__":
    BuzzApp().run()
