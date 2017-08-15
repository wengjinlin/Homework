import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import core,main
# from core import main
choice = -1
while main.menu(choice):
    choice = input(">>:")
