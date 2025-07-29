from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class ExemploCardApp(MDApp):
    def build(self):
        layout = Screen()

        painel = MDCard(
            orientation="vertical",
            size_hint=(None, None),
            size=(400, 300),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            padding=20,
            elevation=8,
            md_bg_color=(0.9, 0.9, 0.9, 1)
        )
        