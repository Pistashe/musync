import paramiko
import getpass


class Config():
    def __init__(self, uname=None, ip=None, port=None):
        self._uname = input("Username (admin): ") if uname is None else uname
        self._ip = ip
        while not _is_valid_ip(self._ip):
            self._ip = input("IP address: ")
        self._port = port
        while not _is_valid_port(self._port):
            self._port = input("Port: ")
        self._pwd = getpass.getpass()

        self._client = None
        self._sftp = None

        self.connect()

    @property
    def uname(self):
        return self._uname

    @uname.setter
    def uname(self, uname):
        self._uname = uname

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, ip):
        self._ip = ip

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        self._port = port

    def connect(self):
        self._client = paramiko.SSHClient()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._client.connect(self._ip, port=self._port, username=self._uname,
                             password=self._pwd)
        self._sftp = self._client.open_sftp()

    def execute(self, cmd, print_res=True):
        if self._client is None:
            raise ConnectionError("No SSH client configured.")
        stdin, stdout, stderr = self._client.exec_command(cmd)
        if print_res:
            for line in stdout.read().splitlines():
                print (line)


    def close(self):
        if self._sftp is not None:
            self._sftp.close()
        if self._client is not None:
            self._client.close()

    def __del__(self):
        self.close()


def _is_valid_ip(ip):
    try:
        ip = ip.split(".")
        if len(ip) != 4:
            return False
        for part in ip:
            part_int = int(part)
            if part_int > 255 or part_int < 0:
                return False
        return True
    except:
        return False


def _is_valid_port(port):
    try:
        if int(port) > 10000:
            return False
        return True
    except:
        return False

if __name__ == "__main__":
    test = Config()
    test.execute("ls")
