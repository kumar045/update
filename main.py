__version__ = '1.0.0'
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.audio import SoundLoader


class HelloCodi(MDApp):
    def build(self):
        return Builder.load_file('assets/main.kv')
    def buzz(self, *args):
        sound = SoundLoader.load('assets/Bee-Sound.mp3')
        if sound:
            sound.play()

HelloCodi().run()        