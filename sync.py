import os
import filecmp
# from   folder import Folder

class Sync():
    def __init__(self, source, target, config=None, options={"remove":False,
                                                             "verbose":True,
                                                             "confirmation":True}):
        self._config  = config
        self._source  = source
        self._target  = target
        self._options = options

    @property
    def config(self):
        return self._config
    @config.setter
    def config(self, config):
        self._config = config

    @property
    def source(self):
        return self._source
    @source.setter
    def source(self, source):
        self._source = source

    @property
    def target(self):
        return self._target
    @target.setter
    def target(self, target):
        self._target = target

    @property
    def options(self):
        return self._options
    @options.setter
    def options(self, options):
        self._options = options

    def find_files_to_sync(self):
        source_files = self._source.files_list()
        target_files = self._target.files_list()

        files_to_add = []
        for f_src in source_files:
            f_src_abs = self._source.path.joinpath(f_src)
            to_add = True
            for f_trg in target_files:
                if f_src in target_files:
                    f_trg_abs = self._target.path.joinpath(f_trg)
                    if filecmp.cmp(f_src_abs, f_trg_abs):
                        to_add = False
                        break
            if to_add:
                files_to_add.append(f_src)

        files_to_del = []
        if self._options["remove"]:
            for f_trg in target_files:
                if f_trg not in source_files:
                    files_to_del.append(f_trg)

        return files_to_add, files_to_del

    def synchronize(self):
        files_to_add, files_to_del = self.find_files_to_sync()
        n_fta, s_fta, n_ftd, s_ftd = self._get_infos(files_to_add,files_to_del)

        print("{} files to add ({}) ; {} files to remove ({})."\
              .format(n_fta, s_fta, n_ftd, s_ftd))

        go_ahead = _ask_for_confirmation(self._options["confirmation"])
        if go_ahead:
            verbose = self._options["verbose"]
            for f in files_to_add:
                self._target.copy_file(self._source.path, f, verbose)
            for f in files_to_del:
                self._target.remove_file(f, verbose)

            print("{} files added ({}) ; {} files removed ({})."\
                  .format(n_fta, s_fta, n_ftd, s_ftd))


    def _get_infos(self, fta, ftd):
        n_fta = len(fta) ; n_ftd = len(ftd)
        s_a = sum([self._source.path.joinpath(f).stat().st_size for f in fta])
        s_d = sum([self._target.path.joinpath(f).stat().st_size for f in ftd])

        s_a_formatted = _byte_conversion(s_a)
        s_d_formatted = _byte_conversion(s_d)

        return n_fta, s_a_formatted, n_ftd, s_d_formatted

def _ask_for_confirmation(ask_for=False):
    go_ahead = True
    if ask_for:
        go_ahead = input("Do you want to continue ? (Y/n) ")
        go_ahead = go_ahead.lower() == "y"
    return go_ahead

def _byte_conversion(byte, n_decimal=1):
    if byte > 1e6:
        return str(round(byte/1e6, n_decimal)) + " mB"
    elif byte > 1e3:
        return str(round(byte/1e3, n_decimal)) + " kB"
    else:
        return str(byte) + " B"
