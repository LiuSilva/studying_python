# coding: utf-8
# Udemy - 19/04/2017
# usando OO no código basico para criar a janela

from kivy.app import App
from kivy.uix.label import Label

# metodo antigo
'''
def build():
    return Label(text="Label Teste")

janela = App()
janela.build = build
janela.run()
'''

# usando OO

class MeuPrograma(App): # herda da classe App

    def build(self): # subscreve a funcao build
        return Label(text="Label Teste")

MeuPrograma().run()