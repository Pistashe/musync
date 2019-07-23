import kivy
# from kivy.uix.filechooser import FileSystemAbstract
from filechooser import FileSystemAbstract
from os.path import basename

kivy.require('1.9.2')

class FileSystemRemote(FileSystemAbstract):
    '''Implementation of :class:`FileSystemAbstract` for remote files
       over ssh connexion.
    '''

    def __init__(self, ssh_client):
        self._ssh_client = ssh_client

    @property
    def ssh_client(self):
        return _ssh_client

    @ssh_client.setter
    def ssh_client(self, ssh_client):
        self._ssh_client = ssh_client

    def listdir(self, fn):
        files = self._ssh_client.execute("ls {}".format(fn))
        return files

    def getsize(self, fn):
        size = self._ssh_client.execute('stat --printf="%s" {}'.format(fn))
        size = int(size[0])
        return size

    def is_hidden(self, fn):
        return basename(fn).startswith('.')

    def is_dir(self, fn):
        ls_output = self._ssh_client.execute("ls {}".format(fn))
        try:
            return ls_output[0] != fn
        except IndexError:
            return True

    def get_icon(self, fn):
        return 'none'
