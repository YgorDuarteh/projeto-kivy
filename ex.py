from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class ExemploApp(MDApp):
    def build(self):
        tela = Screen()

        barra_titulo = MDTopAppBar(
            title="Hello World",
            pos_hint={"top": 1},
            elevation=4
        )

        self.texto = MDLabel(
            text="Olá, Bem vindo ao KivyMD!",
            halign="center",
            pos_hint={"center_y": 0.5}
        )

        self.texto2 = MDLabel(
            text="Este é um exemplo simples de aplicação.",
            halign="center",
            pos_hint={"center_y": 0.4}
        )

        botao = MDRaisedButton(
            text="Clique aqui",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            on_release=self.ao_clicar
        )

        btnlimpar = MDRaisedButton(
            text="Limpar",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            on_release=self.limpar
        )

        tela.add_widget(barra_titulo)
        tela.add_widget(self.texto)
        tela.add_widget(self.texto2)
        tela.add_widget(botao)
        tela.add_widget(btnlimpar) 

        return tela
    
    def ao_clicar(self, instance):
        instance.text = "Você clicou no botão!"

    def limpar(self, instance):
        self.texto.text = ""
        self.texto2.text = ""

ExemploApp().run()