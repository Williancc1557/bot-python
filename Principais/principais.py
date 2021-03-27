import discord
import asyncio
import discord
import asyncio
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
import datetime
import psycopg2



intents = discord.Intents.default()
intents.members = True



bot = commands.Bot(command_prefix=['f!', 'F!'], intents=intents)

mydb = psycopg2.connect(
  database='nmcjvwtd',
  user='nmcjvwtd',
  password='DA0El2jZXUe-tELHRgcl9dLpBUuBbX5H',
  host='motty.db.elephantsql.com',
  port='5432'
)








prefix = 'f!'
color = 0x0000FF



cursor = mydb.cursor()

async def Avaliar(ctx):
    embed = discord.Embed(title='<a:Top:815388123039006741> Avaliar o Fênix <a:Top:815388123039006741>',
                          description='**Avalie o fênix De 0 a 10**\n\n***Obs: Você Só Vai Poder Usar Esse Comando Novamente Após 2 Horas***',
                          color=color)
    await ctx.channel.send(embed=embed)


    def check(p):
        return p.author == ctx.author and p.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', timeout=500, check=check)
    except asyncio.TimeoutError:
        return await ctx.channel.send('**Acabou O Tempo Para Avaliar**')
    else:
        avaliar1 = int(msg.content)

    print(avaliar1)
    eu = bot.get_user(id=567757366506815488)

    if avaliar1 == 10:
        editar1 = await ctx.channel.send('<a:loading:785523240944664646>  **Enviado Para a Equipe**')
        await asyncio.sleep(5)
        await editar1.edit(content=':white_check_mark:  **Enviado Para a Equipe**')
        await asyncio.sleep(1)
        print('avaliar')
        await ctx.channel.send(f'**Obrigado Por Avaliar o Bot Fênix {ctx.author.mention}**')
        return await eu.send(f'**Olá Will, Me Avaliaram Nota:**`10`')

    if avaliar1 > 10 or avaliar1 < 0:
        return await ctx.channel.send(
            '**<:error:788824695184424980>| Deveria Ser Um Numero de 0 a 10. Aguarde `2 Horas` Para Usar o Comando Novamente.**')

    if avaliar1 < 10 and  avaliar1 >= 0:
        await ctx.channel.send('**Fale o que Devemos Melhorar: **')

        def check(p):
            return p.author == ctx.author and p.channel == ctx.channel

        try:
            msg2 = await bot.wait_for('message', timeout=500, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send('**Acabou O Tempo Para Avaliar**')
        else:
            avaliar2 = msg2.content
        await eu.send(f'**Olá Will, O(a) `{ctx.author.name}` Me avaliou com a nota:`{avaliar1}`, O que devo melhorar:** `{avaliar2}`')
        editar = await ctx.channel.send('<a:loading:785523240944664646>  **Enviado Para a Equipe**')
        await asyncio.sleep(5)
        await editar.edit(content=':white_check_mark:  **Enviado Para a Equipe**')
        await asyncio.sleep(1)
        return await ctx.channel.send(f'**Obrigado Por Avaliar o Bot Fênix {ctx.author.mention}**')


async def Invite(ctx):
    embed = discord.Embed(title='<a:seta:796356802760933387> ***Deseja Adicionar o Fênix em seu servidor? 🐦***',
                          color=color,
                          description=f'[clique aqui](https://discord.com/oauth2/authorize?client_id=776613209423216650&permissions=8&scope=bot%20identify%20guilds) **para adicionar o Fênix em seu servidor** <a:emoji_35:815313814189899776> \n\n**Me adicione em seu servidor <a:feliz:815313006937899009> **')
    embed.set_image(
        url='https://media.discordapp.net/attachments/788064370722340885/823220448351354910/20210317_111410.jpg?width=591&height=591')

    return await ctx.reply(ctx.author.mention, embed=embed)

async def Avatar(ctx, member: discord.Member = None):
    if not member:
        embed = discord.Embed(
            title=':frame_photo: Comando para ver o avatar do amiguin!! :frame_photo:\n'
                  '\n'
                  '`f!avatar`\nㅤ',
            description='Esse comandinho serve para você ver o **Avatar** de alguém! \n'
                        '\n'
                        '',
            color=0x00BFFF)
        embed.add_field(name='📚 Como usar', value='`f!avatar <@WiLL>`')

        await ctx.reply(embed=embed)

        return False

    embed = discord.Embed(color=0x00FF00)
    embed.set_author(name=member.name, icon_url=str(member.avatar_url))
    embed.set_image(url=member.avatar_url)
    return await ctx.reply(ctx.author.mention, embed=embed)