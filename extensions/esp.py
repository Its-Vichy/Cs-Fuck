from utils.extension import Extension
from extensions import client

import random
from time import sleep


class GlowEsp(Extension):
    def __init__(self):
        self.isRunning = True

    def esp_thread(self):
        if self.isRunning:
            while self.isRunning:
                sleep(0.006)
                glow_manager = client.pm.read_int(client.client + client.offset.dwGlowObjectManager)

                player = client.pm.read_int(client.client + client.offset.dwLocalPlayer)
                player_team = client.pm.read_int(player + client.offset.m_iTeamNum)

                for i in range(1, 64): # First 64 entities reserved for players.
                    try:
                        entity = client.pm.read_int(client.client + client.offset.dwEntityList + i * 0x10)

                        if entity:
                            entity_glow = client.pm.read_int(entity + client.offset.m_iGlowIndex)
                            entity_team = client.pm.read_int(entity + client.offset.m_iTeamNum)
                                
                            if player_team != entity_team: # Not the player's team.
                                client.pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(random.randint(0, 1))) #R
                                client.pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(random.randint(0, 1))) #G
                                client.pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(random.randint(0, 1))) #B
                                client.pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) #A
                                client.pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1) # Enabling the glow.
                            else: # The player's team.
                                client.pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0)) #R
                                client.pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1)) #G
                                client.pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0)) #B
                                client.pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) #A
                                client.pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1) # Enabling the glow.
                    except:
                        pass
        else:
            pass