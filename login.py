#Start (imports)
import discord
from discord.ext import commands
import os
import requests as re
global user
user = "nil"
from time import sleep


def scrape(link):

    response = re.get(link)
    html = response.text
    return html


def passcheck(username):
    made = False
    sucpas = False
    pasw = input("Password: ")
    paswds = scrape("https://pastebin.com/raw/QSdpFLVf")
    searchforp = paswds.split(",")
    for x in searchforp:
        cjnd = x.split(":")
        if cjnd[0] == username:
            if pasw == cjnd[1]:
                sucpas = True

    if not sucpas:
        print("Incorrect password")
        usernamecheck()
    else:
        print("Successfully logged in")


def usernamecheck():

    global user
    made = False
    sucpas = False

    username = input("Username: ")
    usernames = scrape("https://pastebin.com/raw/f7SN0RvE")
    searchfor = usernames.split(",")
    for i in searchfor:
        if i == username:
            print("successful")
            made = True

    if not made:
        print("Unknown username.")
        usernamecheck()
    else:
        user = username
        passcheck(username)


usernamecheck()

##----------------------------------------------##
#                    Bot Code                    #
cp = "/"

trap = commands.Bot(command_prefix=cp, selfbot=True)

token = input(f"{user}@skids$~root import token > ")


@trap.event
async def on_ready():
    print("rawr")

    for _ in "CONNECTED - ":
        sleep(0.3)
        ctypes.windll.kernel32.SetConsoleTitleW(_,end="")


trap.run(token, bot=False)
