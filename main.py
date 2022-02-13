__version__ = '1.0.0'
from kivymd.app import MDApp
from kivy.lang import Builder
from playsound import playsound


class HelloCodi(MDApp):
    def build(self):
        return Builder.load_file('assets/main.kv')
    def buzz(self, *args):
        playsound('assets/Bee-Sound.mp3')


HelloCodi().run()        