from pystyle import Anime, Center, Colorate, Colors
from pynput.mouse import Button, Controller
import threading, time, pymem, random

class Offset:
    def __init__(self):
        self.dwEntityList = 0x4DBF75C
        self.dwLocalPlayer = 0xDA544C
        self.m_iCrosshairId = 0x11838
        self.m_iTeamNum = 0xF4
        self.m_fFlags = 0x104

        self.m_flFlashMaxAlpha = 0x1046C
        
        self.dwGlowObjectManager = 0x5307C48
        self.m_iGlowIndex = 0x10488

        self.m_dwBoneMatrix = 0x26A8
        self.m_vecOrigin = 0x138

class CsFuck:
    def __init__(self):
        self.trigger_bot = True
        self.no_flash = True
        self.esp = True

        self.mouse = Controller()
        self.Offset = Offset()
        self.pm = pymem.Pymem("csgo.exe")
        self.client = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
    
    def triger_bot_tread(self):
        while True:
            if self.triger_bot_tread:
                time.sleep(0.006)

                try:
                    player = self.pm.read_int(self.client + self.Offset.dwLocalPlayer)
                    entity_id = self.pm.read_int(player + self.Offset.m_iCrosshairId)
                    entity = self.pm.read_int(self.client + self.Offset.dwEntityList + (entity_id - 1) * 0x10)

                    entity_team = self.pm.read_int(entity + self.Offset.m_iTeamNum)
                    player_team = self.pm.read_int(player + self.Offset.m_iTeamNum)

                    if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                        self.mouse.click(Button.left, 1)
                except:
                    pass

            else:
                time.sleep(1)
    
    def no_flash_thread(self):
        while True:
            if self.no_flash:
                player = self.pm.read_int(self.client + self.Offset.dwLocalPlayer)
                if player:
                    flash_value = player + self.Offset.m_flFlashMaxAlpha
                    if flash_value:
                        self.pm.write_float(flash_value, float(0))

            time.sleep(1)

    def esp_thread(self):
        while True:
            if self.esp:
                time.sleep(0.006)
                glow_manager = self.pm.read_int(self.client + self.Offset.dwGlowObjectManager)

                player = self.pm.read_int(self.client + self.Offset.dwLocalPlayer)
                player_team = self.pm.read_int(player + self.Offset.m_iTeamNum)

                for i in range(1, 64):
                    try:
                        entity = self.pm.read_int(self.client + self.Offset.dwEntityList + i * 0x10)

                        if entity:
                            entity_glow = self.pm.read_int(entity + self.Offset.m_iGlowIndex)
                            entity_team = self.pm.read_int(entity + self.Offset.m_iTeamNum)
                            
                            if player_team != entity_team:
                                self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(random.randint(0, 1)))
                                self.pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(random.randint(0, 1)))
                                self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(random.randint(0, 1)))
                                self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))
                                self.pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
                            else:
                                self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
                                self.pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))
                                self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))
                                self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))
                                self.pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)
                    except:
                        pass
            else:
                time.sleep(1)

    def run(self):
        threading.Thread(target= self.no_flash_thread).start()
        threading.Thread(target= self.triger_bot_tread).start()
        threading.Thread(target= self.esp_thread).start()

        banner = '''
   ____         _____           _    
  / ___|___ _ _|  ___|   _  ___| | __
 | |   / __(_|_) |_ | | | |/ __| |/ /
 | |___\__ \_ _|  _|| |_| | (__|   < 
  \____|___(_|_)_|   \__,_|\___|_|\_\\

        '''

        Anime.Fade(Center.Center(banner), Colors.blue_to_purple, Colorate.Vertical, interval=1)

CsFuck().run()