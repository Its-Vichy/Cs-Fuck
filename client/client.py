from offset.offset import Offset

import pymem

class Client:
    """The client that is running."""
    def __init__(self):
        self.process = self.__get_process("csgo.exe")
        self.client = self.__get_module("client.dll")
        self.offset = Offset()
        self.local_player = self.process.read_int(self.client + self.offset.DW_LOCAL_PLAYER)
    
    def __get_process(self, process):
        """(Private) Get a process and handle error if needed."""
        try:
            process = pymem.Pymem(process)
        except pymem.exception.ProcessNotFound:
            print("Please start csgo.exe")
            exit() # Leave we do not want exception to appear.
        
        return process

    def __get_module(self, module):
        """(Private) Get a module and handle error if needed"""
        try:
            module = pymem.process.module_from_name(self.process.process_handle, module).lpBaseOfDll
        except Exception as e:
            print("There was an error, please restart the cheat.")

        return module