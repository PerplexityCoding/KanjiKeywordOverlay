# -------------------------------------------------------------------------------
# -------------------------   Profile Manager  ----------------------------------
# -------------------------------------------------------------------------------
from aqt import mw

from .utils import log


class KolConfig:
    """Contais the settings for using this plugin for a single anki user."""

    def __init__(
        self,
        profileName="DEFAULT",
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
        kanjiLoadDefaultValuesForNonExistingValues=False,
        kanjiShowColorsForKnownKanji=True,
        kanjiUseLink=False,
        kanjiUseLinkUrl="",
    ):
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
        self.kanjiLoadDefaultValuesForNonExistingValues = kanjiLoadDefaultValuesForNonExistingValues
        self.kanjiShowColorsForKnownKanji = kanjiShowColorsForKnownKanji
        self.kanjiUseLink = kanjiUseLink
        self.kanjiUseLinkUrl = kanjiUseLinkUrl

    @staticmethod
    def createFromDict(data):
        self = KolConfig()
        self.__dict__.update(data)
        return self

    def toDict(self):
        return self.__dict__


class KolConfigs:
    VERSION = 5

    def __init__(self, version=None, profiles=None):
        self.version = version if version != None else KolConfigs.VERSION
        self.allProfiles = self.createFromProfiles(profiles) if profiles else dict()

    def createFromProfiles(self, profiles):
        allProfiles = dict()
        for profilesName, profilesValue in profiles.items():
            allProfiles[profilesName] = KolConfig.createFromDict(profilesValue)
        return allProfiles

    def update(self, newProfile):
        self.allProfiles.update({newProfile.profileName: newProfile})

    def get(self, name):
        if name in self.allProfiles:
            return self.allProfiles[name]
        return None

    def toDict(self):
        profiles = dict()
        for profilesName, profilesValue in self.allProfiles.items():
            profiles[profilesName] = profilesValue.__dict__
        return {"profiles": profiles, "version": self.version}


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
            log("Warning: An error occured when loading config")

        if kolConfigs == None:
            kolConfigs = KolConfigs()

        self.kolConfigs = kolConfigs

    def save(self):
        config = self.kolConfigs.toDict()
        # Calls to aqt to write the meta.json file.
        mw.addonManager.writeConfig(__name__, config)

    def getProfileByName(self, profileName):
        kolConfigs = self.kolConfigs
        profile = kolConfigs.get(profileName)
        if profile == None:
            profile = self.__addNewProfile(profileName)
        return profile

    def __loadConfigsFromFs(self):
        # Calls to aqt to read the meta.json file.
        config = mw.addonManager.getConfig(__name__)
        kolConfigs = KolConfigs(profiles=config["profiles"], version=config["version"])
        return kolConfigs

    def __addNewProfile(self, profilename):
        newProfile = KolConfig(profileName=profilename)
        self.kolConfigs.update(newProfile)

        return newProfile
