from time import sleep
from datetime import datetime
from os import execv
from sys import argv, executable
import discord

TOKEN = 'your discord token here'
CHANNELID = 0000000000000
MESSAGE = 'your message here'
DELAY = 3000 #in milliseconds

client = discord.Client()

def self_restart():
    execv(executable, [executable] + argv)
    
@client.event
async def on_ready():
    USER = str(client.user.display_name)
    USERID = str(client.user.id)
    DISCR = str(client.user.discriminator)
    
    print('User: ' + USER + '#' + DISCR)
    print('User ID: ' + USERID)
    print('Channel ID: ' + str(CHANNELID))

    counter = 0
    while True:
        try:
            await client.get_channel(CHANNELID).send(MESSAGE)
            counter += 1
            now = datetime.now()
            print('#' + str(counter) + ' msg is sent at ' + now.strftime("%H:%M:%S, %d.%m.%y"))
            sleep(DELAY/1000)
        except:
            print("Error occured while sending message")
            sleep(1)

if __name__ == "__main__":
    while True:
        try:
            client.run(TOKEN, bot=False)
        except:
            print("Error running client, restarting")
            sleep(1)
            self_restart()
