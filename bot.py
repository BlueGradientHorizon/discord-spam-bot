from time import sleep
from datetime import datetime
import discord

TOKEN = 'mfa.xmHCJ_O4d3BNQjGDpYogQL4eeAufKoe3kM-JTgNaKMJY--2gmZcCvGVF5rPnHY8UGqFB56uk9BWxabolNHQH'
CHANNELID = 835802833878122577 #pingpong
MESSAGE = '<@&835808706042134608>'

USER = ''
DISCR = ''
USERID = ''

client = discord.Client()

@client.event
async def on_ready():
    USER = str(client.user.display_name)
    USERID = str(client.user.id)

    print('User: ' + USER + '#' + DISCR)
    print('User ID: ' + USERID)
    print('Channel ID: ' + str(CHANNELID))

    channel = client.get_channel(CHANNELID)
    counter = 0
    while True:
        await channel.send(MESSAGE) # send '@PingPong Gang' message using role id
        counter += 1
        now = datetime.now()
        print('#' + str(counter) + ' msg is sent at ' + now.strftime("%H:%M:%S, %d.%m.%y"))
        sleep(1)

if __name__ == "__main__":
    client.run(TOKEN, bot = False)
