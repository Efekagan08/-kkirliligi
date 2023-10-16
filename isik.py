import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def determine_light_pollution(star_count):
    if star_count >= 1000:
        return 1
    elif star_count >= 500:
        return 2
    elif star_count >= 100:
        return 3
    elif star_count >= 50:
        return 4
    elif star_count >= 20:
        return 5
    elif star_count >= 10:
        return 6
    elif star_count >= 5:
        return 7
    elif star_count >= 2:
        return 8
    else:
        return 9

@bot.event
async def on_ready():
    print(f'Olarak giriş yaptı {bot.user.name}')

@bot.command('star')
async def star(ctx, star_count: int):
    level = determine_light_pollution(star_count)
    await ctx.send(f'{star_count} gökyüzündeki yıldızların sayısına göre ışık kirliliği seviyesi {level}')

bot.run('Bottoken')
