import os
from shutil import rmtree, copyfile

root   = "test_folder"
source = root + "/source"
target = root + "/target"

rmtree("test_folder")

os.mkdir(root)
os.mkdir(source)
os.mkdir(target)

for folder in ["source1", "source2"]:
    os.mkdir(source + "/" + folder)
    for file_name in ["file1", "file2", "file3"]:
        path = os.path.join(source, folder, file_name)
        with open(path, "w") as f:
            f.write("okkk")
copyfile("../../Documents/PUNCH/CUb_Mx_chargt_L546_CaseC_HEXA.pch", source + "/file.pch")

for folder in ["source1"]:
    os.mkdir(target + "/" + folder)
    os.mkdir(target + "/ok")
    path = os.path.join(target, "ok", "fiiile")
    with open(path, "w") as f:
        f.write("okkk")
    for file_name in ["file1"]:
        path = os.path.join(target, folder, file_name)
        with open(path, "w") as f:
            f.write("okkk")
copyfile("../../Documents/PUNCH/CUb_Mx_chargt_L546_CaseC_GRID.pch", target + "/file2.pch")
