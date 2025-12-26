import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def announce(ctx, *, message):
    embed = discord.Embed(
        title="📢 Announcement",
        description=message,
        color=discord.Color.blue()
    )
    await ctx.send(embed=embed)

@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")

import os
bot.run(os.getenv("DISCORD_TOKEN"))
