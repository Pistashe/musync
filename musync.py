import argparse

from config import Config
from folder import Folder
from sync   import Sync

# DEFAULT_PORT     = "2222"
# DEFAULT_IP       = "10.63.209.126"
# DEFAULT_USERNAME = "admin"
DEFAULT_PORT     = "22"
DEFAULT_IP       = "127.0.0.1"
DEFAULT_USERNAME = "sgiorno"

parser = argparse.ArgumentParser()
parser.add_argument("source",
                    help    = "Source folder to synchronize",
                    type    = str)
parser.add_argument("target",
                    help    = "Target folder to synchronize",
                    type    = str)
parser.add_argument("-v", "--verbose",
                    help    = "Print more information",
                    action  = "store_true")
parser.add_argument("-f", "--force",
                    help    = "Force the operations without asking for "\
                              "confirmation",
                    action  = "store_true")
parser.add_argument("-d", "--delete",
                    help    = "If target's files that do not exist in source "\
                              "folder should be erased",
                    action  = "store_true")
parser.add_argument("-t", "--default",
                    help    = "Use the default values: "\
                              "admin@10.63.209.126:2222",
                    action  = "store_true")
parser.add_argument("-u", "--username",
                    help    = "Username to connect by ssh",
                    type    = str,
                    default = None)
parser.add_argument("-i", "--ip",
                    help    = "IP address to connect to",
                    type    = str,
                    default = None)
parser.add_argument("-p", "--port",
                    help    = "Port to connect onto",
                    type    = str,
                    default = None)

args = parser.parse_args()
if args.default:
    args.port     = DEFAULT_PORT
    args.ip       = DEFAULT_IP
    args.username = DEFAULT_USERNAME

options = vars(args)

config = Config(args.username, args.ip, args.port)
config.execute("ls -l")
sftp = config._client.open_sftp()
sftp.put("./test_folder/source/file.pch", "./ok")
# sftp.close()
# source = Folder(args.source)
# target = Folder(args.target)
# sync   = Sync(source, target, config, options)
