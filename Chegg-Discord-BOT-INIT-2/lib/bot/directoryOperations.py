from shutil import rmtree
from os import listdir


def deleteDir(dir_name):
    rmtree(dir_name)


def scanDir(path):
    files = listdir(path)
    for file in files:
        q = file[0]
        if q == "q":
            return file

def scanTheDir(path):
    files = listdir(path)
    fullPathFileList = []
    for file in files:
        fileName = r"{0}\{1}".format(path,file)
        fullPathFileList.append(fileName)
    return fullPathFileList