# coding: utf-8

# Udemy - 03/03/2017
# Hello World em Kivy - Aula 80

from kivy.app import App
from kivy.uix.label import Label

def build():
    return Label(text="Hello World")

hello_world = App()
hello_world.build = build
hello_world.run()