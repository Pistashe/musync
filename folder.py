import os
from   shutil  import copyfile
from   pathlib import Path

class Folder():
    def __init__(self, path):
        self._path  = Path(path)

    @property
    def path(self):
        return self._path
    @path.setter
    def path(self, path):
        self._path = path

    def files_list(self):
        files = Path(self._path).glob("**/*")
        files = [f for f in files if not f.is_dir()]
        files = [f.relative_to(self.path) for f in files]
        return files

    def copy_file(self, src_path, f, verbose=False):
        src = src_path.joinpath(f)
        trg = self._path.joinpath(f)
        self._create_path_to_file(f)
        copyfile(src, trg)
        if verbose:
            print("copying  {} --> {}".format(src, trg))

    def remove_file(self, f, verbose=False):
        path = self._path.joinpath(f)
        os.remove(path)
        if verbose:
            print("removing {}".format(path))
        self.remove_empty_folders(path, verbose)

    def remove_empty_folders(self, path, verbose=False):
        parent = path.parent
        while len(os.listdir(parent)) == 0 and parent != Path("./"):
            os.rmdir(parent)
            if verbose:
                print("removing {}".format(parent))
            parent = parent.parent

    def _create_path_to_file(self, f):
        for part in f.parts[:-1]:
            full_path = self._path.joinpath(part)
            if not full_path.exists():
                os.mkdir(full_path)
