import imaplib
from smtpbust import buster, proxylessbuster
import os
#https://discord.gg/7jZ5S9W7
def Mainsite():
    os.system("cls")
    print("""
    
    
███████╗███╗   ███╗████████╗██████╗ ██████╗ ██╗   ██╗███████╗████████╗
██╔════╝████╗ ████║╚══██╔══╝██╔══██╗██╔══██╗██║   ██║██╔════╝╚══██╔══╝
███████╗██╔████╔██║   ██║   ██████╔╝██████╔╝██║   ██║███████╗   ██║   
╚════██║██║╚██╔╝██║   ██║   ██╔═══╝ ██╔══██╗██║   ██║╚════██║   ██║   
███████║██║ ╚═╝ ██║   ██║   ██║     ██████╔╝╚██████╔╝███████║   ██║   
╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝     ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   
                                                                          
    https://discord.gg/7jZ5S9W7
    
    Please only use socks4 proxies with this version.
    
    {1} Proxy
    {2} Proxyless
    """)


    def checkifexist():
        if not os.path.exists("logs.txt"):
            with open("logs.txt", 'w') as file:
                print(f"The file logs.txt has been created.")
        else:
            pass

        if not os.path.exists("proxies.txt"):
            # If it doesn't exist, create the file
            with open("proxies.txt", 'w') as file:
                print(f"The file proxies.txt has been created.")
        else:
            pass
    checkifexist()
    choose = input("SMTP Buster >>")
    if choose == "1":
        buster()
    if choose == "2":
        proxylessbuster()
    else:
        Mainsite()
    os.system("cls")
    buster()
Mainsite()
