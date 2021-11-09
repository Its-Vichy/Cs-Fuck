import requests

class Offset:
    """CSGO offset used for Cs-Fuck"""
    def __init__(self):
        self.DATA = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()

        # ESP
        self.DW_GLOW_OBJECT_MANAGER = self.DATA["signatures"]["dwGlowObjectManager"]
        self.M_I_GLOW_INDEX = self.DATA["netvars"]["m_iGlowIndex"]

        # ENTITIES
        self.DW_ENTITY_LIST = self.DATA["signatures"]["dwEntityList"]
        self.M_B_DORMANT = self.DATA["signatures"]["m_bDormant"]

        # FLASH
        self.M_FL_FLASH_MAX_ALPHA = self.DATA["netvars"]["m_flFlashMaxAlpha"]

        # PLAYER
        self.DW_LOCAL_PLAYER = self.DATA["signatures"]["dwLocalPlayer"]

        # OTHERS
        self.M_I_TEAM_NUM = self.DATA["netvars"]["m_iTeamNum"]



