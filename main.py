import os
import random
import urllib.request
import hypixel
import nextcord
import requests
from nextcord import Member
from nextcord.ext import commands
from dotenv import load_dotenv


load_dotenv()
token = os.environ['token']


rand = random.Random()

intents = nextcord.Intents().all()

bot = commands.Bot(command_prefix='?', intents=intents, help_command=None)

hypixel.setKeys(api_keys=['ea07fe17-6122-476f-9c57-dc10714108af'])


@bot.event
async def on_ready():
    print('Я готов!')


@bot.command()
async def server(ctx):
    guild = ctx.guild
    owner = guild.owner
    embed = nextcord.Embed(
        title="Информация о сервере",
        color=Colors.red,
    )
    embed.add_field(name='Название: ', value=guild.name, inline=False)
    embed.add_field(name='Описание: ', value=guild.description, inline=False)
    embed.add_field(name='Текстовые каналы: ', value=len(guild.text_channels))
    embed.add_field(name='Голосовые каналы: ', value=len(guild.voice_channels))
    embed.add_field(name='Категории: ', value=len(guild.categories))
    embed.add_field(name='Владелец: ', value=owner.name, inline=False)
    embed.add_field(name='Айди сервера: ', value=guild.id, inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def random(ctx, number1, number2):
    await ctx.send(str(rand.randrange(number1, number2)))


@bot.command()
async def status(ctx, ip):
    response = requests.get('https://api.mcsrvstat.us/2/' + ip)
    json = response.json()
    embed = nextcord.Embed(
        title='Статистика Данного сервера',
        colour=Colors.red
    )
    embed.add_field(name='Онлайн: ', value=str(json['players']['online']) + '/' + str(json['players']['max']), inline=False)
    embed.add_field(name='Мотд: ', value=json['motd']['clean'], inline=False)
    embed.add_field(name='Буквенный Айпи: ', value=json['hostname'])
    embed.add_field(name='Цифровой Айпи', value=json['ip'])
    embed.add_field(name='Порт', value=json['port'])
    embed.add_field(name='Ядро', value=json['software'], inline=False)
    embed.add_field(name='Версия: ', value=json['version'], inline=False)
    embed.add_field(name='Список игроков: ', value=json['players']['list'], inline=False)
    embed.add_field(name='Иконка', value=icon)
    await ctx.send(embed=embed)


@bot.command()
async def download(ctx, url, name):
    urllib.request.urlretrieve(url, name)
    await ctx.send("Скачивание файла: " + name)


@bot.command()
async def say(ctx, *, arg):
    await ctx.send(arg)


@bot.command()
async def user(ctx, member: Member):
    embed = nextcord.Embed(
        colour=Colors.red,
        title='О пользователе ' + member.name
    )
    embed.add_field(name='Ник человека', value=member.name)
    embed.add_field(name='Айди человека', value=member.id)
    embed.add_field(name='Статус человека', value=member.status)
    embed.add_field(name='Система', value=member.system.numerator)
    role_names = []
    for role in member.roles:
        role_names.append(role.name)
    role_names = ', '.join(role_names)
    embed.add_field(name="Роли", value=f'**{role_names}**', inline=False)
    embed.set_image(url=member.avatar)
    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = nextcord.Embed(
        colour=Colors.red,
        title='Команды'
    )
    embed.add_field(name='<:spigot:964881475994542161> Информация о майнкрафт сервере', value='?status <айпи>')
    embed.add_field(name='Информация о сервере: ', value='?server')
    embed.add_field(name='Бот скажет за тебя', value='?say <сообщение>')
    embed.add_field(name='Рандомное число ', value='?random <первое число> <второе число>')
    embed.add_field(name='Информация о юзере ', value='?user <пинг человека>')
    await ctx.send(embed=embed)


class Colors:
    default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5


bot.run(token)