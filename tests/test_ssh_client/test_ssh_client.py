""" Unit tests of the ssh_client module.
"""
import os
import sys
import pytest

sys.path.append("./")

from ssh_client import SSHClient
from local_config import UNAME, IP, PORT, PWD

DIR_PATH = os.path.abspath(os.path.dirname(__file__))

@pytest.fixture
def ssh_client():
    return SSHClient(UNAME, IP, PORT, PWD)

def test_execute(ssh_client):
    expected = sorted(os.listdir(DIR_PATH))
    output = sorted(ssh_client.execute("ls {}".format(DIR_PATH)))

    assert output == expected
