import requests, json

class Offset:
    """CSGO offset used for Cs::Fuck"""
    def __init__(self):
        self.data = requests.get("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.json").json()

        # ESP
        self.dwEntityList = self.data["signatures"]["dwEntityList"]
        self.dwLocalPlayer = self.data["signatures"]["dwLocalPlayer"]
        self.m_iTeamNum = self.data["netvars"]["m_iTeamNum"]
        self.dwGlowObjectManager = self.data["signatures"]["dwGlowObjectManager"]
        self.m_iGlowIndex = self.data["netvars"]["m_iGlowIndex"]