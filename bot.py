import discord
import os, asyncio
from dotenv import load_dotenv
# from datetime import datetime
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = discord.Client()
# today = datetime.now()

@bot.event
async def on_ready():
    server_count = 0
    for server in bot.guilds:
        print(f'{bot.user} is connected to the following guild:\n'f'{server.name}(id: {server.id})')
        server_count += 1
    print("taBot is in " + str(server_count) + " server(s).")
    


    ByleServer = bot.get_channel(909952095707357185)
    await ByleServer.send("Hello :poop: ninjas! Logging on to eat some bandit ass!")
    await asyncio.sleep(5)
    await ByleServer.send("I meant kick... kick some bandit ass.... yea :sweat_smile:")

@bot.event
async def close():
    ByleServer = bot.get_channel(909952095707357185)
    await ByleServer.send("Peace Bitches! :v:")


bot.run(DISCORD_TOKEN)