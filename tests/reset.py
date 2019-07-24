import os
from shutil import rmtree, copyfile

root   = "environnement"
source = root + "/source"
target = root + "/target"

rmtree(root)

os.mkdir(root)
os.mkdir(source)
os.mkdir(target)

for folder in ["folder1", "folder2"]:
    os.mkdir(source + "/" + folder)
    for file_name in ["file1", "file2", "file3"]:
        path = os.path.join(source, folder, file_name)
        with open(path, "w") as f:
            f.write("okkk")

# pch_path = "/home/sgiorno/Documents/PUNCH"
# for file_ in os.listdir(pch_path):
#     copyfile("{}/{}".format(pch_path, file_), "{}/{}".format(source, file_))

for folder in ["folder1"]:
    os.mkdir(target + "/" + folder)
    os.mkdir(target + "/ok")
    path = os.path.join(target, "ok", "fiiile")
    with open(path, "w") as f:
        f.write("okkk")
    for file_name in ["file1"]:
        path = os.path.join(target, folder, file_name)
        with open(path, "w") as f:
            f.write("okkk")

os.system("chmod -R a+rwx {}".format(root))
