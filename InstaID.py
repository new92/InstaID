#Imports
try:
    import os
    import sys
    import instagrapi
    import requests
    import http
    import crypto
    import cryptography
    import json
    import urllib
    import webbrowser
    import instaloader
    import socket
    import logging
    import platform
    import pyfiglet
    import locale
    import geocoder
    import time
    import nmap 
    import sniffer
    import re
    import signal
    from tkinter import messagebox
except ImportError as imp:
    tkinter.messagebox.error("Error !","You haven't installed all the modules used on this program")
    print("Please enter the command: pip3 install -r requirements.txt")
    time.sleep(2)
    print("And execute the program again !")
    time.sleep(1)
#End of Imports

#Logo
insta = pyfiglet.figlet_format("INSTAID")
print(insta)
#

#Main Program
print("[+] Github: @new92")
print("\n")
print("[01] Instagram Account ID")
print("[02] Exit")
print("\n")
option=input("[::] Choose an option: ")

while option != "01" and option != "02" and option != "1" and option != "2":
    print("Invalid option !")
    option=input("[::] Please enter again: ")
if option == "01" or option == "1":
    user=input("Please enter the username: ")
    username = user.lower()
    username = username.strip()
    insta = instaloader.Instaloader()
    id = insta.check_profile_id(username)
    time.sleep(3)
    print("The id of the given profile: "+str(id))
else:
    print("Exiting...")
    time.sleep(2)
    quit(0)
#End of the Program