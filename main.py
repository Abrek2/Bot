import discord
import os

from duck_api import get_ducked
from discord.ext import commands
from parola_oluşturucu import gen_pass


prefix = "/"

# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()

# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True

# Bir bot oluşturma ve yetkileri aktarma
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı')

# 
@bot.command
async def merhaba(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum! Bip Bop.')
async def hoşçakal(ctx):
    await ctx.send('Hoşçakal! \U0001f642')
async def prefix(ctx):
    await ctx.send(prefix)

    # parola oluşturucu
async def paralo_oluştur(ctx):
    await ctx.send("Al sana güçlü bir şifre!"+ gen_pass(10))

    # select random meme
async def meme(ctx):
    image_name = random.choice(os.lisdir('images'))
    with open(f'images/{image_name}.jpg'+'rb') as f:

        picture = discord.File(f)

    await ctx.send(file=picture)

    # list possible memes
async def list(ctx):
    await ctx.send(print(os.listdir('images')))

    # get ducked
async def duck(ctx):
    image_url = get_ducked
    await ctx.send(image_url)



bot.run("Çok gizli token")