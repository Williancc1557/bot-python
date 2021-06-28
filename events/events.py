import discord
import asyncio
import discord
import asyncio
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
import datetime
import psycopg2

from Principais.principais import bot, mydb, cursor

bot = bot

mydb = mydb

cursor = cursor


async def On_command_error(ctx, error):
    error = getattr(error, 'original', error)
    cmd_name = ctx.message.content.split()[0]

    # SE O COMANDO NÃO EXISTIR
    if isinstance(error, commands.CommandNotFound):
        return await ctx.channel.send(
            f"<:error:788824695184424980>| {ctx.message.author.mention} O comando `{cmd_name}` **não foi encontrado** em meu sistema, deseja ver meus comandos? Digite `f!help`.")
    else:
        print(error)


async def On_message(message):
    if bot.user.mentioned_in(message):
        if f"<@{bot.user.id}>" in message.content or f"<@!{bot.user.id}>" in message.content:
            embed = discord.Embed(title="Olá, meu nome é Fênix! 🐦",
                                  description='📖 Utilize `f!ajuda` para mais **informações**',
                                  color=0xff00ff)
            embed.add_field(name='Servidor Suporte', value='[Suporte](https://discord.gg/VDTAt3Qb9X)')
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/823220448351354910/20210317_111410.jpg?width=650&height=650')

            msg = await message.channel.send(embed=embed)
            await asyncio.sleep(8)
            await msg.delete()

    await bot.process_commands(message)


async def On_ready():
    print('\033[1;36mFênix ta On\n TLGD?\033[m')

    while True:
        list_guilds = bot.guilds
        servers = len(list_guilds)

        activity = discord.Streaming(name="❓ f!help", url='https://www.twitch.tv/ylost_', type=3)
        await bot.change_presence(status=discord.Status.idle, activity=activity)

        await asyncio.sleep(20)

        activity = discord.Streaming(name=f"📚 Estou em {servers} servidores!", url='https://www.twitch.tv/ylost_',
                                     type=3)
        await bot.change_presence(status=discord.Status.idle, activity=activity)

        # atividade = f"Estou em {servers} servidores!"
        # activity1 = discord.Activity(name=atividade, type=discord.ActivityType.watching)  # status assistindo
        # await bot.change_presence(activity=activity1)

        await asyncio.sleep(20)

        activity = discord.Streaming(name=f"🏡 Fiquem em casa!", url='https://www.twitch.tv/ylost_', type=3)
        await bot.change_presence(status=discord.Status.idle, activity=activity)

        await asyncio.sleep(20)


async def On_guild_remove(guild):
    try:
        inserir = f'DELETE FROM welcome WHERE idserv = {guild.id}'
        cursor.execute(inserir)
        mydb.commit()
    except:
        pass

    inserir = f'DELETE FROM logs WHERE idserv = {guild.id}'
    cursor.execute(inserir)
    mydb.commit()


async def On_member_join(member):
    sqlinsert3 = f'SELECT mensagem FROM welcome WHERE idserv = {member.guild.id}'

    cursor.execute(sqlinsert3)

    message = cursor.fetchone()

    sqlinsert3 = f'SELECT channel FROM welcome WHERE idserv = {member.guild.id}'

    cursor.execute(sqlinsert3)

    canal = cursor.fetchone()

    sqlinsert3 = f'SELECT idserv FROM welcome WHERE idserv = {member.guild.id}'

    cursor.execute(sqlinsert3)

    idserv = cursor.fetchone()

    try:
        guild = bot.get_guild(idserv[0])  # YOUR INTEGER GUILD ID HERE
        welcome_channel = guild.get_channel(canal[0])  # YOUR INTEGER CHANNEL ID HERE
    except:
        pass

    if message[0] == 1:
        embed = discord.Embed(title='***Novo Membro Na Bagaça!***',
                              colour=0x00FFFF,
                              description=f'{member.mention} entrou no servidor {guild} :tulip: :cherries: :shaved_ice:')
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.set_author(name=f'{member}', icon_url=f'{member.avatar_url}')
        embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')

        await welcome_channel.send(embed=embed)
    if message[0] == 2:
        embed = discord.Embed(title='***Novo Membro No Servidor!***',
                              colour=0x00FFFF,
                              description=f'{member.mention} entrou no nosso servidor **{guild}**  <a:giveway:815050719803211786> <a:feliz:815313006937899009>')
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.set_author(name=f'{member}', icon_url=f'{member.avatar_url}')
        embed.set_footer(text=f'{member.guild}', icon_url=f'{member.guild.icon_url}')

        await welcome_channel.send(embed=embed)

    if message[0] == 3:
        await welcome_channel.send(
            f'**Bem Vindo** {member.mention} <a:feliz:815313006937899009> <a:giveway:815050719803211786>\n'
            f'\n'
            f'Leia as nossas regras e **divirta-se** em nosso **Servidor!! <a:fogo:778982001901961216>** \n')
    if message[0] == 4:
        embed = discord.Embed(title='***Novo Membro No Servidor!***',
                              colour=0x00FFFF,
                              description=f'{member.mention} entrou no nosso servidor **{guild}**  <a:giveway:815050719803211786> <a:feliz:815313006937899009>')
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.set_author(name=f'{member}', icon_url=f'{member.avatar_url}')

        await welcome_channel.send(embed=embed)


async def On_guild_join(guild):
    role = discord.utils.find(lambda r: r.name == "Mutado", guild.roles)

    PessoaInvite = await guild.audit_logs(action=discord.AuditLogAction.bot_add).flatten()
    print(PessoaInvite[0])
    if PessoaInvite[0].user == guild.owner:

        embed = discord.Embed(title='Olá! Meu nome é Fênix 🐦',
                              description=f'Obrigado por me **Adicionar** no servidor `{guild.name}`, senhor(a) {PessoaInvite[0].user.mention}.\n\n ***Isso vai me ajudar muito na minha evolução!! 🚀*** ',
                              color=0x00FFFF)

        embed.add_field(name=' ☎️ Servidor Suporte', value='[Suporte](https://discord.gg/VDTAt3Qb9X)')

        embed.add_field(name=' 🕹 Meu Prefixo', value='`F!` ou `f!`')
        await guild.owner.send(embed=embed)


    else:

        embed = discord.Embed(title='Olá! Meu nome é Fênix 🐦',
                              description=f'Aparentemente fui **adicionado** em seu servidor `{guild.name}` pelo administrador {PessoaInvite[0].user}.\n\n ***Obrigado por me escolher!! 😀*** ',
                              color=0x00FFFF)

        embed.add_field(name=' ☎️ Servidor Suporte', value='[ Servidor Suporte](https://discord.gg/VDTAt3Qb9X)')
        embed.add_field(name=' 🕹 Meu Prefixo', value='`F!` ou `f!`')

        await guild.owner.send(embed=embed)

        embed2 = discord.Embed(title='Olá! Meu nome é Fênix 🐦',
                               description=f'Obrigado por me **Adicionar** no servidor `{guild.name}`, senhor(a) {PessoaInvite[0].user.mention}.\n\n ***Isso vai ajudar muito na minha evolução!! 🚀*** ',
                               color=0x00FFFF)

        embed2.add_field(name=' ☎️ Servidor Suporte', value='[Suporte](https://discord.gg/VDTAt3Qb9X)')

        embed2.add_field(name=' 🕹 Meu Prefixo', value='`F!` ou `f!`')

        await PessoaInvite[0].user.send(embed=embed2)

    if role == None:

        perms = discord.Permissions(send_messages=False, read_messages=True)
        await guild.create_role(name='Mutado', permissions=perms)

    else:
        pass

async def On_message_edit(before, after):
    await bot.process_commands(after)