import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__), 'moduls'))

from moduls.menu import menu_user

if(__name__=='__main__'):
    menu_user()