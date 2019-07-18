"""
Simple GUI to easily synchronize music files between two devices
using rsync.
"""
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from ssh_client import SSHClient
from file_system_remote import FileSystemRemote
import subprocess as sp
import re

kivy.require("1.9.1")


SOURCE_PATH = "/home/sgiorno/musync_env/musync/tests/environnement/source"
TARGET_PATH = "/home/sgiorno/musync_env/musync/tests/environnement/target"

def _find_text_between_patterns(text, pat1, pat2):
    return re.findall(r'{}(.*?){}'.format(pat1, pat2), text)

def _parser(text):
    print(_find_text_between_patterns(text, "cd+++++++++", "\n"))

# class in which we are creating the button
class Musync(App):
    def build(self):
        # layout = BoxLayout(orientation='horizontal')
        layout = GridLayout(rows=2)
        lab1 = Label(text="Local" , height=30, bold=True, size_hint_y=None)
        lab2 = Label(text="Remote", height=30, bold=True, size_hint_y=None)
        layout.add_widget(lab1)
        layout.add_widget(lab2)
        ssh_client = SSHClient("sgiorno", "192.168.122.1", 22, "babibel123")
        file_system_remote = FileSystemRemote(ssh_client)
        file_chooser_source = FileChooserListView(path=SOURCE_PATH)
        file_chooser_target = FileChooserListView(file_system=file_system_remote,
                                                  path=TARGET_PATH)
        # proc = sp.Popen(["rsync", "-ain", "--del", SOURCE_PATH,
        #          "sgiorno@192.168.122.1:{}".format(TARGET_PATH)],
        #         stdout=sp.PIPE)
        # text = proc.communicate()[0]
        # text = text.decode("utf-8")
        # print(text)
        # _parser(text)
        layout.add_widget(file_chooser_source)
        layout.add_widget(file_chooser_target)
        btn = Button(text="Push Me !",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(300, 250))

        btn.bind(on_press=self.callback)
        # self.load_kv("ui.kv")
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
