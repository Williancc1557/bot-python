from Principais.principais import bot, mydb, cursor
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






async def Embed(ctx):
    if ctx.message.author.guild_permissions.manage_messages or ctx.author == ctx.guild.owner:
        await ctx.message.delete()
        embed1 = discord.Embed(title='(Titulo)',
                               description='(Descrição)', )
        msg1 = await ctx.channel.send(f':pencil: {ctx.author.mention}', embed=discord.Embed(title='(Titulo)',
                                                                                            description='(Descrição)', ))
        pergunta = await ctx.channel.send('**:pencil:| Escreva o Titulo:**')

        def check(p):
            return p.author == ctx.author and p.channel == ctx.channel

        try:
            til = await bot.wait_for('message', timeout=1000, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send('**Acabou O Tempo Para Aceitar**')
        else:
            titulo = til.content

            await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=discord.Embed(title=f'{titulo}',
                                                                                          description='(Descrição)'))

            await pergunta.edit(content='**:book:| Escreva a descrição:**')
            await til.delete()

            def check(p):
                return p.author == ctx.author and p.channel == ctx.channel

            try:
                desc = await bot.wait_for('message', timeout=1000, check=check)
            except asyncio.TimeoutError:
                return await ctx.channel.send('**Acabou O Tempo Para Editar**')

            else:
                description = desc.content
                await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=discord.Embed(title=f'{titulo}',
                                                                                              description=f'{description}'))
                await desc.delete()

                await pergunta.edit(content='**📷 Deseja colocar uma imagem na embed?**  *Digite Sim ou Não*')

                def check(p):
                    return p.author == ctx.author and p.channel == ctx.channel

                try:
                    desc = await bot.wait_for('message', timeout=1000, check=check)
                except asyncio.TimeoutError:
                    return await ctx.channel.send('**Acabou O Tempo Para Editar**')
                img = desc.content.lower()
                await desc.delete()
                if img == 'sim':
                    await pergunta.edit(
                        content='**📜 digite a url da imagem:**  \n\n*Ex:*\n\n`https://media.discordapp.net/attachments/788064370722340885/788170935018323988/1607733218699.png`'
                                '\n\n'
                                '**Caso não apareça a imagem, significa que:**\n\n'
                                '*A imagem não está com url do discord, ou a Url ta errada!*')

                    def check(p):
                        return p.author == ctx.author and p.channel == ctx.channel

                    try:
                        desc = await bot.wait_for('message', timeout=1000, check=check)
                    except asyncio.TimeoutError:
                        return await ctx.channel.send('**Acabou O Tempo Para Editar**')
                    img = desc.content.lower()
                    await desc.delete()

                    embed = discord.Embed(title=f'{titulo}',
                                          description=f'{description}')
                    embed.set_image(url=img)
                    try:
                        await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                    except:
                        await pergunta.delete()
                        await ctx.send('<:error:788824695184424980> Não consegui gerar uma imagem com essa **URL**!')
                        return

                    # THUMBNAIL

                    await pergunta.edit(content='**🖼 Deseja colocar uma thumbnail na embed?**  *Digite Sim ou Não*')

                    def check(p):
                        return p.author == ctx.author and p.channel == ctx.channel

                    try:
                        desc = await bot.wait_for('message', timeout=1000, check=check)
                    except asyncio.TimeoutError:
                        return await ctx.channel.send('**Acabou O Tempo Para Editar**')
                    thumb1 = desc.content.lower()
                    await desc.delete()

                    if thumb1 == 'sim':

                        await pergunta.edit(
                            content='**📜 digite a url da thumbnail:**  \n\n*Ex:*\n\n`https://media.discordapp.net/attachments/788064370722340885/788170935018323988/1607733218699.png`'
                                    '\n\n'
                                    '**Caso não apareça a imagem, significa que:**\n\n'
                                    '*A imagem não está com url do discord, ou a Url ta errada!*')

                        def check(p):
                            return p.author == ctx.author and p.channel == ctx.channel

                        try:
                            desc = await bot.wait_for('message', timeout=1000, check=check)
                        except asyncio.TimeoutError:
                            return await ctx.channel.send('**Acabou O Tempo Para Editar**')
                        thumb = desc.content.lower()

                        embed = discord.Embed(title=f'{titulo}',
                                              description=f'{description}')
                        embed.set_image(url=img)
                        embed.set_thumbnail(url=thumb)
                        await desc.delete()
                        try:
                            await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                        except:
                            await pergunta.delete()
                            await ctx.send(
                                '<:error:788824695184424980> Não consegui gerar uma thumbnail com essa **URL!**')
                            return
                        await pergunta.edit(
                            content='**:art:| Escolha a cor da embed:**\n\n***Temos as seguintes cores:*** Azul, Rosa, Vermelho, Verde')

                        def check(p):
                            return p.author == ctx.author and p.channel == ctx.channel

                        try:
                            cor = await bot.wait_for('message', timeout=1000, check=check)
                        except asyncio.TimeoutError:
                            return await ctx.channel.send('**Acabou O Tempo Para Aceitar**')
                        color1 = cor.content.lower()
                        if color1 == 'azul':
                            azul = 0x0000FF
                            embed = discord.Embed(title=f'{titulo}',
                                                  description=f'{description}',
                                                  color=azul)

                            try:
                                embed.set_image(url=img)
                                embed.set_thumbnail(url=thumb)
                            except:
                                pass

                            await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)

                            await cor.delete()

                        if color1 == 'rosa':
                            rosa = 0xFF007F
                            embed = discord.Embed(title=f'{titulo}',
                                                  description=f'{description}',
                                                  color=rosa)

                            try:
                                embed.set_image(url=img)
                                embed.set_thumbnail(url=thumb)
                            except:
                                pass

                            await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                            await cor.delete()

                        if color1 == 'vermelho':
                            vermelho = 0xff0000
                            embed = discord.Embed(title=f'{titulo}',
                                                  description=f'{description}',
                                                  color=vermelho)
                            try:
                                embed.set_image(url=img)
                                embed.set_thumbnail(url=thumb)
                            except:
                                pass
                            await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                            await cor.delete()

                        if color1 == 'verde':
                            verde = 0x39ff14
                            embed = discord.Embed(title=f'{titulo}',
                                                  description=f'{description}',
                                                  color=verde)

                            try:
                                embed.set_image(url=img)
                                embed.set_thumbnail(url=thumb)

                            except:
                                pass

                            await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)

                            await cor.delete()

                        if color1 != 'verde' and color1 != 'vermelho' and color1 != 'rosa' and color1 != 'azul':
                            await ctx.channel.send(
                                f'<:error:788824695184424980>| Não encontrei a cor ``{color1}`` no meu sistema')

                        if color1 == 'verde' or color1 == 'vermelho' or color1 == 'rosa' or color1 == 'azul':
                            pass

                        await pergunta.delete()

                        return


                    else:

                        await pergunta.edit(
                            content='**:art:| Escolha a cor da embed:**\n\n***Temos as seguintes cores:*** Azul, Rosa, Vermelho, Verde')

                        def check(p):
                            return p.author == ctx.author and p.channel == ctx.channel

                        try:
                            cor = await bot.wait_for('message', timeout=1000, check=check)
                        except asyncio.TimeoutError:
                            return await ctx.channel.send('**Acabou O Tempo Para Aceitar**')
                        color1 = cor.content.lower()
                        if color1 == 'azul':
                            azul = 0x0000FF
                            embed = discord.Embed(title=f'{titulo}',
                                                  description=f'{description}',
                                                  color=azul)

                            try:
                                embed.set_image(url=img)

                            except:
                                pass

                            await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)

                            await cor.delete()

                        if color1 == 'rosa':
                            rosa = 0xFF007F
                            embed = discord.Embed(title=f'{titulo}',
                                                  description=f'{description}',
                                                  color=rosa)

                            try:
                                embed.set_image(url=img)

                            except:
                                pass

                            await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                            await cor.delete()

                        if color1 == 'vermelho':
                            vermelho = 0xff0000
                            embed = discord.Embed(title=f'{titulo}',
                                                  description=f'{description}',
                                                  color=vermelho)
                            try:
                                embed.set_image(url=img)

                            except:
                                pass
                            await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                            await cor.delete()

                        if color1 == 'verde':
                            verde = 0x39ff14
                            embed = discord.Embed(title=f'{titulo}',
                                                  description=f'{description}',
                                                  color=verde)

                            try:
                                embed.set_image(url=img)


                            except:
                                pass

                            await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)

                            await cor.delete()

                        if color1 != 'verde' and color1 != 'vermelho' and color1 != 'rosa' and color1 != 'azul':
                            await ctx.channel.send(
                                f'<:error:788824695184424980>| Não encontrei a cor ``{color1}`` no meu sistema')

                        if color1 == 'verde' or color1 == 'vermelho' or color1 == 'rosa' or color1 == 'azul':
                            pass

                        await pergunta.delete()

                        return

                    return


                else:

                    pass

                await pergunta.edit(content='**🖼 Deseja colocar uma thumbnail na embed?**  *Digite Sim ou Não*')

                def check(p):
                    return p.author == ctx.author and p.channel == ctx.channel

                try:
                    desc = await bot.wait_for('message', timeout=1000, check=check)
                except asyncio.TimeoutError:
                    return await ctx.channel.send('**Acabou O Tempo Para Editar**')
                thumb1 = desc.content.lower()
                await desc.delete()

                if thumb1 == 'sim':

                    await pergunta.edit(
                        content='**📜 digite a url da thumbnail:**  \n\n*Ex:*\n\n`https://media.discordapp.net/attachments/788064370722340885/788170935018323988/1607733218699.png`'
                                '\n\n'
                                '**Caso não apareça a imagem, significa que:**\n\n'
                                '*A imagem não está com url do discord, ou a Url ta errada!*')

                    def check(p):
                        return p.author == ctx.author and p.channel == ctx.channel

                    try:
                        desc = await bot.wait_for('message', timeout=1000, check=check)
                    except asyncio.TimeoutError:
                        return await ctx.channel.send('**Acabou O Tempo Para Editar**')
                    thumb = desc.content.lower()
                    await desc.delete()

                    embed = discord.Embed(title=f'{titulo}',
                                          description=f'{description}')
                    embed.set_thumbnail(url=thumb)
                    try:
                        await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                    except:
                        await pergunta.delete()
                        await ctx.send('<:error:788824695184424980> Não consegui gerar uma thumbnail com essa **URL**!')
                        return

                    await pergunta.edit(
                        content='**:art:| Escolha a cor da embed:**\n\n***Temos as seguintes cores:*** Azul, Rosa, Vermelho, Verde')

                    def check(p):
                        return p.author == ctx.author and p.channel == ctx.channel

                    try:
                        cor = await bot.wait_for('message', timeout=1000, check=check)
                    except asyncio.TimeoutError:
                        return await ctx.channel.send('**Acabou O Tempo Para Aceitar**')
                    color1 = cor.content.lower()
                    if color1 == 'azul':
                        azul = 0x0000FF
                        embed = discord.Embed(title=f'{titulo}',
                                              description=f'{description}',
                                              color=azul)

                        embed.set_thumbnail(url=thumb)

                        await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)

                        await cor.delete()

                    if color1 == 'rosa':
                        rosa = 0xFF007F
                        embed = discord.Embed(title=f'{titulo}',
                                              description=f'{description}',
                                              color=rosa)
                        embed.set_thumbnail(url=thumb)
                        await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                        await cor.delete()

                    if color1 == 'vermelho':
                        vermelho = 0xff0000
                        embed = discord.Embed(title=f'{titulo}',
                                              description=f'{description}',
                                              color=vermelho)
                        embed.set_thumbnail(url=thumb)
                        await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                        await cor.delete()

                    if color1 == 'verde':
                        verde = 0x39ff14
                        embed = discord.Embed(title=f'{titulo}',
                                              description=f'{description}',
                                              color=verde)
                        embed.set_thumbnail(url=thumb)
                        await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)

                        await cor.delete()

                    if color1 != 'verde' and color1 != 'vermelho' and color1 != 'rosa' and color1 != 'azul':
                        await ctx.channel.send(
                            f'<:error:788824695184424980>| Não encontrei a cor ``{color1}`` no meu sistema')

                    if color1 == 'verde' or color1 == 'vermelho' or color1 == 'rosa' or color1 == 'azul':
                        pass
                    await pergunta.delete()

                await pergunta.edit(
                    content='**:art:| Escolha a cor da embed:**\n\n***Temos as seguintes cores:*** Azul, Rosa, Vermelho, Verde')

                def check(p):
                    return p.author == ctx.author and p.channel == ctx.channel

                try:
                    cor = await bot.wait_for('message', timeout=1000, check=check)
                except asyncio.TimeoutError:
                    return await ctx.channel.send('**Acabou O Tempo Para Aceitar**')
                color1 = cor.content.lower()
                if color1 == 'azul':
                    azul = 0x0000FF
                    embed = discord.Embed(title=f'{titulo}',
                                          description=f'{description}',
                                          color=azul)

                    await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)

                    await cor.delete()

                if color1 == 'rosa':
                    rosa = 0xFF007F
                    embed = discord.Embed(title=f'{titulo}',
                                          description=f'{description}',
                                          color=rosa)

                    await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                    await cor.delete()

                if color1 == 'vermelho':
                    vermelho = 0xff0000
                    embed = discord.Embed(title=f'{titulo}',
                                          description=f'{description}',
                                          color=vermelho)

                    await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)
                    await cor.delete()

                if color1 == 'verde':
                    verde = 0x39ff14
                    embed = discord.Embed(title=f'{titulo}',
                                          description=f'{description}',
                                          color=verde)

                    await msg1.edit(content=f':pencil: {ctx.author.mention}', embed=embed)

                    await cor.delete()

                if color1 != 'verde' and color1 != 'vermelho' and color1 != 'rosa' and color1 != 'azul':
                    await ctx.channel.send(
                        f'<:error:788824695184424980>| Não encontrei a cor ``{color1}`` no meu sistema')

                if color1 == 'verde' or color1 == 'vermelho' or color1 == 'rosa' or color1 == 'azul':
                    pass
                return await pergunta.delete()





    else:
        await ctx.channel.send(
            '<:error:788824695184424980> Você não possui um cargo com a **permissão** de ***gerenciar mensagens***.')





async def Limpar(ctx, amount: int = None):
    if ctx.message.author.guild_permissions.manage_messages or ctx.author == ctx.guild.owner:
        if not amount:
            embed = discord.Embed(
                title='<a:lixo:818920412233859083> Comando para apagar mensagens do chat!! <a:lixo:818920412233859083>\n'
                      '\n'
                      '`f!limpar`\nㅤ',
                description='Seu chat do discord está com muita mensagem? Então utilize esse comando! <:kaway:825740909177077851>\nㅤ',
                color=0x9400D3)
            embed.add_field(name='📚 Como usar', value='`f!limpar <quantidade>`')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/788064370722340885/825745566591221790/lixin.gif')
            ctx.command.reset_cooldown(ctx)
            return await ctx.reply(embed=embed)


        if amount + 1 > 101:
            return await ctx.channel.send('<:error:788824695184424980>| Não posso apagar mais que **100 mensagens**')

        else:
            limit = amount + 1
            a = await ctx.channel.purge(limit=limit, bulk=True,
                                        after=datetime.datetime.now() - datetime.timedelta(days=14))
            print(int(len(a)))
            print(amount + 1)
            if int(len(a)) == amount + 1:
                Apagado = await ctx.channel.send(
                    f'**<a:lixo:818920412233859083>| {ctx.author.mention} apagou {int(len(a)) - 1} mensagen(s)**')



            else:
                Apagado = await ctx.channel.send(
                    f'<a:lixo:818920412233859083>**| {ctx.author.mention} apagou {int(len(a)) - 1} mensagens**\n'
                    f'\n'
                    f'<a:warn:818918476915540020> Parece que não consegui apagar a quantidade de **Mensagens Desejada**, provavelmente, ou o chat não possui mensagens para ser apagadas, ou as mensagens são muito antigas!')

            await asyncio.sleep(20)

            await Apagado.delete()
    else:
        return await ctx.reply(
            f'<:error:788824695184424980>| {ctx.author.mention}Você não possui um cargo com **Permissão** de *Gerenciar Mensagens*')


async def Warn(ctx, member: discord.Member = None, *, motivo: str = 'Motivo Não Especificado!'):

    #CHECKS

    if ctx.author == member:
        return await ctx.reply(
            f'<:error:788824695184424980>| {ctx.author.mention} Você não pode dar warn para **Si Mesmo!**')
    else:
        pass

    if ctx.message.author.guild_permissions.ban_members or ctx.author == ctx.guild.owner:
        pass
    else:
        return await ctx.reply(
            f'<:error:788824695184424980>| {ctx.author.mention} Você precisa ter um cargo com a permissão de **Banir Membros!**')

    if member == ctx.guild.owner:
        return await ctx.reply(
            f'<:error:788824695184424980>| {ctx.author.mention} Não é possivel dar **Warn** no *Dono* do servidor rapaz.')
    try:
        if member.top_role < ctx.author.top_role or ctx.author == ctx.guild.owner:
            pass
        else:
            return await ctx.reply(
                f'<:error:788824695184424980>| {ctx.author.mention}**Seu cargo é menor ou igual que o do {member.mention}**')
    except:
        pass

    #MEMBER = NONE

    if member == None:
        embed = discord.Embed(
            title='<a:warn:818918476915540020> Comando para dar warn em um membro!! <a:warn:818918476915540020>\n'
                  '\n'
                  '`f!warn`\nㅤ',
            description='Tem alguém fazendo **Algo de Errado** no servidor? Utilize esse comando então, quero ver ele(a) continuar bagunçando <:hmm:825743465086058526>\n'
                        '\n'
                        '*Obs: 3 warns = ban*\nㅤ',
            color=0x9400D3)
        embed.add_field(name='📚 Como usar', value='`f!warn <@WiLL> <Motivo>`')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/788064370722340885/825749587737313331/1616944371886.png')

        return await ctx.reply(embed=embed)

    sqlinsert3 = f'SELECT * FROM warn WHERE idserv = {member.guild.id} AND iduser = {member.id}'

    cursor.execute(sqlinsert3)

    verifict = cursor.fetchone()

    print(verifict)

    #   Código

    if verifict == None:

        inserir = 'INSERT INTO warn (idserv, iduser, quantidade) VALUES (%s, %s, %s)'
        dados = (ctx.guild.id, member.id, 1)
        cursor.execute(inserir, dados)
        mydb.commit()

        embed1 = discord.Embed(
            title=f'<a:warn:818918476915540020> Você levou uma warn no servidor `{member.guild.name}`',
            color=0xFF0000,
            timestamp=datetime.datetime.utcnow())

        embed1.add_field(name=f'<a:chorando:818927110646267924> Quantidade de Warns', value=f'1 warn',
                         inline=False)
        embed1.add_field(name=f':police_officer: Penalizado por',
                         value=f'{ctx.author} **ID :** {ctx.author.id}',
                         inline=False)
        embed1.add_field(name=f'<a:emoji_10:778982158458028042> Motivo do Warn', value=f'{motivo}',
                         inline=False)

        embed1.set_thumbnail(url=member.guild.icon_url)
        try:
            await member.send(embed=embed1)
        except:
            pass
        embed2 = discord.Embed(
            title=f'<a:warn:818918476915540020> Membro Penalizado com Sucesso!',
            color=0x00FFFF,
            timestamp=datetime.datetime.utcnow())
        embed2.add_field(name=f'<a:Upd:815312986528677899> Membro', value=f'`{member}` **ID:** {member.id}',
                         inline=False)
        embed2.add_field(name=f'<a:chorando:818927110646267924> Quantidade de Warns', value=f'1 warn(s)',
                         inline=False)
        embed2.add_field(name=f':police_officer: Penalizado por',
                         value=f'{ctx.author.name} **ID :** {ctx.author.id}',
                         inline=False)
        embed2.add_field(name=f'<a:emoji_10:778982158458028042> Motivo do Warn', value=f'{motivo}',
                         inline=False)

        embed2.set_thumbnail(url=member.guild.icon_url)

        return await ctx.reply(embed=embed2)


    else:
        sqlinsert = f"UPDATE warn SET quantidade = '{verifict[2] + 1}' WHERE idserv = {member.guild.id} AND iduser = {member.id}"

        cursor.execute(sqlinsert)

        mydb.commit()

        embed1 = discord.Embed(
            title=f'<a:warn:818918476915540020> Você levou uma warn no servidor `{member.guild.name}`',
            color=0xFF0000,
            timestamp=datetime.datetime.utcnow())

        embed1.add_field(name=f'<a:chorando:818927110646267924> Quantidade de Warns',
                         value=f'{verifict[2] + 1} warn(s)', inline=False)
        embed1.add_field(name=f':police_officer: Penalizado por',
                         value=f'{ctx.author} **ID :** {ctx.author.id}', inline=False)
        embed1.add_field(name=f'<a:emoji_10:778982158458028042> Motivo do Warn', value=f'{motivo}',
                         inline=False)

        embed1.set_thumbnail(url=member.guild.icon_url)

        await member.send(embed=embed1)

        embed2 = discord.Embed(
            title=f'<a:warn:818918476915540020> Membro Penalizado com Sucesso!',
            color=0x00FFFF,
            timestamp=datetime.datetime.utcnow())
        embed2.add_field(name=f'<a:Upd:815312986528677899> Membro', value=f'`{member}` **ID:** {member.id}',
                         inline=False)
        embed2.add_field(name=f'<a:chorando:818927110646267924> Quantidade de Warns',
                         value=f'{verifict[2] + 1} warn(s)',
                         inline=False)
        embed2.add_field(name=f':police_officer: Penalizado por',
                         value=f'{ctx.author.name} **ID :** {ctx.author.id}', inline=False)
        embed2.add_field(name=f'<a:emoji_10:778982158458028042> Motivo do Warn', value=f'{motivo}',
                         inline=False)

        embed2.set_thumbnail(url=member.guild.icon_url)

        await ctx.reply(embed=embed2)

    if verifict[2] + 1 == 3:
        await member.ban(reason='3 warns')




async def Warn_remove(ctx, member: discord.Member):

    if ctx.message.author.guild_permissions.ban_members or ctx.author == ctx.guild.owner:
        pass
    else:
        return await ctx.reply(
            f'<:error:788824695184424980>| {ctx.author.mention} Você precisa ter um cargo com a permissão de **Banir Membros!**')


    #MEMBER = None
    if not member:
        embed = discord.Embed(
            title='<a:warn:818918476915540020> Comando para *Visualizar* Warn(s)!! <a:warn:818918476915540020>\n'
                  '\n'
                  '`f!warn_remove`\nㅤ',
            description='Deseja **Remover** alguma penalização? Então utilize esse comando para a remoção da mesma  <:kaway:825740909177077851>\nㅤ',
            color=0x9400D3)
        embed.add_field(name='📚 Como usar', value='`f!warn_remove <@WiLL>`')
        embed.set_thumbnail(
            url='https://media.discordapp.net/attachments/788064370722340885/825749587737313331/1616944371886.png')

        return await ctx.reply(embed=embed)


    sqlinsert3 = f'SELECT * FROM warn WHERE idserv = {member.guild.id} AND iduser = {member.id}'

    cursor.execute(sqlinsert3)

    verifict = cursor.fetchone()

    if verifict == None:
        return await ctx.reply(
            '<:error:788824695184424980>| Esse membro **Não Possui** warn nesse servidor!')



    if ctx.author == member:
        return await ctx.reply(
            f'<:error:788824695184424980>| {ctx.author.mention} Você não pode remover warn de **Si Mesmo!**')
    else:
        pass

    if member.top_role < ctx.author.top_role or ctx.author == ctx.guild.owner:
        pass
    else:
        return await ctx.reply(
            f'<:error:788824695184424980>| {ctx.author.mention}**Seu cargo é menor ou igual que o do {member.mention}**')

    inserir = f'DELETE FROM warn WHERE idserv = {member.guild.id} AND iduser = {member.id}'
    cursor.execute(inserir)
    mydb.commit()

    embed = discord.Embed(title='<a:verificao_1:815313840354361384> Warn removida com sucesso!',
                          description=f'ㅤ\n'
                                      f'<a:warn:818918476915540020> Todas as **Warns** do `{member}` foram **Removidas!**',
                          color=0x00FF00,
                          timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url=member.guild.icon_url)
    embed.add_field(name=f':police_officer: Removido por', value=f'{ctx.author} **ID :** {ctx.author.id}',
                    inline=False)
    await ctx.reply(embed=embed)

    embed = discord.Embed(
        title=f'<a:feliz:815313006937899009> Suas warn(s) do servidor `{ctx.guild}` foram removidas!',
        color=0x00FF00,
        timestamp=datetime.datetime.utcnow())
    embed.add_field(name=f':police_officer: Removido por', value=f'{ctx.author} **ID :** {ctx.author.id}',
                    inline=False)
    embed.set_thumbnail(url=member.guild.icon_url)
    await member.send(embed=embed)






async def Check_warns(ctx, member: discord.Member = None):


    if not member:
        if not member:
            embed = discord.Embed(
                title='<a:warn:818918476915540020> Comando para *Retirar* Warn(s)!! <a:warn:818918476915540020>\n'
                      '\n'
                      '`f!warn_check`\nㅤ',
                description='Deseja ver a **Quantidade** de warn de alguém? Então utilize esse comando.\nㅤ',
                color=0x9400D3)
            embed.add_field(name='📚 Como usar', value='`f!warn_check <@WiLL>`')
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/825749587737313331/1616944371886.png')

            return await ctx.reply(embed=embed)

    sqlinsert3 = f'SELECT * FROM warn WHERE idserv = {member.guild.id} AND iduser = {member.id}'

    cursor.execute(sqlinsert3)

    verifict = cursor.fetchone()

    if verifict == None:
        embed = discord.Embed(
            title=f'<a:warn:818918476915540020> Warns do(a) `{member}` <a:warn:818918476915540020>',
            color=0xFF0000,
            timestamp=datetime.datetime.utcnow())
        embed.add_field(name=f'<a:chorando:818927110646267924> Quantidade de Warns', value=f'0 warn(s)',
                        inline=False)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f'<a:warn:818918476915540020> Warns do(a) `{member}` <a:warn:818918476915540020>',
            color=0xFF0000,
            timestamp=datetime.datetime.utcnow())
        embed.add_field(name=f'<a:chorando:818927110646267924> Quantidade de Warns',
                        value=f'{verifict[2]} warn(s)',
                        inline=False)
        await ctx.send(embed=embed)


#Mute
async def Mute(ctx, member: discord.Member = None, mute_minutes: int = 0, unit=None):

        if ctx.message.author.guild_permissions.kick_members or ctx.author == ctx.guild.owner:

            if not mute_minutes or not unit or not member:
                embed = discord.Embed(
                    title='<a:muted:815317083427569665> Comando para *Mutar usuários*!! <a:muted:815317083427569665>\n'
                          '\n'
                          '`f!mute`\nㅤ',
                    description='Deseja **Mutar** alguém? Então utilize esse comando.\nㅤ',
                    color=0x9400D3)
                embed.add_field(name='📚 Como usar', value='`f!mute <@WiLL> <temp> <horas, minutos, segundos>`')
                embed.set_thumbnail(
                    url='https://media.discordapp.net/attachments/788064370722340885/825769140248772658/muted.gif')

                return await ctx.reply(embed=embed)
            if member == ctx.guild.owner:
                return await ctx.reply('<:error:788824695184424980>| Não posso banir o **Dono** do servidor! seu bobo')
            try:
                if member.top_role < ctx.author.top_role:
                    pass
                else:
                    return await ctx.reply(
                    f'<:error:788824695184424980>| **{ctx.author.mention} Seu cargo é menor ou igual que o do {member.mention}**')
            except:
                pass

            role = discord.utils.find(lambda r: r.name == "Mutado", ctx.guild.roles)
            if not role:
                return await ctx.reply('**<:error:788824695184424980>| O cargo `Mutado` não existe no servidor**')
            await member.add_roles(role)
            eu = bot.get_user(id=member.id)



            if unit == "segundos" or unit == 'segundo':
                wait = 1 * mute_minutes
                await ctx.reply(
                    f"**O {member.mention} foi mutado por {ctx.author.mention} por {mute_minutes} segundo(s)!** ")
                m = await ctx.channel.send(
                    '**Deseja enviar no privado do mesmo o motivo do mute?**\n\n***Escreva: Sim ou Não***')

                def check(p):
                    return p.author == ctx.author and p.channel == ctx.channel

                try:
                    msg = await bot.wait_for('message', timeout=1000, check=check)
                except asyncio.TimeoutError:
                    return await ctx.channel.send('**Acabou O Tempo Para Editar**')

                else:
                    privado = str(msg.content).lower()
                    await msg.delete()

                    if privado == 'sim':
                        await m.edit(content='**Qual foi o motivo?**')

                        def check(p):
                            return p.author == ctx.author and p.channel == ctx.channel

                        try:
                            msg1 = await bot.wait_for('message', timeout=1000, check=check)
                        except asyncio.TimeoutError:
                            return await ctx.channel.send('**Acabou O Tempo Para Editar**')

                        else:
                            privado1 = str(msg1.content).lower()
                            await msg1.delete()
                            editar1 = await ctx.channel.send(
                                f'<a:loading:785523240944664646> **Enviando Aviso**')
                            await asyncio.sleep(4)
                            await editar1.edit(content=':white_check_mark:  **Aviso Enviado**')
                            await eu.send(f'Você foi mutado por {ctx.author.name} pelo motivo: {privado1}')
                    else:
                        await m.delete()
                        l = await ctx.channel.send('Ok')
                        await asyncio.sleep(3)
                        await l.delete()
                await asyncio.sleep(wait)

            elif unit == "minutos" or unit == 'minuto':
                wait = 60 * mute_minutes
                await ctx.reply(f"**O {member.mention} foi mutado por {ctx.author.mention} por {mute_minutes} minuto(s)!** ")
                m = await ctx.channel.send(
                    '**Deseja enviar no privado do mesmo o motivo do mute?**\n\n***Escreva: Sim ou Não***')

                def check(p):
                    return p.author == ctx.author and p.channel == ctx.channel

                try:
                    msg = await bot.wait_for('message', timeout=1000, check=check)
                except asyncio.TimeoutError:
                    return await ctx.channel.send('**Acabou O Tempo Para Editar**')

                else:
                    privado = str(msg.content).lower()
                    await msg.delete()

                    if privado == 'sim':
                        await m.edit(content='**Qual foi o motivo?**')

                        def check(p):
                            return p.author == ctx.author and p.channel == ctx.channel

                        try:
                            msg1 = await bot.wait_for('message', timeout=1000, check=check)
                        except asyncio.TimeoutError:
                            return await ctx.channel.send('**Acabou O Tempo Para Editar**')

                        else:
                            privado1 = str(msg1.content).lower()
                            await msg1.delete()
                            editar1 = await ctx.channel.send(
                                f'<a:loading:785523240944664646>  **Enviando Aviso**')
                            await asyncio.sleep(4)
                            await editar1.edit(content=':white_check_mark:  **Aviso Enviado**')
                            await eu.send(f'Você foi mutado por {ctx.author.name} pelo motivo: {privado1}')
                    else:
                        m.delete()
                        l = await ctx.channel.send('Ok')
                        await asyncio.sleep(3)
                        await l.delete()
                await asyncio.sleep(wait)
            elif unit == 'horas' or unit == 'hora':
                wait = 3600 * mute_minutes
                await ctx.reply(
                    f"**O {member.mention} foi mutado por {ctx.author.mention} por {mute_minutes} hora(s)!** ")
                m = await ctx.channel.send(
                    '**Deseja enviar no privado do mesmo o motivo do mute?**\n\n***Escreva: Sim ou Não***')

                def check(p):
                    return p.author == ctx.author and p.channel == ctx.channel

                try:
                    msg = await bot.wait_for('message', timeout=1000, check=check)
                except asyncio.TimeoutError:
                    return await ctx.channel.send('**Acabou O Tempo Para Editar**')

                else:
                    privado = str(msg.content).lower()
                    await msg.delete()

                    if privado == 'sim':
                        await m.edit(content='**Qual foi o motivo?**')

                        def check(p):
                            return p.author == ctx.author and p.channel == ctx.channel

                        try:
                            msg1 = await bot.wait_for('message', timeout=1000, check=check)
                        except asyncio.TimeoutError:
                            return await ctx.channel.send('**Acabou O Tempo Para Editar**')

                        else:
                            privado1 = str(msg1.content).lower()
                            await msg1.delete()
                            editar1 = await ctx.channel.send(
                                f'<a:loading:785523240944664646>  **Enviando Aviso**')
                            await asyncio.sleep(4)
                            await editar1.edit(content=':white_check_mark:  **Aviso Enviado**')
                            await eu.send(f'Você foi mutado por {ctx.author.name} pelo motivo: {privado1}')
                            await m.delete()
                    else:
                        l = await ctx.channel.send('Ok')
                        await asyncio.sleep(3)
                        await l.delete()
                        await m.delete()
                await asyncio.sleep(wait)



            else:
                await ctx.reply("Escreva no formato `f!mute (@pessoa) (tempo) (segundos, minutos, horas)`")
                return





            await member.remove_roles(role)
            await ctx.channel.send(f"O {member.mention} foi desmutado.")
            return False
        else:
            await ctx.reply(f'**<:error:788824695184424980>| {ctx.author.mention}Você não possui um cargo com permissão para kickar membros**')



#unmute



async def Unmute(ctx, member: discord.Member = None):
    if ctx.message.author.guild_permissions.kick_members or ctx.author == ctx.guild.owner:
        if not member:
            embed = discord.Embed(
                title='<a:muted:815317083427569665> Comando para *Desmutar usuários*!! <a:muted:815317083427569665>\n'
                      '\n'
                      '`f!unmute`\nㅤ',
                description='Deseja **Desmutar** alguém? Então utilize esse comando.\nㅤ',
                color=0x9400D3)
            embed.add_field(name='📚 Como usar', value='`f!unmute <@WiLL>`')
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/825769140248772658/muted.gif')

            return await ctx.reply(embed=embed)

        if member.top_role < ctx.author.top_role or ctx.author == ctx.guild.owner:
            editar = await ctx.reply(f'<a:loading:785523240944664646>  **Desmutando o(a) {member.mention}!**')
            await asyncio.sleep(4)
            await member.remove_roles(discord.utils.find(lambda r: r.name == "Mutado", ctx.guild.roles))
            return await editar.edit(content=':white_check_mark:  **Membro Desmutado**')
        else:
            return await ctx.reply(
                f'<:error:788824695184424980>| {ctx.author.mention}**Seu cargo é menor ou igual que o do {member.mention}**')
    else:
        return await ctx.reply(
            f'<:error:788824695184424980>| {ctx.author.mention}Você não possui um cargo com **Permissão** de *kickar membros*')











#BAN

async def Ban(ctx, member: discord.Member, *, reason='*Motivo não especificado*'):
    if ctx.message.author.guild_permissions.ban_members or ctx.author == ctx.guild.owner:

        if not member:
            embed = discord.Embed(
                title='<a:ban:815316725402566666> Comando para *Banir*!! <a:ban:815316725402566666>\n'
                      '\n'
                      '`f!ban`\nㅤ',
                description='Deseja **Banir** aquele membro chato? Então utilize esse comando.\nㅤ',
                color=0x9400D3)
            embed.add_field(name='📚 Como usar', value='`f!ban <@WiLL> motivo`')
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/825772453187682334/banned.gif')

            return await ctx.reply(embed=embed)
        if member == bot.user:
            return await ctx.channel.send('<:error:788824695184424980>| Não posso me **banir** bobinho kk.')

        if member == ctx.guild.owner:
            return await ctx.reply('<:error:788824695184424980>| Não posso banir o **Dono** do servidor! seu bobo')

        if member.top_role < ctx.author.top_role or ctx.author == ctx.guild.owner:

            msg = await ctx.reply(f'<a:warn:818918476915540020> Deseja realmente **Banir** o(a) `{member}`?\n'
                                  f'\n'
                                  f'**Motivo:** {reason}\n'
                                  '\n'
                                  '**Caso realmente deseja banir essa pessoa, clique na reação** <a:verificao_1:815313840354361384>.\n'
                                  '**Não quer mais banir essa pessoa? Clique na reação** <:error:788824695184424980>'

                                  )
            await msg.add_reaction('<a:verificao_1:815313840354361384>')

            await msg.add_reaction('<:error:788824695184424980>')

            def check(reaction, user):
                print(reaction)
                return ctx.author == user and str(
                    reaction) == '<a:verificao_1:815313840354361384>' or ctx.author == user and str(
                    reaction) == '<:error:788824695184424980>'

            try:
                reaction, user = await bot.wait_for('reaction_add', check=check, timeout=50)
            except asyncio.TimeoutError:
                return False
            else:
                print(reaction, user)

            if str(reaction) == '<a:verificao_1:815313840354361384>':
                pass
            else:
                return await msg.delete()

            embed1 = discord.Embed(title=f':no_entry_sign:Você foi banido do {member.guild.name}',
                                   description=f'**:police_officer:Banido por:**\n{ctx.author.display_name}\n:pencil:**Motivo:**\n{reason}',
                                   color=0xFF0000,
                                   timestamp=datetime.datetime.utcnow())
            embed1.set_thumbnail(url=member.guild.icon_url)
            await msg.delete()
            try:
                await member.ban(reason=reason)
            except:
                return await ctx.reply(
                    '<:error:788824695184424980>| Por algum motivo eu **Não Consegui** banir essa pessoa!')

            try:
                await member.send(embed=embed1)


            except:
                pass

            embed2 = discord.Embed(title=f':no_entry_sign: Membro {member} banido com sucesso!',
                                   description=f'**:police_officer:Banido por:**\n{ctx.author}\n:pencil:**Motivo:**\n{reason}',
                                   color=0x00FF00,
                                   timestamp=datetime.datetime.utcnow())
            num = random.randint(1, 2)

            if num == 1:
                embed2.set_image(
                    url='https://media.discordapp.net/attachments/778295088753016903/785811979088429067/07155146350102.gif?width=617&height=473')
            if num == 2:
                embed2.set_image(
                    url='https://media.discordapp.net/attachments/778295088753016903/785816768533889034/ban1.gif')
            embed2.set_thumbnail(url=ctx.author.guild.icon_url)

            a = await ctx.reply(embed=embed2)

            await asyncio.sleep(25)
            await a.delete()
            return False


        else:
            return await ctx.channel.send(
                f'<:error:788824695184424980>| {ctx.author.mention}**Seu cargo é menor ou igual que o do {member.mention}**')
    else:
        return await ctx.channel.send(
            '<:error:788824695184424980>| Você precisa ter um cargo com a **Permissão** de *Banir Membros!*')


async def Unban(ctx, id: int):
    if not id:
        embed = discord.Embed(
            title='<a:ban:815316725402566666> Comando para *Desbanir*!! <a:ban:815316725402566666>\n'
                  '\n'
                  '`f!unban`\nㅤ',
            description='Deseja **Desbanir** alguem? Então utilize esse comando.\nㅤ',
            color=0x9400D3)
        embed.add_field(name='📚 Como usar', value='`f!unban <user_id>`')
        embed.set_thumbnail(
            url='https://media.discordapp.net/attachments/788064370722340885/825772453187682334/banned.gif')

        return await ctx.reply(embed=embed)
    if ctx.message.author.guild_permissions.ban_members or ctx.author == ctx.guild.owner:
        user = await bot.fetch_user(id)
        try:
            await ctx.guild.unban(user)
        except:
            return await ctx.reply(f'<:error:788824695184424980>| Não encontrei **Nenhum** usuário com o id {id}')

        embed40 = discord.Embed(title=':white_check_mark:  **Membro Desbanido**',
                                color=0xFF0000,
                                timestamp=datetime.datetime.utcnow())
        return await ctx.reply(f'{ctx.author.mention}', embed=embed40)
    else:
        embed30 = discord.Embed(
            title='**<:error:788824695184424980>| Você precisa ter um cargo com a permissão de banir membros!**',
            color=0xFF0000)
        return await ctx.reply(f':x: {ctx.author.mention}', embed=embed30)