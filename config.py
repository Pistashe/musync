import getpass

class Config():
    def __init__(self, uname="admin", ip=None, port=2222):
        self._uname = input("Username: ")   if uname is None else uname
        self._ip    = ip
        while not _is_valid_ip(self._ip):
            self._ip    = input("IP address: ")
        self._port = port
        while not _is_valid_port(self._port):
            self._port  = input("Port: ")
        self._pwd   = getpass.getpass()

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
    a = Config()
