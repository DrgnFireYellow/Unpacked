import requests
import sys
import json
import shutil
import uuid
import os
from zipfile import ZipFile


if __name__ == "__main__":
    filename = "Unpacked-" + str(uuid.uuid4())
    zipfilename = filename + ".zip"
    try:
        if not os.path.exists(sys.argv[1]):
            raise ()
        shutil.copy(sys.argv[1], zipfilename)
        zipfileobject = ZipFile(zipfilename)
        zipfileobject.extractall(filename)
        shutil.copytree(filename + "/overrides", filename + "/output")
        if not os.path.exists(filename + "/output/mods"):
            os.mkdir(filename + "/output/mods")
        if not os.path.exists(filename + "/output/shaderpacks"):
            os.mkdir(filename + "/output/shaderpacks")
        if not os.path.exists(filename + "/output/resourcepacks"):
            os.mkdir(filename + "/output/resourcepacks")
        indexfile = open(filename + "/modrinth.index.json")
        index = json.load(indexfile)
        for mod in index["files"]:
            pathtosavein = filename + "/output/" + mod["path"]
            jarfile = requests.get(mod["downloads"][0])
            save = open(pathtosavein, "xb")
            save.write(jarfile.content)
            save.close()
        os.remove(zipfilename)
    except:
        print("Please specify a Modrinth modpack .mrpack file")
        if os.path.exists(zipfilename):
            os.remove(zipfilename)
        quit()
