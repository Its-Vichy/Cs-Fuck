from utils.cheat import Cheat
from cheats import client

import random
from time import sleep

import pymem

class GlowEsp(Cheat):
    """The Glow Esp cheat class."""
    def __init__(self):
        super().__init__("Glow Esp")
        super().set_is_running(True) # Set it to false if you do not want it to run.

    def esp(self):
            while self.is_running:
                sleep(0.006)
                try:
                    glow_manager = client.process.read_int(client.client + client.offset.DW_GLOW_OBJECT_MANAGER)
                    player_team = client.process.read_int(client.local_player + client.offset.M_I_TEAM_NUM)

                    for i in range(1, 32): # Entities 1 to 32 are reserved for players.
                        entity = client.process.read_int(client.client + client.offset.DW_ENTITY_LIST + i * 0x10)
                        entity_dormant = client.process.read_int(client.client + client.offset.M_B_DORMANT)

                        if entity and not entity_dormant:                  
                            entity_glow = client.process.read_int(entity + client.offset.M_I_GLOW_INDEX)
                            entity_team = client.process.read_int(entity + client.offset.M_I_TEAM_NUM)

                            try: # Different color for both team
                                if player_team != entity_team: # Rainbow Team
                                    client.process.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(random.randint(0, 1))) # R
                                    client.process.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(random.randint(0, 1))) # G
                                    client.process.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(random.randint(0, 1))) # B
                                    client.process.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) # Alpha
                                    client.process.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1) # Enabling the glow.
                                else: # Green Tean
                                    client.process.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0)) # R
                                    client.process.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1)) # G
                                    client.process.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0)) # B
                                    client.process.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1)) # Alpha
                                    client.process.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1) # Enabling the glow.
                            except pymem.exception.MemoryWriteError as e:
                                self.is_running = False
                                print("There was an error, please restart your game.") # Non-normal error.
                                break
                except pymem.exception.MemoryReadError: # The player is not in game.
                    sleep(20) # Wait till a game is launch
                    continue