import codecs
import os
import datetime

from aqt import mw

def log(msg):
    logPath = os.path.join(mw.pm.addonFolder(), 'kol', 'main.log')
    txt = '%s: %s' % (datetime.datetime.now(), msg)
    f = codecs.open(logPath, 'a', 'utf-8')
    f.write(txt + '\n')
    f.close()