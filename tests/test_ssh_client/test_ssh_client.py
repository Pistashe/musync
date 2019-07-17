""" Unit tests of the ssh_client module.
"""
import os
import sys
import pytest

sys.path.append("./")

from ssh_client import SSHClient

DIR_PATH = os.path.abspath(os.path.dirname(__file__))

@pytest.fixture
def ssh_client():
    return SSHClient("sgiorno", "192.168.122.1", 22, "babibel123")

def test_execute(ssh_client):
    expected = sorted(os.listdir(DIR_PATH))
    output = sorted(ssh_client.execute("ls {}".format(DIR_PATH)))

    assert output == expected
