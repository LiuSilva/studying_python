# coding: utf-8
# Udemy - 03/03/2017
# Imprimindo textos com Kivy

from kivy.app import App
from kivy.uix.label import Label

def build():
    #return Label(text="Curso de Python e Kivy") # texto normal
    #return Label(text="Curso de Python e Kivy", italic=True) # texto com italico
    #return Label(text="Curso de Python e Kivy", italic=True, font_size=50) # fonte 50px
    lb = Label()
    lb.text="Curso de Python e Kivy"
    lb.italic=True
    lb.font_size=50
    return lb

app = App()

# atribuição de funcao, associa a funcao da funcao app com a funcao que criamos
app.build = build

app.run()