from kivy.uix.label import Label
from kivy.properties import ListProperty

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string("""
<LabelB>:
  background_color: 0, 0, 0, 1
  canvas.before:
    Color:
      rgba: self.background_color
    Rectangle:
      pos: self.pos
      size: self.size
""")

class LabelB(Label):
  background_color = ListProperty([0,0,0,1])

Factory.register('KivyB', module='LabelB')
