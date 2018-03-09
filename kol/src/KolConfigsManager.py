# -------------------------------------------------------------------------------
# -------------------------   Profile Manager  ----------------------------------
# -------------------------------------------------------------------------------
import pickle
import os

dir = os.path.dirname(__file__)
CONFIG_FILENAME = os.path.join(dir, "../data/KolConfig.profiles")

class KolConfig:
    def __init__(self,
                 profileName="",
                 kanjiDeckName="",
                 kanjiExpression="",
                 kanjiKeyword="",
                 kanjiOnYomi="",
                 kanjiOnYomiEnabled=True,
                 kanjiKunYomi="",
                 kanjiKunYomiEnabled=True,
                 kanjiMemoStory="",
                 kanjiMemoStoryEnabled=False,
                 kanjiCustomProfileEnabled=False,
                 kanjiDisplayWithFuriganaMod=True,
                 kanjiLoadDefaultValuesForNonExistingValues=False,
                 kanjiShowColorsForKnownKanji=True,
                 kanjiUseLink=False,
                 kanjiUseLinkUrl=""):

        self.profileName = profileName
        self.kanjiCustomProfileEnabled = kanjiCustomProfileEnabled
        self.kanjiDeckName = kanjiDeckName
        self.kanjiExpression = kanjiExpression
        self.kanjiKeyword = kanjiKeyword
        self.kanjiOnYomi = kanjiOnYomi
        self.kanjiOnYomiEnabled = kanjiOnYomiEnabled
        self.kanjiKunYomi = kanjiKunYomi
        self.kanjiKunYomiEnabled = kanjiKunYomiEnabled
        self.kanjiMemoStory = kanjiMemoStory
        self.kanjiMemoStoryEnabled = kanjiMemoStoryEnabled
        self.kanjiDisplayWithFuriganaMod = kanjiDisplayWithFuriganaMod
        self.kanjiLoadDefaultValuesForNonExistingValues = kanjiLoadDefaultValuesForNonExistingValues
        self.kanjiShowColorsForKnownKanji = kanjiShowColorsForKnownKanji
        self.kanjiUseLink = kanjiUseLink
        self.kanjiUseLinkUrl = kanjiUseLinkUrl

class KolConfigs:
    VERSION = 5

    def __init__(self):
        self.version = KolConfigs.VERSION
        self.allProfiles = dict()

    def update(self, newProfile):
        self.allProfiles.update({newProfile.profileName: newProfile})

    def get(self, name):
        if name in self.allProfiles:
            return self.allProfiles[name]
        return None

class KolConfigsManager:

    __instance = None

    @staticmethod
    def getInstance():
        if KolConfigsManager.__instance == None:
            KolConfigsManager.__instance = KolConfigsManager()
        return KolConfigsManager.__instance

    def __init__(self):
        kolConfigs = None
        try:
            kolConfigs = self.__loadConfigsFromFs()
        except:
            print("Warning: An error occured when loading config")

        if kolConfigs == None:
            kolConfigs = KolConfigs()

        self.kolConfigs = kolConfigs

    def save(self):
        pickle.dump(self.kolConfigs, open(CONFIG_FILENAME, "wb"))

    def getProfileByName(self, profileName):
        kolConfigs = self.kolConfigs
        profile = kolConfigs.get(profileName)
        if profile == None:
            profile = self.__addNewProfile(profileName)
        return profile

    def __loadConfigsFromFs(self):
        kolConfigs = pickle.load(open(CONFIG_FILENAME, "rb"))

        # basically for saving time finding bugs, as pickler doesn't inform about anything:
        if (kolConfigs.version != KolConfigs.VERSION):
            print("Error: wrong Version in stored file")
            raise (Exception("wrong Version in stored file. All old profiles will be deleted"))

        return kolConfigs

    def __addNewProfile(self, profilename):
        newProfile = KolConfig(profileName=profilename)
        self.kolConfigs.update(newProfile)

        return newProfile
