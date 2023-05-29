import shutil

def zipfile(path):
    shutil.make_archive(path,'zip','.')

zipfile("./teste")