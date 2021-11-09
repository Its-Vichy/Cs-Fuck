from banner.banner import Banner

from cheats.esp import GlowEsp
from cheats.no_flash import NoFlash

from os import system
from threading import Thread

class CsFuck:
    def _run(self):
        """(Protected) Main Thread where the extensions get run."""
        # Do not replace Thread by threading.Timer, Timer takes more memory
        Thread(target = GlowEsp().esp).start()
        Thread(target = NoFlash().no_flash).start() 
        Thread(target = Banner().main_banner()).start()
 
if __name__ == "__main__":
    system("cls")
    CsFuck()._run()