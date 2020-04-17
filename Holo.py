 # These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import json
import atexit
import threading
import pickle
import requests
import re
import csv
import json
import numpy as np
from PIL import Image
import hashlib
import os, sys
import io
import subprocess
from Config import Virus
from Config import Shop
import mysql.connector
from _thread import start_new_thread
#from tkinter import Tk
from PIL import Image,ImageDraw
import matplotlib.pyplot as plt;


file = open("secret.txt","r")
token = file.read()
  
def IsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False


# START INIT PDISOCRD
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="Holo"
)

cursor = mydb.cursor(prepared=True)

VirusUser = []
cursor.execute("SELECT uid FROM Virus;")
VirusUser = [item[0] for item in cursor.fetchall()]


Music = []

r = requests.get("https://spotifycharts.com/regional/global/daily/latest/download", allow_redirects=True)
decoded_content = r.content.decode('utf-8')

readCSV = csv.reader(decoded_content.splitlines(), delimiter=',')
for row in readCSV:
    Music.append(row[1])

Rol = {}   
#s = open('Sover.txt', 'r').read()
#Rol = eval(s)

client = Bot(description="Fun Bot by Agent_Orange", command_prefix="~", pm_help = False)
RecNext = 0
author = ""
a1 = a2 = ""
Dict = {}
PokePref = []
Tcmd = 0
ccheck = 0
Catch = 1
Channel = ["495009196132007946"]
acp = 0
osci = 0
pname = ""
grnd = random.randint(1,100)
print("GLoBAL Random:"+str(grnd))

def SQL(que):
    print(cursor.execute(que))

def launchWithoutConsole(command, args):
    """Launches 'command' windowless and waits until finished"""
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    return subprocess.Popen([command] + args, startupinfo=startupinfo).wait()

def MusicU():
    r = requests.get("https://spotifycharts.com/regional/global/daily/latest/download", allow_redirects=True)
    open('Spotify\\regs.csv', 'wb').write(r.content)
    
def RefresnRnd():
    global grnd
    grnd = random.randint(1,100)
    print("GLoBAL Random:"+str(grnd))
    
with open('udata.pkl', 'rb') as input:
        Dict = pickle.load(input)

def SaveDict():
  with open('udata.pkl', 'wb') as output:
    pickle.dump(Dict, output, pickle.HIGHEST_PROTOCOL)
  print ("Saved")

                
def Moneh(Entry:int,money:int):
        if(Entry in Dict):
                Dict[Entry] = Dict[Entry] + money
        else:
                Dict[Entry] = money
        SaveDict()

def MonehInAcc(cns):
    return Dict.get(cns,0)

def MonehRemove(Entry:int,money:int):
    Dict[Entry] = Dict[Entry] - money
    SaveDict()
    
def MonehG(Giver:int,Rec:int,money:int):
    Moneh(Rec,money)
    MonehRemove(Giver,money)
    SaveDict()

def HintAw(dif):
    if(-5<dif<5):
        return "Extremely Close"
    elif(-10<dif<10):
        return "Very Close"
    elif(-30<dif<30):
        return "Close"
    elif(-50<dif<50):
        return "Far"
    else:
        return "Extremely Far"
        

def GetPoke(url):
    with open('temp.png', 'wb') as ini:
        rq = requests.get(url + "?width=128&height=128").content
        ini.write(rq)

    size = 128, 128

    im = Image.open("temp.png")
    im.thumbnail(size, Image.ANTIALIAS)
    im.save("temp.png", "png")

    print("REACHED",url)
    exc = ".\IMGBRK.exe"
    launchWithoutConsole(exc, ["", ""])
    data = Tk().clipboard_get()
    return data[8:]

@client.event
async def on_message(message):
    mes = message.content[:]

    global RecNext
    global ccheck
    global acp
    global osci
    global Catch
    global PokePref
    if(message.embeds):
        Catch = 1
    else:
        Catch = 0


    if(int(message.author.id) in VirusUser):
        await AddXP(message)


    
    if(mes=="~clear"):
        RecNext = 0
        ccheck = 0
        acp = 0
        osci = 0
        await client.send_message(message.channel,"Cleared All Running Instanes...")

    if(mes.startswith("~send")):
        await client.process_commands(message)
        return

                
    if(message.author.id == "365975655608745985" and message.channel.id in Channel and Catch == 1):
        cnt = message.embeds[0]["title"]
        if("A wild pokémon has appeared!" in cnt):
            pname = GetPoke(message.embeds[0]["image"]["url"])
            print("CAUGHT:"+pname)
            for mem in PokePref:
                if(Dict[mem.id]>=200):
                    await client.send_message(mem, "p!catch "+pname)
                    Dict[mem.id] -= 200
                    SaveDict()
                else:
                    await client.send_message(mem, "You Want Atleast 200 Holo Coins To Auto Catch Pokemons...")

                
    
    if message.author == client.user:
        return
    
    if RecNext==1 and message.author==author:
        mes = message.content[:]
        rn = random.randint(1,10)
        if(IsInt(rn) and 0<rn<11):
            if(int(mes)==rn):
                await client.send_message(message.channel,"Congrats You Won 10 Holo Coins For Correct Guess!!")
                Moneh(message.author.id,10)
            else:
                await client.send_message(message.channel,"Sorry Your Guess Is Wrong, The Correct Answer Is " + str(rn))
                                

        RecNext = 0
    
    if ccheck==1:
        
        print(message.author.name)
        if(message.author.name==a2.name and mes.lower()=="y"):
            await client.send_message(message.channel,a1.name + ", " + a2.name+" Accepted Your Challenge, PREPARE TO FIGHT!!")
            await asyncio.sleep(2)
            await client.send_message(message.channel,a1.name + ", Enter A Number")
            ccheck = 0
            acp = 1
        elif(message.author.name==a2.name and mes.lower()=="n"):
            await client.send_message(message.channel,a1.name + ", " + a2.name+" Rejected Your Challenge..")
            ccheck = 0
            acp=0

    if(acp==1):
        
        if(message.author.name==a1.name and osci==0):
            if(int(mes) == grnd):
                await client.send_message(message.channel,a1.name + ", Congrats You Won The Game!! 50 Holo Coins Credited To Your Account.")
                RefresnRnd()
                Moneh(a1.id,50)
                acp = 0
            else:
                osci=1
                await client.send_message(message.channel,a1.name + ", Your Guess Is Wrong, Chance Passed To Next Player.")
                await asyncio.sleep(0.5)
                await client.send_message(message.channel,"HINT:The Number Entered Was " + HintAw(int(mes) - grnd) + " From Guessing Number.")
                await asyncio.sleep(0.5)
                await client.send_message(message.channel,a2.name + ", Enter A Number")
        elif(message.author.name==a2.name and osci==1):
            if(int(mes) == grnd):
                await client.send_message(message.channel,a2.name + ", Congrats You Won The Game!! 50 Holo Coins Credited To Your Account.")
                Moneh(a2.id,50)
                RefresnRnd()
                acp = 0
            else:
                osci=0
                await client.send_message(message.channel,a2.name + ", Your Guess Is Wrong, Chance Passed To Next Player.")
                await asyncio.sleep(0.5)
                await client.send_message(message.channel,"HINT:The Number Entered Was " + HintAw(int(mes) - grnd) + " From Guessing Number.")
                await asyncio.sleep(0.5)
                await client.send_message(message.channel,a1.name + ", Enter A Number")

    
    await client.process_commands(message)





@client.event
async def on_ready():
        global Glow
        Glow = client
        print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
        print('--------')
        print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
        print('--------')
        print('Use this link to invite {}:'.format(client.user.name))
        print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
        print('--------')
        print('Support Discord Server: https://discord.gg/FNNNgqb')
        print('Github Link: https://github.com/Habchy/BasicBot')
        print('--------')
        print('You are running BasicBot v2.1') #Do not change this. This will really help us support you, if you need support.
        print('Created by Habchy#1665')
        return await client.change_presence(game=discord.Game(name='Bot v7')) #This is buggy, let us know if it doesn't work.

@client.command(pass_context=True)
@commands.cooldown(1, 60*5, commands.BucketType.user)
async def rnd(ctx):

        await client.say("Please Guess A Number Between 1-10...")
        global RecNext
        RecNext=1
        global author
        author = ctx.message.author
        await asyncio.sleep(3)

@client.command()
async def info():

        await client.say("""I Am Holo, An Advance AI Bot Made By Agent_Orange Designed To Give Good User Experience And Integrated Command Tools
Bunched With Many Fun Games And Useful Things...""")

    
@client.command(pass_context=True)
@commands.cooldown(1, 60*60*24, commands.BucketType.user)
async def daily(ctx):
        await client.say("Daily Coins...")
        await asyncio.sleep(1.5)
        crd = random.randint(1,10)
        await client.say(""+str(crd)+" Holo Coins Credited To Your Balance!!")
        Moneh(ctx.message.author.id,crd)
    
@client.command()
async def send(meschannel, message):
    await client.send_message(client.get_channel(meschannel), message)

@client.command(pass_context=True,brief='Pokemon Holo Catcher', description='Catch Pokemon On Pokecord Automatically Using Holo \n(FEES : 200Holo Coins Per Pokemon)\nUSAGE:Afer Enabling PokeToke Holo Will Automatically Send Names Of Pokes That Appear In Channel\nHope You Enjoy :D')
async def PokeToke(con):
    id = con.message.author
    name = con.message.author.name
    if(id in PokePref):
        await client.say(name + ", Done PokeToke Has Been Disabled For Your Account..")
        await client.say("Do This Again To Enable PokeToke")
        PokePref.remove(id)
    elif(not(id in PokePref)):
        await client.say(name + ", Done PokeToke Has Been Enabled For Your Account..")
        await client.say("Do This Again To Disable PokeToke")
        PokePref.append(id)


@client.command(pass_context=True,brief='1v1 Guessing Game', description='''This Is A Minigame Where You Need To Guess Numbers Between 1-99, Correct Guess Will Win You 50Holo Credits
                                                                            There Will Be Hints Leading To Correct Number..''')
async def challenge(ctx, p2 : discord.Member):
    global ccheck
    global a1
    global a2
    await client.say("Random Guesser v1.0.5")
    await asyncio.sleep(0.5)
    if(ctx.message.author.name==p2.name):
        await client.say("Cannot Challenge Yourself!!")
        return
    await client.say(p2.name + ", " + ctx.message.author.name + " Challenged You For 1v1 Guess Game, Accept? (Y/N)")
    ccheck = 1
    a1 = ctx.message.author
    a2 = p2
    

@client.command(pass_context=True)
async def luck(ctx):

        await client.say("Lucky Draw...")
        await asyncio.sleep(3)
        crd = random.randint(1,10)
        await client.say("You Won "+str(crd)+" Holo Coins!!")
        Moneh(ctx.message.author.id,crd)



@client.command(pass_context=True)
async def xnc530(ctx,arg:int):
    print("ReachedAdmIn")
    print(ctx.message.author.id + " " + str(arg))
    if(int(ctx.message.author.id) != 364288119345905664):
        print("Wrong User ABort")
        return
    if (arg == 47):
        Moneh(ctx.message.author.id,100000)
        await client.send_message(ctx.message.channel,"Command 47 EXECUTED")
    elif (arg==50):
        x = ctx.message.server.members
        for member in x:
            if("" in member.name):
                top = str(member.top_role)
                nik = str(member.nick)
                if("Nyaaa" in nik):
                    continue
                result = re.search(r'^\[(.*)\] ', nik)
                if(result):
                    Rol[top] = result.group(1)
                print(top," NAME ",nik)
        print(Rol)
        await client.send_message(ctx.message.channel,"Command 50 EXECUTED")

'''@client.command(pass_context=True)
async def fiz(ctx):
    global Rol
    if(int(ctx.message.author.id) != 364288119345905664):
        print("Wrong User ABort")
        return
    x = ctx.message.server.members
    for member in x:
        top = str(member.top_role)
        nik = str(member.nick)
        name = str(member.name)
        Mrol = Rol.get(top,0)
        if('Human' in nik and Mrol!=0 and 'Account closed' not in name):
            chn = "["+Mrol+"] "+name
            print(nik+" : "+top+"FORMAT: "+chn)
            await client.change_nickname(member, chn)

        if(not nik.startswith('[') and Mrol!=0 and 'Account closed' not in name):
            chn = "["+Mrol+"] "+name
            print(nik+" : "+top+"FORMAT: "+chn)
            await client.change_nickname(member, chn)

        if('Drones' in top and not name.startswith('[')):
            chn = "[Bot] "+name
            print(nik+" : "+top+"FORMAT: "+chn)
            await client.change_nickname(member, chn)'''


@client.command(pass_context=True)
async def give(ctx, mem : discord.Member, no : int):
    if(MonehInAcc(ctx.message.author.id) >= no):
        MonehG(ctx.message.author.id,mem.id,no)
        SaveDict()
        await client.send_message(ctx.message.channel, "Done! You Gave " +str(no)+ " Holo Coins To " + mem.name + ".")
        print("DEBUG:REACh #+1 " + str(ctx.message.author.id),str(mem.id),str(no))
    else:
        print("dEbug:REACh #-1")
        await client.send_message(ctx.message.channel,"Sorry But You Do Not Have Sufficient Balance To Transfer Coins..")

@client.command(pass_context=True)
async def uu(ctx,tim=1):
    for i in range(tim):
        rn = random.randint(1,200)
        embed=discord.Embed(title="Random Music Selector", description="!play " + Music[rn])
        await client.say(embed=embed)


@client.command(pass_context=True)
async def em(ctx,nm:int):
    if(nm==1):
        imageURL = "https://media.discordapp.net/attachments/427827132320710658/479893406605115412/PenguinBot_data_emoji_cache_478400446654971904.png"
    elif(nm==2):
        imageURL = "https://media.giphy.com/media/eVy46EWyclTIA/giphy.gif"
    elif(nm==3):
        imageURL = "https://media.giphy.com/media/l3UcgJJCfhoyN2jTy/giphy.gif"
    elif(nm==3):
        imageURL = "https://media.giphy.com/media/sauYjWmJJ18xW/giphy.gif"
    elif(nm==4):
        imageURL = "https://tenor.com/view/awesome-reaction-you-who-whos-awesome-gif-4860921"
   

    await client.send_message(ctx.message.channel, imageURL)

@client.command(pass_context=True)
async def wallet(ctx):
        money = Dict.get(ctx.message.author.id,0)
        strm = "Dear User You Have " + str(money) + " Holo Coins."
        await client.send_message(ctx.message.channel, strm)

#@client.command(pass_context=True)
#async def nm(ctx, mem : discord.Member, nickname):
#    await client.change_nickname(mem, nickname)



#PLAGUE DEV WORK EXP
@client.group()
async def plg():
    pass
impl = "https://store-images.s-microsoft.com/image/apps.30736.13510798882964918.4a7928b5-2d62-467c-85f8-7158f8b40eb1.c11c86c9-f685-4310-93a3-b00498b84b2b?mode=crop&q=90&h=270&w=270&format=jpg&background=%23990000"

@plg.command(pass_context=True)
async def istart(ctx):
    embed=discord.Embed(title="Choose Your Starter Virus:", description="To Infect Whole World And Destroy Earth You Need To Have A Starter Virus...", color=0xff5559)
    embed.set_author(name=ctx.message.author.name)
    embed.set_thumbnail(url=impl)
    for key, value in Virus.items():
        embed.add_field(name="***"+key+"***", value="**COST : "+str(value[0])+" Holo Coins**\n*BASE STATS*\n*1.Death Percentage - "+str(value[1])+"*\n*2.Adaptability - "+str(value[2])+"*\n*3.Spread Rate - "+str(value[3])+"*\n", inline=False)

    embed.set_footer(text="~Made By Agent_Orange#9852")
    embed.add_field(name="Command Syntax",value="Do '~plg iselect (Virus Name)' To Select Virus.\n***Apostrophe And Brackets Are Not To Be Included In Command***",inline=True)
    await client.say(embed=embed)
    
@plg.command(pass_context=True)
async def help(pg = 1):
    embed=discord.Embed(title="Plague Help Page", description="Page : 1" ,color=0xff5559)
    embed.set_thumbnail(url=impl)
    embed.add_field(name='Stats', value='1.Death Percentage - Approx Number Of People Who Might Die If Infected From This Virus (Out Of 100)\n2.Adaptability - Chances Of Survival Of Virus In Harsh Conditions (More Adaptibility = More Chance Of Virus Spread)\n3.Spread Rate - How Fast Will This Virus Spread From One Person To Other.', inline=False)
    embed.add_field(name='Choosing Starter Virus', value='Do "~plg istart" To Get List Of Virus Avaliable And Then "~plg iselect (Virus Name)"', inline=True)
    embed.set_footer(text="***Commands Are To Be Added Without Apostrophe And Brackets.***")
    await client.say(embed=embed)

@plg.command(pass_context=True)
async def iselect(ctx,name):
    value = Virus.get(name,0)
    if(value==0):
        await client.say("Sorry But The Virus You Entered Doesnt Exist..")
        return
    if(value and MonehInAcc(ctx.message.author.id) > value[0]):
        MonehRemove(ctx.message.author.id,value[0])
        embed=discord.Embed(title="Virus Selected..", description="You Selected " + name, color=0x09ff5f)
        embed.set_thumbnail(url=impl)
        embed.set_author(name=ctx.message.author.name)
        embed.add_field(name="***"+name+"***", value="**COST : "+str(value[0])+" Holo Coins**\n*VIRUS STATS*\n*1.Death Percentage - "+str(value[1])+"*\n*2.Adaptability - "+str(value[2])+"*\n*3.Spread Rate - "+str(value[3])+"*\n", inline=False)
        embed.set_footer(text="~Made By Agent_Orange#9852")
        await client.say(embed=embed)
        insert_stmt = (
        "INSERT INTO Virus (uid, Vn, DeathP, Adapt,Spread) "
        "VALUES (%s, %s, %s, %s, %s)"
        )
        dat = (ctx.message.author.id,name,value[1],value[2],value[3])
        print(dat)
        VirusUser.append(ctx.message.author.id)
        cursor.execute(insert_stmt, dat)
        mydb.commit()
    else:
        await client.say("You Do Not Have Sufficient Balance To Buy..")


@plg.command(pass_context=True)
async def info(ctx):
    cursor.execute("SELECT * FROM Virus WHERE uid="+ctx.message.author.id)
    val = cursor.fetchone()
    if(val):
        embed=discord.Embed(title="Virus Info", description="Selected : " + str(val[1]), color=0x5604ff)
        embed.set_author(name=ctx.message.author.name)
        embed.add_field(name="***"+str(val[1])+"***", value="*VIRUS STATS*\n*1.Death Percentage - "+str(val[2])+"*\n*2.Adaptability - "+str(val[3])+"*\n*3.Spread Rate - "+str(val[4])+"*\n", inline=False)
        embed.add_field(name="***PROGRESS***", value="Infected "+str(val[5])+" Humans.\nKilled "+str(val[6])+" Humans.", inline=False)
        embed.add_field(name="***DEVELOPMENT***", value="***LEVEL*** "+str(val[8])+"/12\n***XP*** "+str(val[7])+"/"+str(val[8]*1000), inline=False)
        embed.set_footer(text="~Made By Agent_Orange#9852")
        embed.set_thumbnail(url=impl)
        await client.say(embed=embed)
    else:
        await client.say("You Do Not Have Any Starter Virus, Please Select One...")
        embed=discord.Embed(title="Choose Your Starter Virus:", description="To Infect Whole World And Destroy Earth You Need To Have A Starter Virus...", color=0xff5559)
        embed.set_author(name=ctx.message.author.name)
        embed.set_thumbnail(url=impl)
        for key, value in Virus.items():
            embed.add_field(name="***"+key+"***", value="**COST : "+str(value[0])+" Holo Coins**\n*BASE STATS*\n*1.Death Percentage - "+str(value[1])+"*\n*2.Adaptability - "+str(value[2])+"*\n*3.Spread Rate - "+str(value[3])+"*\n", inline=False)

            
        embed.set_footer(text="~Made By Agent_Orange#9852")
        embed.add_field(name="Command Syntax",value="Do '~plg iselect (Virus Name)' To Select Virus.\n***Apostrophe And Brackets Are Not To Be Included In Command***",inline=True)
        await client.say(embed=embed)
        
async def AddXP(mes):
    uid = int(mes.author.id)
    nm = mes.author.name
    cursor.execute("SELECT * FROM Virus WHERE uid="+str(uid))
    val = cursor.fetchone()
    nxp = val[7] + 200
    nlv = val[8]
    if(nxp > 1000*nlv):
        nxp = 0
        nlv += 1
        embed=discord.Embed(title="LEVEL UP", description="Congrats "+str(nm)+", Your Virus Is Level "+str(nlv)+" !!", color=0x00ffff)
        embed.add_field(name="***REWARD***", value="Your Death Percent, Adaptibility And Spread Rate Got 3% Increment!!", inline=False)
        await client.send_message(mes.channel, embed=embed)
        cursor.execute ("UPDATE Virus SET DeathP=DeathP+3, Adapt=Adapt+3, Spread=Spread+3 WHERE uid=%s", (uid,))
        cursor.fetchone()
        
        
    cursor.execute ("UPDATE Virus SET xp=%s, level=%s WHERE uid=%s", (nxp,nlv,uid))
    cursor.fetchone()
    mydb.commit()
    await CInfect(mes)
    

async def CInfect(mes):
    cursor.execute("SELECT * FROM Virus WHERE uid="+str(mes.author.id))
    val = cursor.fetchone()
    inf = val[5]
    di = val[6]
    #ACHIVEMENTS TODO NOTIFICATION
    vsd = di
    inf += round(inf*val[4]/200)
    di += round(inf*val[2]/400)
    await Achive(mes,vsd,di)
    qst = "UPDATE Virus SET pinf = %s, pdie = %s WHERE uid = %s"
    cursor.execute(qst,(inf,di,mes.author.id))
    cursor.fetchone()
    mydb.commit()

async def Achive(mes,di,dit):
    ach = ""
    if(di<7200000000<dit):
        ach = "Your Virus Wiped All Lifeforms On Earth..\nYou Won The Game!!!"
        qst = "UPDATE Virus SET pinf = 400, pdie = 0 WHERE uid = %s"
        cursor.execute(qst,(mes.author.id,))
        cursor.fetchone()
        mydb.commit()
    elif(di<4200000000<dit):
        ach = "Your Virus Killed Half Of Humanity.."
    elif(di<10000000<dit):
        ach = "Your Virus Becaame A Headache For Whole World And Is Becoming More Deadly Than Ebola.."
    elif(di<5000000<dit):
        ach = "Your Virus Resulted In Epidemic And Is Killing Thousand People Per Seconds.."
    elif(di<1000000<dit):
        ach = "Your Virus Resulted Deadly More Than Chickenpox.."
    elif(di<500000<dit):
        ach = "Your Virus Started To Show Its Presence.."
    elif(di<10000<dit):
        ach = "Your Virus Has Resulted In 10000 Kills.."
    elif(di<2000<dit):
        ach = "Your Virus Has Matured And Started Spreading.."
    
    if(ach!=""):
        embed=discord.Embed(title="Achievement", description="Congratz "+mes.author.name+", "+ach, color=0x36ca26)
        embed.set_author(name=mes.author.name)
        embed.set_thumbnail(url="https://78.media.tumblr.com/a5cc7a98cbd52c4d4f897be0bf7b4aef/tumblr_or4llo5Vsm1vmrye9o1_500.png")
        embed.set_footer(text="~Made By Agent_Orange#9852")
        await client.send_message(mes.channel, embed=embed)
    
    


@plg.command(pass_context=True)
async def shop(ctx):
    cursor.execute("SELECT * FROM Virus WHERE uid="+str(ctx.message.author.id))
    val = cursor.fetchone()
    embed=discord.Embed(title="Shop", description="Buy Items To Make Your Virus More Powerful!!", color=0xffff80)
    embed.set_author(name=ctx.message.author.name)
    embed.set_thumbnail(url="https://cdn0.iconfinder.com/data/icons/common-icons/512/cart.png")
    for key, kval in Shop.items():
        embed.add_field(name="***"+key+"***", value="**COST : "+str(round(kval[1]*val[8]/12*10))+" Holo Coins**\n*"+str(kval[0]),inline=True)
    embed.set_footer(text="~Made By Agent_Orange#9852")
    embed.add_field(name="Command Syntax",value="Do '~plg buy (Item Name)' To Buy Item.\n***Apostrophe And Brackets Are Not To Be Included In Command***",inline=True)
    await client.say(embed=embed)


@plg.command(pass_context=True)
async def buy(ctx,name):
    cursor.execute("SELECT * FROM Virus WHERE uid="+str(ctx.message.author.id))
    val = cursor.fetchone()
    idit=0
    itv = Shop.get(name,0)
    if(itv!=0):
        if(MonehInAcc(ctx.message.author.id) >= round(itv[1]*val[8]/12*10)):
            await client.say("Success!")
            MonehRemove(ctx.message.author.id,round(itv[1]*val[8]/12*10))
        else:
            await client.say("You Do Not Have Enough Money To Buy That.")
            return
    elif(name!=value[0]):
        await client.say("Sorry But There Is No Item With That Name.")
        return

    qst = ""
    dta = ""
    if(itv[2] == 0):
        qst = "UPDATE Virus SET DeathP = DeathP + 10 WHERE uid = %s"
    if(itv[2] == 1):
        qst = "UPDATE Virus SET Spread = Spread + 10 WHERE uid = %s"
    if(itv[2] == 2):
        qst = "UPDATE Virus SET Adapt = Adapt + 20 WHERE uid = %s"
    if(itv[2] == 3):
        qst = "UPDATE Virus SET DeathP = DeathP + 3 WHERE uid = %s"
    if(itv[2] == 4):
        qst = "UPDATE Virus SET Spread = Spread + 5 WHERE uid = %s"
    if(itv[2] == 5):
        qst = "UPDATE Virus SET Adapt = Adapt + 10 WHERE uid = %s"
    if(itv[2] == 6):
        qst = "UPDATE Virus SET level = level + 1 WHERE uid = %s"
    if(itv[2] == 7):
        qst = "UPDATE Virus SET pinf = pinf + 1000 WHERE uid = %s"
    if(itv == 8):
        pass
    cursor.execute(qst,(ctx.message.author.id,))
    cursor.fetchone()
    mydb.commit()

def WCOM(percent):
    prob = random.randrange(0,100)
    if prob < percent:
        return True
    else:
        return False

@plg.command(pass_context=True)
async def infect(ctx, p2 : discord.Member):
    cursor.execute("SELECT * FROM Virus WHERE uid="+str(ctx.message.author.id))
    val = cursor.fetchone()
    embed=discord.Embed(title="DANGER", description="You Tried To Infect "+p2.name+" With "+val[1]+",\nPlease Wait 10Seconds To Know If It Suceeded", color=0xffff80)
    embed.set_author(name=ctx.message.author.name)
    embed.set_thumbnail(url="http://www.pngall.com/wp-content/uploads/2017/05/Alert-Download-PNG.png")
    embed.set_footer(text="~Made By Agent_Orange#9852")
    await client.say(embed=embed)
    await asyncio.sleep(10)
    
    if(WCOM(val[4])):
        embed=discord.Embed(title="INFO", description="You Sucessfully Infected "+p2.name+" With "+val[1]+"\nPlease Wait 60 Seconds To Know If Virus Killed "+p2.name, color=0xffff80)
        embed.set_author(name=ctx.message.author.name)
        embed.set_thumbnail(url="http://www.pngall.com/wp-content/uploads/2017/05/Alert-Download-PNG.png")
        embed.set_footer(text="~Made By Agent_Orange#9852")
        await client.say(embed=embed)
        qst = "UPDATE Virus SET pinf = pinf + 1 WHERE uid = %s"
        cursor.execute(qst,(ctx.message.author.id,))
        cursor.fetchone()
        mydb.commit()
        await asyncio.sleep(60)
        ded = WCOM(val[2])
        if(ded):
            embed=discord.Embed(title="INFO", description="Your Virus Killed "+p2.name+"", color=0xffff80)
            embed.set_author(name=ctx.message.author.name)
            embed.set_thumbnail(url="http://www.pngall.com/wp-content/uploads/2017/05/Alert-Download-PNG.png")
            embed.set_footer(text="~Made By Agent_Orange#9852")
            await client.say(embed=embed)
            qst = "UPDATE Virus SET pdie = pdie + 1 WHERE uid = %s"
            cursor.execute(qst,(ctx.message.author.id,))
            cursor.fetchone()
            mydb.commit()
        else:
            embed=discord.Embed(title="INFO", description=p2.name+" Somehow Survived The Virus, But Still Is Infected.", color=0xffff80)
            embed.set_author(name=ctx.message.author.name)
            embed.set_thumbnail(url="http://www.pngall.com/wp-content/uploads/2017/05/Alert-Download-PNG.png")
            embed.set_footer(text="~Made By Agent_Orange#9852")
            await client.say(embed=embed)
        
    else:
        await client.say("Your Virus Didnt Worked And "+p2.name+" Survived From "+val[1])

async def Second(cid):
    await client.wait_until_ready()
    await asyncio.sleep(10)
    await client.send_message(cid, "SECONDZZ 10")
    return


@plg.command(pass_context=True)
async def invade(ctx):
    cursor.execute("SELECT * FROM Virus WHERE uid="+str(ctx.message.author.id))
    val = cursor.fetchone()
    if(val[5]<400):
        qst = "UPDATE Virus SET pinf = pinf + 400 WHERE uid = %s"
        cursor.execute(qst,(ctx.message.author.id,))
        cursor.fetchone()
        mydb.commit()
        await client.say("DONE!! WE SPREAD YOUR VIRUS TO 400 RANDOM PEOPLES!! OUTBREAK!!")
    else:
        await client.say("Sorry But You Already Used This Command...")

@plg.command(pass_context=True)
async def map(ctx):
    cursor.execute("SELECT * FROM Virus WHERE uid="+str(ctx.message.author.id))
    val = cursor.fetchone()
    im = Image.open("gmap.jpg")
    draw = ImageDraw.Draw(im)
    pix = im.load()
    sz = im.size
    ilt = 0
    while ilt<val[5]/1000:
        rx = random.randint(0,999)
        ry = random.randint(0,499)
        rgb = pix[rx,ry]
        if(rgb[2]>rgb[1] or (rgb[0]+rgb[1]+rgb[2])/3>200):
            continue
        else:
            draw.point((rx,ry),fill=255)
            ilt+=1
    im.save("./mtemp.jpg")
    embed=discord.Embed(title="MAP", description="NOTE : EACH RED DOT REPRESENTS 1000 INFECTED PEOPLE", color=0xffff80)
    embed.set_author(name=ctx.message.author.name)
    embed.set_image(url="./gmap.jpg")
    embed.set_footer(text="~Made By Agent_Orange#9852")
    await client.say(embed=embed)


''' COMMAND ERROR START '''
@client.event
async def on_command_error(error, ctx):
        if isinstance(error, commands.CommandOnCooldown):
                if((error.retry_after/3600) > 1):
                        await client.send_message(ctx.message.channel, content="Please Wait " + str(round(error.retry_after/3600)) + "hour Before Using Again.")
                else:
                        await client.send_message(ctx.message.channel, content="Please Wait " + str(round(error.retry_after/60)) +  "mins Before Using Again.")
        raise error  # re-raise the error so all the errors will still show up in console

''' COMMAND ERROR END '''

#start_new_thread( client.run, (os.environ['token'],) )
#start_new_thread( client.run, ('',) )
client.run(token)

