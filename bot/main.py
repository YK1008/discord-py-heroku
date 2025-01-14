import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")
    
@bot.event
async def on_reaction_add(reaction, user):
    role = get(member.server.roles, name="Member")
    await bot.add_roles(user, role)

if __name__ == "__main__":
    bot.run(TOKEN)
