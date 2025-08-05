from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.textfield import MDTextField

# Exemplo de uma calculadora de IMC (Índice de Massa Corporal) usando KivyMD
# IMC = peso / (altura ** 2)

class IMCApp(MDApp):
    def build(self):
        self.tela = Screen()
        
        barra_titulo = MDTopAppBar(
            title="Calculadora de IMC",
            pos_hint={"top": 1},
            elevation=4,
        )

        self.peso_input = MDTextField(
            hint_text='Digite seu peso (kg)',
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            size_hint_x=0.8,
            mode="rectangle"
            # password = true
        )

        botao_calcular = MDRaisedButton(
            text="Calcular IMC",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            on_release=self.calcular_imc
        )

        self.altura_input = MDTextField(
            hint_text="Digite sua altura (m)",
            pos_hint={"center_x": 0.5, "center_y": 0.6},
            size_hint_x=(0.8),
            mode="rectangle",
            # mode="round"
            # mode="fill"
        )

        self.resultado_label = MDLabel(
            text="Seu IMC aparecerá aqui",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            on_release=self.calcular_imc
        )

        botao_limpar = MDRaisedButton(
            text="Limpar",
            pos_hint={"center_x": 0.5, "center_y": 0.25},
            on_release=self.limpar_campos
        )

        self.tela.add_widget(barra_titulo)
        self.tela.add_widget(self.peso_input)
        self.tela.add_widget(self.altura_input)
        self.tela.add_widget(self.resultado_label)
        self.tela.add_widget(botao_limpar)
        self.tela.add_widget(botao_calcular)

        return self.tela
    
    def calcular_imc(self, instance):
        try:
            peso = float(self.peso_input.text)
            altura = float(self.altura_input.text)
            imc = peso / (altura ** 2)

            categoria =  self.classificar_imc(imc)
            self.resultado_label.text = f"Seu IMC é: {imc:.2f} - {categoria}"
        except:
            self.resultado_label.text = "Por favor, insira valores válidos."
    def classificar_imc(self, imc):
        if imc < 18.5:
            return "Abaixo do peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidade"
    def limpar_campos(self, instance):
        self.peso_input.text = ""
        self.altura_input.text = ""
        self.resultado_label.text = "Seu IMC aparecerá aqui"

IMCApp().run()