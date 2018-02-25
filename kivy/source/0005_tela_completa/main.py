# coding: utf-8
# Udemy - 19/04/2017
# Usando Layout para colocar varios componentes na tela

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def click():
    print(ed.text)

def build():

    layout = FloatLayout()

    ed = TextInput(text="eXcript")
    # vai definir ed como global, mas isso é uma ma pratica definir a variavel
    # como escopo global ao inves de passar como argumento de funcao
    # mas para facilitar o estudo vai colocar a variavel como global
    global ed
    ed.size_hint = None, None # ainda nao tem explicacao, vai ser dada depois
    ed.height = 300
    ed.width = 400
    ed.x = 100
    ed.y = 250

    bt = Button(text="Clique Aqui")
    bt.size_hint = None, None  # ainda nao tem explicacao, vai ser dada depois
    bt.height = 50
    bt.width = 200
    bt.y = 150
    bt.x = 210

    bt.on_press = click

    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout

janela = App()
janela.title = "Titulo da Aplicacao"

# alterar dimensao da janela
from kivy.core.window import Window
Window.size = 600, 600 # passa uma tupla

janela.build = build
janela.run()