class Cheat:
    def __init__(self, name: str):
        self.name = name
        self.is_running = False

    def set_is_running(self, is_running: bool):
        self.is_running = is_running