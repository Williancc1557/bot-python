from Principais.principais import bot, mydb, cursor, color

import discord
import asyncio
import discord
import asyncio
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
import datetime
import psycopg2
import time


bot = bot
mydb = mydb
cursor = cursor
color = color


async def Add_suporte(ctx, member: discord.Member = None):
    if ctx.author.id == 567757366506815488 or ctx.author.id == 597777716011335682:
        pessoa = member.id
        sqlinsert2 = f'SELECT permmissão FROM admin WHERE id = {pessoa}'

        cursor.execute(sqlinsert2)

        valores_lidos2 = cursor.fetchone()
        try:
            print(valores_lidos2[0])
            await ctx.channel.send('<:error:788824695184424980> **Esse usuário já faz parte da equipe de suporte**')
            return
        except:

            inserir = 'INSERT INTO admin (id, permmissão) VALUES (%s, %s)'
            dados = (pessoa, 'sim')
            cursor.execute(inserir, dados)
            mydb.commit()
            await ctx.channel.send(':white_check_mark: **Adicionado na suporte com sucesso!**')

            embed1 = discord.Embed(title='Parabéns',
                                description='Agora você faz parte do suporte do fênix!!',
                                color=0xFFFF00)
            embed1.set_thumbnail(url='https://media.discordapp.net/attachments/778295088753016903/787245337295060992/1607735746221.png')

            await member.send(embed=embed1)
    else:
        await ctx.channel.send('<:error:788824695184424980> **Você não possui permissão para dar esse comando!**')



async def Remove_suporte(ctx, member: discord.Member = None):
    if ctx.author.id == 567757366506815488 or ctx.author.id == 597777716011335682:
        pessoa = member.id
        inserir = f'DELETE FROM admin WHERE id = {pessoa}'
        cursor.execute(inserir)
        mydb.commit()
        await ctx.channel.send(':white_check_mark: **Removido na suporte com sucesso!**')

        embed1 = discord.Embed(title='Que triste',
                              description='Você não faz mais parte do suporte do fênix.',
                              color=0xFFFF00)
        embed1.set_thumbnail(url='https://media.discordapp.net/attachments/778295088753016903/787245337295060992/1607735746221.png')

        await member.send(embed=embed1)
    else:
        await ctx.channel.send('<:error:788824695184424980> **Você não possui permissão para dar esse comando!**')

async def Identificar(ctx, member: discord.Member = None):
    sqlinsert3 = f'SELECT permmissão FROM admin WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert3)

    valores_lidos3 = cursor.fetchone()
    try:
        if valores_lidos3[0] == 'sim':
            sqlinsert2 = f'SELECT permmissão FROM admin WHERE id = {member.id}'

            cursor.execute(sqlinsert2)

            valores_lidos2 = cursor.fetchone()

            try:
                if valores_lidos2[0] == 'sim':
                    await ctx.channel.send(f':white_check_mark: **{member} faz parte da equipe de suporte**')

            except:
                await ctx.channel.send('<:error:788824695184424980> **Esse membro não faz parte da equipe suporte **')
    except:
        await ctx.channel.send('<:error:788824695184424980> **Você não tem permissão para usar esse comando**')


async def Clean_fenix(ctx, amount=10):
    sqlinsert3 = f'SELECT permmissão FROM admin WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert3)

    valores_lidos3 = cursor.fetchone()
    try:
        if valores_lidos3[0] == 'sim':
            def is_me(m):
                return m.author == bot.user

            deleted = await ctx.channel.purge(limit=amount + 1, check=is_me)
            await ctx.channel.send(':white_check_mark: **deletado {} mensagens do fênix nesse canal**'.format(amount))
        else:
            await ctx.channel.send('<:error:788824695184424980> **Você não tem permissão para dar esse comando**')
    except:
        await ctx.channel.send('<:error:788824695184424980> **Você não tem permissão para usar esse comando**')


async def Ajuda_suporte(ctx):
    sqlinsert3 = f'SELECT permmissão FROM admin WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert3)

    valores_lidos3 = cursor.fetchone()
    try:
        if valores_lidos3[0] == 'sim':
            embed = discord.Embed(
                title='**<a:Top:815388123039006741>Painel Suporte Fênix<a:Top:815388123039006741>**',
                color=color,
                description='***Comandos da equipe suporte:***\n\n`identificar (@user)` : identificar quem é da equipe de suporte\n`add_fenicoins` : Adicionar fenicoin em alguém\n`remove_fenicoins` : Remover fenicoin de alguém\n`set_fenicoins` : Setar fenicoins em alguèm\n`clean_fenix (valor)` : Limpa mensagens do fênix em um canal\n`add_suporte (@user)` : adicionar alguém na suporte\n`remove_suporte` : remover alguém da equipe de suporte\n`ban_fenix (id/user) (motivo)`\n`unban_fenix (id/user)`')
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/787270440283406399/787289422164131870/1607735746221.png')

            await ctx.channel.send(ctx.author.mention, embed=embed)
            await ctx.message.delete()
    except:
        await ctx.channel.send('<:error:788824695184424980> **Você não tem permissão para usar esse comando**')


async def Add_fenicoins(ctx, member: discord.Member, valor: int):
    if ctx.author.id == 567757366506815488 or ctx.author.id == 597777716011335682:
        sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {member.id}'

        cursor.execute(sqlinsert2)

        valores_lidos2 = cursor.fetchone()

        try:
            print(valores_lidos2[0])
        except:
            await ctx.channel.send(embed=discord.Embed(
                title='<:error:788824695184424980> **Esse usuário não possui uma conta no fênix!!**',
                color=0xFF0000))
            return

        sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] + valor}' WHERE id = {member.id}"

        cursor.execute(sqlinsert)

        mydb.commit()
        await ctx.channel.send(
            embed=discord.Embed(title=f':white_check_mark: Adicionado {valor} *fenicoins* para o(a) {member}',
                                color=0x00FF00))
    else:
        await ctx.channel.send('<:error:788824695184424980> **Você não tem permissão para usar esse comando**')


async def Remove_fenicoins(ctx, member: discord.Member, valor: int):
    if ctx.author.id == 567757366506815488 or ctx.author.id == 597777716011335682:
        sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {member.id}'

        cursor.execute(sqlinsert2)

        valores_lidos2 = cursor.fetchone()

        try:
            print(valores_lidos2[0])
        except:
            await ctx.channel.send(embed=discord.Embed(title='<:error:788824695184424980> **Esse usuário não possui uma conta no fênix!!**',
                                                       color=0xFF0000))
            return

        sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - valor}' WHERE id = {member.id}"

        cursor.execute(sqlinsert)

        mydb.commit()
        await ctx.channel.send(embed=discord.Embed(title=f':white_check_mark: Removido {valor} *fenicoins* do(a) {member}',
                                                   color=0xFF0000))
    else:
        await ctx.channel.send('<:error:788824695184424980> **Você não tem permissão para usar esse comando**')


async def Set_fenicoins(ctx, member: discord.Member, valor: int):
    if ctx.author.id == 567757366506815488 or ctx.author.id == 597777716011335682:

        sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {member.id}'

        cursor.execute(sqlinsert2)

        valores_lidos2 = cursor.fetchone()

        try:
            print(valores_lidos2[0])
        except:
            await ctx.channel.send(embed=discord.Embed(title='<:error:788824695184424980> **Esse usuário não possui uma conta no fênix!!**',
                                                       color=0xFF0000))
            return

        sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valor}' WHERE id = {member.id}"

        cursor.execute(sqlinsert)

        mydb.commit()
        await ctx.channel.send(embed=discord.Embed(title=f':white_check_mark: Setado {valor} *fenicoins* no(a) {member}',
                                                   color=0x00FF00))
    else:
        await ctx.channel.send('<:error:788824695184424980> **Você não tem permissão para usar esse comando**')


async def Ban_fenix(ctx, member, *, motivo: str = 'Motivo não especificado!'):
    if member == 567757366506815488:
        return

    member = await bot.fetch_user(int(member))

    sqlinsert3 = f'SELECT permmissão FROM admin WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert3)

    valores_lidos3 = cursor.fetchone()
    if valores_lidos3[0] == 'sim':
        inserir = 'INSERT INTO ban (idban, motivo) VALUES (%s, %s)'
        dados = (int(member.id), motivo)
        try:
            cursor.execute(inserir, dados)
            mydb.commit()

            await ctx.send("***Usuário banido com sucesso!*** \n"
                           f"**motivo:** {motivo}\n"
                           f"**Tempo:** Permanente!")
        except:
            return await ctx.send("**Este usuário já está banido!**")

        embed1 = discord.Embed(title=f':no_entry_sign:Você foi banido do fênix',
                               description=f'**:police_officer:Banido por:**\n{ctx.author}\n:pencil:**Motivo:**\n{motivo}',
                               color=0xFF0000,
                               timestamp=datetime.datetime.utcnow())
        embed1.set_thumbnail(url='https://media.discordapp.net/attachments/788064370722340885/788170896363618345/1607735746221.png')


        await member.send(embed=embed1)

    else:
        return


async def Unban_fenix(ctx, member: int):
    if member == 567757366506815488:
        return

    member = await bot.fetch_user(int(member))

    sqlinsert3 = f'SELECT permmissão FROM admin WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert3)

    valores_lidos3 = cursor.fetchone()
    if valores_lidos3[0] == 'sim':
        inserir = f'DELETE FROM ban WHERE idban = {member.id}'
        cursor.execute(inserir)
        mydb.commit()

        embed1 = discord.Embed(title=f':no_entry_sign:Você foi Desbanido do fênix',
                               description=f'**:police_officer:Desbanido por:**\n{ctx.author}',
                               color=0xFF0000,
                               timestamp=datetime.datetime.utcnow())
        embed1.set_thumbnail(
            url='https://media.discordapp.net/attachments/788064370722340885/788170896363618345/1607735746221.png')


        await ctx.send('Desbanido!')
        await member.send(embed=embed1)