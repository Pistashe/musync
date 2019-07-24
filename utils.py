"""
    Bunch of useful and generic functions that are for the app.
"""
import re
import threading
import subprocess as sp


def find_text_between_patterns(text, pat1, pat2):
    """
    Returns all occurences of the text between two patterns.

    :param text: Text where to search
    :type  text: string
    :param pat1: Starting pattern
    :type  pat1: string
    :param pat2: Ending pattern
    :type  pat2: string

    :rtype: list of strings
    """
    return re.findall(r'{}(.*?){}'.format(pat1, pat2), text)


def popen_and_call(on_exit, popen_args):
    """
    Runs the given args in a subprocess.Popen, and then calls the function
    on_exit when the subprocess completes.
    on_exit is a callable object, and popenArgs is a list/tuple of args that
    would give to subprocess.Popen.

    :param on_exit: Callback function to execute after finishing the subprocess
    :type  on_exit: function
    :param popen_args: Command to run in a subprocess
    :type  popen_args: list of strings

    :rtype: :class:`thread.Thread`
    """
    def run_in_thread(on_exit, popen_args):
        proc = sp.Popen(popen_args, stdout=sp.PIPE, stderr=sp.PIPE)
        proc.wait()
        text = proc.communicate()[0].decode("utf-8")
        on_exit(sync_state=text)
        return
    thread = threading.Thread(target=run_in_thread, args=(on_exit, popen_args))
    thread.start()
    # returns immediately after the thread starts
    return thread
