from banner.banner import main_banner
from extensions.esp import GlowEsp

import sys, pymem
from pynput.mouse import Button, Controller
from threading import Thread

class CsFuck:
    def __init__(self):
        self.mouse = Controller()

    def run(self):
        """Main Thread where the extensions get run."""
        Thread(target = GlowEsp().esp_thread).start()

if __name__ == "__main__":
    try:
        CsFuck().run()
        main_banner()
    except pymem.exception.ProcessNotFound as e:
        print(e)
        sys.exit()
        