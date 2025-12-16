import discord
import os
from discord.ext import commands
import database # Importăm fișierul creat mai sus

# Această bucată e necesară pentru Railway să citească tokenul local dacă testezi,
# dar pe server va fi ignorată automat dacă nu există fișierul .env
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectat ca {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Salut! Sunt online pe Railway!")

@bot.command()
async def puncte(ctx):
    # Convertim ID-ul în string pentru siguranță
    uid = str(ctx.author.id)
    pct = database.get_points(uid)
    await ctx.send(f"{ctx.author.mention}, ai {pct} puncte în Supabase!")

@bot.command()
async def bonus(ctx):
    uid = str(ctx.author.id)
    new_balance = database.add_points(uid, 10)
    await ctx.send(f"Ți-am adăugat 10 puncte! Acum ai {new_balance}.")

# Token-ul va fi setat în Railway
bot.run(os.environ.get("DISCORD_TOKEN"))