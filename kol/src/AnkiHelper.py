
from aqt import mw

from anki.utils import joinFields, splitFields
from anki.utils import ids2str

from .utils import log


class AnkiCard:
    def __init__(self, ivl):
        self.ivl = ivl
        
class AnkiNote:
    def __init__(self, id, fields, mid):
        self.id = id
        
        self.fields = splitFields(fields)
        self._model = mw.col.models.get(mid)
        self._fmap = mw.col.models.fieldMap(self._model)
           
    # Dict interface
    ##################################################

    def keys(self):
        return list(self._fmap.keys())

    def values(self):
        return self.fields

    def items(self):
        return [(f['name'], self.fields[ord])
                for ord, f in sorted(self._fmap.values())]

    def _fieldOrd(self, key):
        try:
            return self._fmap[key][0]
        except:
            raise KeyError(key)

    def __getitem__(self, key):
        return self.fields[self._fieldOrd(key)]

    def __setitem__(self, key, value):
        self.fields[self._fieldOrd(key)] = value

    def __contains__(self, key):
        return key in list(self._fmap.keys())


class AnkiHelper:

    @staticmethod
    def getDidsFromName(name):
        did = mw.col.decks.id(name, False)
        if did == None:
            return None
        dids = [did]
        for name, id in mw.col.decks.children(did):
            dids.append(id)
        return dids
    
    @staticmethod
    def getCards(dids):
        log("getCards")
        log(ids2str(dids))

        rows = mw.col.db.all("Select c.ivl, n.id, n.flds, n.mid from cards c, notes n "
                             "Where c.nid = n.id and c.did in " + ids2str(dids))
        ankiCards = list()
        for row in rows:
            ankiCard = AnkiCard(row[0])
            ankiCard.note = AnkiNote(row[1], row[2], row[3])
            ankiCards.append(ankiCard)

        return ankiCards

    @staticmethod
    def getNotes(dids):
        rows = mw.col.db.all("Select n.id, n.flds, n.mid from cards c, notes n "
                             "Where c.nid = n.id and c.did in " + ids2str(dids))
        ankiNotes = list()
        for row in rows:
            ankiNotes.append(AnkiNote(row[0], row[1], row[2]))

        return ankiNotes

    @staticmethod
    def isDeckModified(dlmod, nlmod, clmod, deck):
        if dlmod != deck["mod"]:
            return True
        did = deck["id"]
        return mw.col.db.first("select * From Notes n, Cards c "
            "where c.nid = n.id and (n.mod > ? or c.mod > ?) and c.did = ? limit 1", nlmod, clmod, did) != None
    
    @staticmethod
    def getLastModified(did):
        maxes = mw.col.db.first("Select max(n.mod), max(c.mod) from Notes n, Cards c Where c.nid = n.id and c.did = ?", did)
        return maxes[0], maxes[1]
