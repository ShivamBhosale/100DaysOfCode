import os
import time
import pyfiglet
from colorama import Fore
from subprocess import call

msg = "Happy New Year 2021"
fontt = "slant"

FIREWORKS = """
                             .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""



def print_msg():
    f = pyfiglet.Figlet(font=fontt)
    
    for col in [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW ] * 10 + [Fore.WHITE]:
        print(col + f.renderText(msg))
        print(FIREWORKS)
        time.sleep(0.05)
        

if __name__ == "__main__":
    print(print_msg())

