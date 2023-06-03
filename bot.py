import discord
from discord.ext import commands
token = MTExNDY1NjYzNDk4NDIwNjM2Nw.Gj4R2V.geaE26iu4O81MyvuD1faXrQda9W1nbMAaMMBSE

# Create a new bot instance
bot = commands.Bot(command_prefix='!')

# Event: When the bot is ready and connected
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event: When a message is received
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author.bot:
        return
    
    # Check if the message contains the word "huh?"
    if 'huh?' in message.content.lower():
        # Find the user with the display name "huh?"
        user = discord.utils.get(message.guild.members, display_name='huh?')

        # Mention the user if found
        if user is not None:
            await message.channel.send(f'{user.mention}, someone mentioned "huh?"!')

    # Process other commands and events
    await bot.process_commands(message)

# Run the bot with your token
bot.run(token)
