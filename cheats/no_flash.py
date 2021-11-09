from utils.cheat import Cheat
from cheats import client

from time import sleep

class NoFlash(Cheat):
    def __init__(self):
        super().__init__("No Flash")
        super().set_is_running(True) # Set it to false if you do not want it to run.

    def no_flash(self):
        while self.is_running:
            flash_value = client.local_player + client.offset.M_FL_FLASH_MAX_ALPHA

            if client.local_player and flash_value:
                client.process.write_float(flash_value, float(0))
            
            sleep(2) # Sleep helps the CPU (A LOT)