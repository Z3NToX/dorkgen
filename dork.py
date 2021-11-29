import sys
import os
from dlist import dork

os.system("cls") # clears the screen

try:
    os.system('title Z3NToX - Simple Dork Generator')  # title of the terminal window
except:
    pass
   
class color:

   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


print(color.BOLD + """\033[91m'

  _____   ____  _____  _  __   _____ ______ _   _ 
 |  __ \ / __ \|  __ \| |/ /  / ____|  ____| \ | |
 | |  | | |  | | |__) | ' /  | |  __| |__  |  \| |
 | |  | | |  | |  _  /|  <   | | |_ |  __| | . ` |
 | |__| | |__| | | \ \| . \  | |__| | |____| |\  |
 |_____/ \____/|_|  \_\_|\_\  \_____|______|_| \_|
                                              
\033[92mDork Generator
\033[92mCoded by: \033[93mZ3NToX
""" + color.END)

while True:
   try:
      url = input("\033[96mEnter a country's domain extension:\033[0m ") # asks for the domain extension which the dorks should use
      if not url:
         raise ValueError # raises an error if the input is left empty

      f = open("Latest Dorks.txt", "w+", encoding='utf8') # creates the file 
      countrydomain = dork.replace("countrydomain", "site:" + url) # replaces the "countrydomain" in dorklist.py with the entered input
      f.write(countrydomain) # writes the dorks in the "Latest Dorks" file

      print(color.DARKCYAN + "Dorks saved to \"Latest Dorks.txt\"" + color.END)
      done = input("Press \"Enter\" to exit")
      sys.exit()

   except ValueError:
         print("\033[91mError: Please enter a valid domain extension!") # prints the error 
