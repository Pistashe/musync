"""
Simple GUI to easily synchronize music files between two devices
using rsync.
"""
import os
import re
import shlex
import pathlib
import subprocess as sp

# os.environ["KIVY_NO_CONSOLELOG"] = "1"

import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.splitter import Splitter
# from kivy.uix.filechooser import FileChooserListView
from filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from utils import find_text_between_patterns, popen_and_call
from ssh_client import SSHClient
from file_system_remote import FileSystemRemote

from local_config import UNAME, IP, PORT, PWD, SOURCE_PATH, TARGET_PATH

kivy.require("1.9.1")

def _parser(text):
    plus = "\+\+\+\+\+\+\+\+\+ "
    dirs_to_create = find_text_between_patterns(text,
                                                "cd{}".format(plus), "\n")
    files_to_create = find_text_between_patterns(text,
                                                 "\<f{}".format(plus), "\n")
    to_del = find_text_between_patterns(text, "\*deleting   ", "\n")

    return dirs_to_create, files_to_create, to_del

# class in which we are creating the button
class Musync(App):
    def build(self):
        self.load_kv("test.kv")
        layout = BoxLayout(orientation='vertical')
        splitter_layout = BoxLayout(orientation='horizontal')
        lab1 = Label(text="Local" , height=30, bold=True, size_hint_y=None)
        lab2 = Label(text="Remote", height=30, bold=True, size_hint_y=None)
        source_layout = BoxLayout(orientation='vertical')
        target_layout = BoxLayout(orientation='vertical')
        ssh_client = SSHClient(UNAME, IP, PORT, PWD)
        file_system_remote = FileSystemRemote(ssh_client)
        self.file_chooser_source = FileChooserListView(rootpath=SOURCE_PATH)
        self.file_chooser_target = FileChooserListView(file_system=file_system_remote,
                                                  rootpath=TARGET_PATH)
        source_layout.add_widget(lab1)
        source_layout.add_widget(self.file_chooser_source)
        target_layout.add_widget(lab2)
        target_layout.add_widget(self.file_chooser_target)
        splitter = Splitter(sizable_from='right')
        splitter.add_widget(source_layout)
        splitter_layout.add_widget(splitter)
        splitter_layout.add_widget(target_layout)
        btn = Button(text="Sync it !",
                     font_size="20sp",
                     background_color=(0, 1, 0, 1),
                     color=(1, 1, 1, 1),
                     height=30,
                     size_hint_y=None)

        btn.bind(on_press=self.sync)
        # layout.add_widget(btn)
        self.layout = layout
        self.btn = btn
        self.update_view(None)
        layout.add_widget(splitter_layout)
        layout.add_widget(btn)
        return layout

    def display_while_waiting(self, *args):
        from kivy.clock import Clock
        self.layout.add_widget(Label(text="hehe"))

    def sync(self, event):
        cmd = "rsync -ai --del -e 'ssh -p {}' {} {}@{}:{}"\
              .format(PORT, SOURCE_PATH, UNAME, IP, TARGET_PATH)
        cmd = shlex.split(cmd)
        popen_and_call(self.update_view, cmd)

    def _update_view_source(self, sync_state):
        dtc, ftc, td = _parser(sync_state)
        self.file_chooser_source.file_system.remote_files = dtc + ftc + td
        self.file_chooser_source._trigger_update()

    def _update_view_target(self):
        self.file_chooser_target._update_files()

    def update_sync_state(self):
        cmd = "rsync -ain --del -e 'ssh -p {}' {} {}@{}:{}"\
              .format(PORT, SOURCE_PATH, UNAME, IP, TARGET_PATH)
        cmd = shlex.split(cmd)
        popen_and_call(self._update_view_source, cmd)

    def update_view(self, text):
        self._update_view_target()
        self.update_sync_state()


    # callback function tells when button pressed
    def callback(self, event):
        sync(self)
    def callback2(self, event):
        pass

root = Musync()

root.run()
