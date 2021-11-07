from offset.offset import Offset

import pymem

class Client:
    """The client that is running."""
    def __init__(self):
        self.pm = pymem.Pymem("csgo.exe")
        self.client = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
        self.offset = Offset()