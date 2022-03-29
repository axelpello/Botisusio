import discord
from discord import FFmpegPCMAudio
from discord.ext import commands
import time

bot = commands.Bot(command_prefix='!!')

@bot.command()
async def ping(ctx):
    await ctx.send('andando imbÉCILLLLLLL(pong)')

@bot.event
async def on_ready():
    print ('BOTARDO LISTO MI CAPITÁN')

@bot.command()
async def Conectarse (ctx):
    ojete = ctx.author.voice.channel 
    await ojete.connect() 

@bot.command()
async def Desconectarse (ctx):
    voice_client = ctx.author.voice.channel
    await ctx.voice_client.disconnect()
#hola
@bot.command()
async def BotisusioDecime (ctx, palabra:str):
    await ctx.send (palabra)

lista = ['Nacho', 'Kerchak', 'Pardo', 'Juan', 'Hugue', 'Fabri', 'Irene', 'Catalina', 'Axel']

@bot.command()
async def Botopino (ctx, persona):
    persona:str
    if persona == 'Kerchak':
        await ctx.send ('KERCHAK SOS EL MÁS LINDO (es mi opinión respetenla)')
    elif persona == 'Pardo':
        await ctx.send ('HolAAaAAaaA :B')
    elif persona == 'Nacho':
        await ctx.send ('Daría mi opinión pero ahora no puedo, tengo que hacer un trabajo.')
    elif persona == 'Juan':
        await ctx.send ('No entendió Hellblade porque lo jugó en latino, escuchando música y salteando cinemáticas. Yo lo vi.')
    elif persona == 'Hugue':
        await ctx.send ('Cuando Kerchak está dormido, él es el más lindo ;)')
    elif persona == 'Fabri':
        await ctx.send ('A veces sospecho que es gay en serio y no es solamente una joda que quedó. Encima re otaku.')
    elif persona == 'Catalina':
        await ctx.send ('Buenas teturris. Y eso que soy un bot sin líbido.')
    elif persona == 'Irene':
        await ctx.send ('Dice que es gay pero no le gusta Billie Eilish ni Angelina Jolie, el peor trolo de todos.')
    elif persona == 'Axel':
        await ctx.send ('TA FÍA DA KOKAAAA :D')
    elif persona == 'help':
        await ctx.send ('Para que el bot opine de algún miembro del canal escribí "!!Botopino" seguido del miembro que quieras que el Botisusio opine.')
        await ctx.send ('Lista de miembros con opinión del Bot ↓↓')
        await ctx.send (lista[0:])
    else:
        await ctx.send ('Nakver amigo q pusiste escribilo bien. De última usá "!!Botopino help".')


@bot.command()
async def p (ctx, tema:str):
    if tema == 'atucasa':
        voice_client = ctx.author.voice.channel
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=r"C:\Users\Axel\Desktop\Botisusio\ffmpeg\ffmpeg-2022-02-17-git-2812508086-essentials_build\bin\ffmpeg.exe", source=r"C:\Users\Axel\Desktop\Botisusio\Audios\Audiovegeta.mp3"))
    elif tema == 'wololo': #WOLOLO
        voice_client = ctx.author.voice.channel
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=r"C:\Users\Axel\Desktop\Botisusio\ffmpeg\ffmpeg-2022-02-17-git-2812508086-essentials_build\bin\ffmpeg.exe", source=r"C:\Users\Axel\Desktop\Botisusio\Audios\Wololo.mp3"))

    elif tema == 'vieja':#FOLLARME ESA VIEJA
        voice_client = ctx.author.voice.channel
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=r"C:\Users\Axel\Desktop\Botisusio\ffmpeg\ffmpeg-2022-02-17-git-2812508086-essentials_build\bin\ffmpeg.exe", source=r"C:\Users\Axel\Desktop\Botisusio\Audios\Sijoder.mp3"))
    
    elif tema == 'jackson': #I'm sorry Ms.Jackson!
        voice_client = ctx.author.voice.channel
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=r"C:\Users\Axel\Desktop\Botisusio\ffmpeg\ffmpeg-2022-02-17-git-2812508086-essentials_build\bin\ffmpeg.exe", source=r"C:\Users\Axel\Desktop\Botisusio\Audios\Jackson.mp3"))

    elif tema == 'birra': #Gorda, traeme una birra
        voice_client = ctx.author.voice.channel
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=r"C:\Users\Axel\Desktop\Botisusio\ffmpeg\ffmpeg-2022-02-17-git-2812508086-essentials_build\bin\ffmpeg.exe", source=r"C:\Users\Axel\Desktop\Botisusio\Audios\Birra.mp3"))

    elif tema == 'recaro': #Fua amigo, está re caro
        voice_client = ctx.author.voice.channel
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=r"C:\Users\Axel\Desktop\Botisusio\ffmpeg\ffmpeg-2022-02-17-git-2812508086-essentials_build\bin\ffmpeg.exe", source=r"C:\Users\Axel\Desktop\Botisusio\Audios\Recaro.mp3"))

    elif tema == 'oof': #OOF!
        voice_client = ctx.author.voice.channel
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=r"C:\Users\Axel\Desktop\Botisusio\ffmpeg\ffmpeg-2022-02-17-git-2812508086-essentials_build\bin\ffmpeg.exe", source=r"C:\Users\Axel\Desktop\Botisusio\Audios\Oof.mp3"))

    elif tema == 'omaewa': #Omae wa, mo shindeiru
        voice_client = ctx.author.voice.channel
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=r"C:\Users\Axel\Desktop\Botisusio\ffmpeg\ffmpeg-2022-02-17-git-2812508086-essentials_build\bin\ffmpeg.exe", source=r"C:\Users\Axel\Desktop\Botisusio\Audios\Omaewa.mp3"))

    elif tema == 'sexo': #SEXOOO!
        voice_client = ctx.author.voice.channel
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=r"C:\Users\Axel\Desktop\Botisusio\ffmpeg\ffmpeg-2022-02-17-git-2812508086-essentials_build\bin\ffmpeg.exe", source=r"C:\Users\Axel\Desktop\Botisusio\Audios\Sexo.mp3"))

    elif tema == 'apagalo': #APAGALO OTTO, APAGALO!
        voice_client = ctx.author.voice.channel
        vc = await ctx.author.voice.channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=r"C:\Users\Axel\Desktop\Botisusio\ffmpeg\ffmpeg-2022-02-17-git-2812508086-essentials_build\bin\ffmpeg.exe", source=r"C:\Users\Axel\Desktop\Botisusio\Audios\Apagalo.mp3"))



    elif tema == 'help': #Ayuda
        await ctx.send ('Los audios se ponen con !!p seguido del audio que quieras reproducir. Por ej: !!p wololo')
        await ctx.send ('AUDIOS: "!!p atucasa", "!!p wololo", "!!p vieja", "!!p jackson", "!!p birra", "!!p recaro", "!!p oof", "!!p omaewa", "!!p sexo", "!!p apagalo".')



    #DESCONEXIÓN 
    while vc.is_playing():
            time.sleep(1)
    await vc.disconnect()


bot.run('OTI3NDQzODAwMzUwMTUwNzE3.YdKTWQ.MQDgHlEAhUpCYPS1pUHJ8gMke94')
