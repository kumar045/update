__version__ = '1.0.0'
import os
os.environ['KIVY_AUDIO'] = 'ffpyplayer'
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.audio import SoundLoader


class HelloCodi(MDApp):
    def build(self):
        return Builder.load_file('assets/main.kv')
    def buzz(self, *args):
        sound = SoundLoader.load('assets/Bee-Sound.mp3')
        sound.play()

HelloCodi().run()        