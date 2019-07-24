""" Unit tests of the file_system_remote module.
"""
import os
import sys
import pytest

sys.path.append("./")

from ssh_client import SSHClient
from widgets.file_system_remote import FileSystemRemote
from local_config import UNAME, IP, PORT, PWD

DIR_PATH = os.path.abspath(os.path.dirname(__file__))
FILE_PATH = os.path.abspath(__file__)


@pytest.fixture
def file_system_remote():
    ssh_client = SSHClient(UNAME, IP, PORT, PWD)
    return FileSystemRemote(ssh_client)


def test_listdir(file_system_remote):
    expected = sorted(os.listdir(DIR_PATH))
    output = sorted(file_system_remote.listdir(DIR_PATH))

    assert expected == output


def test_getsize(file_system_remote):
    expected = os.path.getsize(FILE_PATH)
    output = file_system_remote.getsize(FILE_PATH)

    assert expected == output


def test_is_hidden(file_system_remote):
    expected = os.path.basename(FILE_PATH).startswith(".")
    output = file_system_remote.is_hidden(FILE_PATH)

    assert expected == output


def test_is_dir(file_system_remote):
    expected = [os.path.isdir(FILE_PATH), os.path.isdir(DIR_PATH)]
    output = [file_system_remote.is_dir(FILE_PATH),
              file_system_remote.is_dir(DIR_PATH)]

    assert expected == output
