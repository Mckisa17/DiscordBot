# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord.ext import commands
import csv
import random

# IMPORT THE OS MODULE.
import os

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix=None, intents=intents)

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@client.event
async def on_ready() -> None:
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in client.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("huh? bot is in " + str(guild_count) + " guilds.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'huh?' in message.content.lower():
        user_mention = message.author.mention
        joke = get_random_joke()
        response = f'{user_mention} :\n{joke}'
        await message.channel.send(response)


def get_random_joke():
    with open('reddit_dadjokes.csv', 'r', encoding='utf-8') as file:
        jokes = list(csv.DictReader(file))
        random_joke = random.choice(jokes)
        return random_joke['joke']



# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
client.run(TOKEN)
