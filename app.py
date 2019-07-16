"""
Simple GUI to easily synchronize music files between two devices
using rsync.
"""
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout

kivy.require("1.9.1")


# class in which we are creating the button
class Musync(App):
    def build(self):
        layout = BoxLayout(orientation='horizontal')
        file_chooser_source = FileChooserListView(path="/home/sven")
        file_chooser_target = FileChooserListView()
        layout.add_widget(file_chooser_source)
        layout.add_widget(file_chooser_target)
        btn = Button(text="Push Me !",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(300, 250))

        # bind() use to bind the button to function callback
        btn.bind(on_press=self.callback)
        # return btn
        # return file_chooser_source#, file_chooser_target
        return layout

    # callback function tells when button pressed
    def callback(self, event):
        print("button pressed")
        print('Yoooo !!!!!!!!!!!')


# creating the object root for ButtonApp() class
root = Musync()

# run function runs the whole program
# i.e run() method which calls the target
# function passed to the constructor.
root.run()
