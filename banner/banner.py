from pystyle import Anime, Center, Colorate, Colors

def main_banner():
      banner = """
   ____         _____           _    
  / ___|___ _ _|  ___|   _  ___| | __
 | |   / __(_|_) |_ | | | |/ __| |/ /
 | |___\__ \_ _|  _|| |_| | (__|   < 
  \____|___(_|_)_|   \__,_|\___|_|\_\\

        """

      Anime.Fade(Center.Center(banner), Colors.blue_to_purple, Colorate.Vertical, interval = 1)