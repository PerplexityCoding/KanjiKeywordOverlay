import codecs
import datetime
import os

from aqt import mw

def log(msg):
    logPath = os.path.join(mw.pm.addonFolder(), 'kol', 'main.log')
    txt = '%s: %s' % (datetime.datetime.now(), msg)
    f = codecs.open(logPath, 'a', 'utf-8')
    f.write(txt + '\n')
    f.close()

def readFile(path):
    try:
        f = open(path, mode="r", encoding="utf-8")
        res = f.read()
        f.close()
    except:
        res = None
    return res

def writeFile(path, obj):
    try:
        f = open(path, mode="w", encoding="utf-8")
        f.write(obj)
        f.close()
    except:
        pass