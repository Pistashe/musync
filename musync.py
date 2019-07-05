import argparse

parser = argparse.ArgumentParser()
parser.add_argument("source",
                    help   = "Source folder to synchronize",
                    type   = str)
parser.add_argument("target",
                    help   = "Target folder to synchronize",
                    type   = str)
parser.add_argument("-v", "--verbose",
                    help   = "Print more information",
                    action = "store_true")
parser.add_argument("-f", "--force",
                    help   = "Force the operations without asking for "\
                             "confirmation",
                    action = "store_true")
parser.add_argument("-d", "--delete",
                    help   = "If target's files that do not exist in source "\
                             "folder should be erased",
                    action = "store_true")

args = parser.parse_args()

print(args)
