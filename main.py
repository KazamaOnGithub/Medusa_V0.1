import subprocess
import queue as _queue
import requests, json,threading
import time
import sys
import os
import base64
from pystyle import Box,Center,Cursor,Write,Colors,Add,Colorate
from colorama import Fore,Style,Back
from ast import main


banner = """                                                                 ____________
                                                                /\  ________ \ 
                                                               /  \ \______/\ \ 
                                                              / /\ \ \  / /\ \ \ 
        *            (               (                       / / /\ \ \/ / /\ \ \ 
      (  `           )\ )            )\ )     (             / / /__\_\/ / /__\_\ \ 
      )\))(    (    (()/(       (   (()/(     )\           / /_/_______/ /________\ 
      ((_)()\   )\    /(_))      )\   /(_)) ((((_)(       / /_/_______/ /________ / 
      (_()((_) ((_)  (_))_    _ ((_) (_))    )\ _ )\      \ \ \______ \ \______  /
      |  \/  | | __|  |   \  | | | | / __|   (_)_\(_)      \ \ \  / /\ \ \  / / /
      | |\/| | | _|   | |) | | |_| | \__ \    / _ \         \ \ \/ / /\ \ \/ / /
      |_|  |_| |___|  |___/   \___/  |___/   /_/ \_\         \ \/ / /__\_\/ / /
                                                              \  / /______\/ /
                                                               \/___________/



"""

# variables
Cursor.HideCursor()
UserChannelsAPI = "users/@me/channels"
SendMessageAPI = "v8/channels/{}/messages"
lock = threading.Lock()

# Class API DM ALL

class API:

    def __init__(self, Token:str):

        self.BASEURL = "https://discord.com/api/"
        self.headers = {'authorization' : Token}

        self.req = requests.session()

        self.ChannelIDs = []

        chan_req = requests.get(self.BASEURL+UserChannelsAPI, headers=self.headers)

        for x in list(chan_req.json()):
            self.ChannelIDs.append(x)

    def Message(self, content:str):

        data = {"content":content,"tts":False}
        
        for x in self.ChannelIDs:
            message_req = self.req.post(self.BASEURL+SendMessageAPI.format(x["id"]), headers=self.headers, json=data)
            
            if message_req.status_code == 429:
                time.sleep(10)
            elif message_req.status_code == 200:
                print("[$] Envoyé à {}".format(str(x["id"])))

# def du dm all
def dmall():
    os.system(Center.XCenter("cls"))
    print(banner)
    print(" [$] Enter Token:")
    Token = input()
    
    print(" [$] Your message:")
    Content = input()
    print()
    print(" -------------[$] Message logs -------------")
    print()
    
    API(Token).Message(Content)
    
    os.system('cls')
    
    print()
    retry_dmall = print(" [$] Do you want to restart the program? (y/n): ")
    print()

    if retry_dmall == "y" or retry_dmall == "yes":
      dmall()

    elif retry_dmall == "n" or retry_dmall == "no":
      quit()
    
    else:
      print(" Closing the programme...")
      time.sleep("3")
      quit()


# def du id_finder
def id_finder():
  os.system("cls")
  print(banner)
  id = input(" Mettez l'ID discord juste ici --> ")
  send_id = id.encode('utf-8')
  base64_bytes = base64.b64encode(send_id)
  print()
  print(" La première partie du token discord est > " + str(base64_bytes.decode('utf-8')))
  print()
  
  retry_idfinder = input(" [$] Do you want to restart the program? (y/n): ")
  
  if retry_idfinder == "y" or retry_idfinder == "yes":
    id_finder()
  
  elif retry_idfinder == "n" or retry_idfinder == "no":
    quit()
  
  else:
    print(" Closing the programme...")
    time.sleep("3")
    quit()

# def du More
def more_information():
  os.system("cls")
  print(Center.XCenter(banner))
  print(Center.XCenter("""The "medusa" program was created entirely in python.
It can only be useful if you use the discord application on your computer.
Everything you do with the program is not related to me. 

To contact me (Kazama), please join discord.gg/pythonfr"""))
  print()
  # retour menu selection de base
  print()
  print()
  back_menu_principal = input(" [>] Have you finished reading? it's useless lol (y/yes) ")

  # choix oui ou non pour retour menu principale
  if back_menu_principal == "y" or back_menu_principal == "yes":
    quit()

# menu selection catégorie discord
def menu_discord():
      os.system("cls")
      print(Center.XCenter(banner))
      print(Center.XCenter((Box.DoubleCube("Here is the list of available orders: "))))
      print()
      print("""                                        ║
                                        ║
 ╔══════════════════════════════════════╝
 ║                ║
[>] .dmall       [>]
 ║                ║
[>] .idfinder    [>]
 ║                ║""")
      choice_discord_categorie()

 # selection pour au dessus
def choice_discord_categorie():
  choix_categ_discord = input(" ╚══> Enter one of the above commands: ")

  if choix_categ_discord == ".dmall":
    dmall()
  
  if choix_categ_discord == ".idfinder":
    id_finder()

# bannière pour du tool
def banner_menu():
   print(Center.XCenter("""                                                                 ____________
                                                                /\  ________ \ 
                                                               /  \ \______/\ \ 
                                                              / /\ \ \  / /\ \ \ 
        *            (               (                       / / /\ \ \/ / /\ \ \ 
      (  `           )\ )            )\ )     (             / / /__\_\/ / /__\_\ \ 
      )\))(    (    (()/(       (   (()/(     )\           / /_/_______/ /________\ 
      ((_)()\   )\    /(_))      )\   /(_)) ((((_)(       / /_/_______/ /________ / 
      (_()((_) ((_)  (_))_    _ ((_) (_))    )\ _ )\      \ \ \______ \ \______  /
      |  \/  | | __|  |   \  | | | | / __|   (_)_\(_)      \ \ \  / /\ \ \  / / /
      | |\/| | | _|   | |) | | |_| | \__ \    / _ \         \ \ \/ / /\ \ \/ / /
      |_|  |_| |___|  |___/   \___/  |___/   /_/ \_\         \ \/ / /__\_\/ / /
                                                              \  / /______\/ /
                                                               \/___________/



"""))
banner_menu()

# menu selection de base
def menu_start():
  print(Center.XCenter((Box.DoubleCube("Here is the list of available orders: "))))
  print()
  print("""                                        ║
                                        ║
 ╔══════════════════════════════════════╝
 ║
[>] .discord
 ║
[>] .more
 ║""")          

menu_start()

# selection catégorie
def menu_start_selection():
  selection_menu_start = input(" ╚══> Enter one of the above commands: ")

  if selection_menu_start == ".discord":
     menu_discord()

  elif selection_menu_start == ".more":
     more_information()
  
  else:
    print(" ╔══> Error! The command you just entered is not in our registry")
    menu_start_selection()
    
menu_start_selection()
