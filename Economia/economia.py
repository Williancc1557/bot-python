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


async def Criar_conta(ctx):
    try:
        d = await ctx.channel.send(embed=discord.Embed(title=':floppy_disk: Escreva o nome da conta: '))

        def check(p):
            return p.author == ctx.author and p.channel == ctx.channel

        try:
            msg1 = await bot.wait_for('message', timeout=1000, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send('**Acabou O Tempo**')
        else:
            nome = str(msg1.content).strip()

        await d.delete()
        await msg1.delete()

        a = await ctx.channel.send(embed=discord.Embed(title=':clipboard: Escreva a descrição da conta: '))

        def check(p):
            return p.author == ctx.author and p.channel == ctx.channel

        try:
            msg2 = await bot.wait_for('message', timeout=1000, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send('**Acabou O Tempo**')
        else:
            descriçao = str(msg2.content)

        await a.delete()
        await msg2.delete()

        def check(p):
            return p.author == ctx.author and p.channel == ctx.channel

        pessoa = ctx.author.id

        sqlinsert = f'SELECT descrição FROM dinheiro WHERE id = {pessoa}'

        cursor.execute(sqlinsert)

        valores_lidos = cursor.fetchone()

        arma = -1
        try:
            print(valores_lidos[0])
            await ctx.channel.send('<:error:788824695184424980> **Ops, Parece que você já possui um registro!!**')
            return
        except:

            dindin = 200
            cor = '000000'
            inserir = 'INSERT INTO dinheiro (id, nome, descrição, dinheiro, cor, arma) VALUES (%s, %s, %s, %s, %s, %s)'
            dados = (pessoa, nome, descriçao, dindin, cor, arma)
            cursor.execute(inserir, dados)
            mydb.commit()
            msg1 = await ctx.channel.send(embed=discord.Embed(title='<a:loading:785523240944664646> Criando conta ',
                                                              color=0xFF69B4))
            await asyncio.sleep(4)
            await msg1.edit(embed=discord.Embed(title=':white_check_mark: **Conta criada**',
                                            color=0x00FF00))
    except:
        await ctx.channel.send(f'<:error:788824695184424980>  Ops, parece que utilizou caracteres diferente desses: **a, b, c** no seu nome, ou escreveu um nome com mais de 30 caractéres! {ctx.author.mention}')


async def Conta(ctx,  member: discord.Member = None):
    pessoa = ctx.author.id

    if not member:

        try:
            sqlinsert = f'SELECT descrição FROM dinheiro WHERE id = {pessoa}'

            cursor.execute(sqlinsert)

            valores_lidos = cursor.fetchone()

            sqlinsert1 = f'SELECT dinheiro FROM dinheiro WHERE id = {pessoa}'

            cursor.execute(sqlinsert1)

            valores_lidos1 = cursor.fetchone()

            sqlinsert2 = f'SELECT nome FROM dinheiro WHERE id = {pessoa}'

            cursor.execute(sqlinsert2)

            valores_lidos2 = cursor.fetchone()

            sqlinsert3 = f'SELECT cor FROM dinheiro WHERE id = {pessoa}'

            cursor.execute(sqlinsert3)

            valores_lidos3 = cursor.fetchone()

            v = 0x0 + int(valores_lidos3[0])

            sqlinsert4 = f'select id from dinheiro ORDER BY dinheiro desc'

            cursor.execute(sqlinsert4)

            valores_lidos4 = cursor.fetchall()

            for index, element in enumerate(valores_lidos4):
                if element[0] == pessoa:
                    num = index + 1
                    break

            embed = discord.Embed(
                title='Sua conta no fênix: ',
                description=f'ㅤ\n**Discord name:** {ctx.author.name}\n\n**Nome da conta:** {valores_lidos2[0]}\n**Descrição:** {valores_lidos[0]}\n**Dinheiro:** {valores_lidos1[0]} *fenicoins*',
                color=v)
            embed.set_footer(text=f'Você está em #{num} lugar no ranking')
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/811621833484140555/edificio-de-banco-retro-dos-desenhos-animados-ou-tribunal-com-ilustracao-de-colunas-isolada-no-branc.png')
            embed.set_author(name=ctx.author.name, icon_url=str(ctx.author.avatar_url))
            await ctx.reply(embed=embed)
        except:
            await ctx.channel.send(
                embed=discord.Embed(title='<:error:788824695184424980> ** Você não possui uma conta no fênix!!**',
                                    color=0xFF0000))
    else:
        membro = member.id
        sqlinsert = f'SELECT descrição FROM dinheiro WHERE id = {membro}'

        cursor.execute(sqlinsert)

        valores_lidos = cursor.fetchone()

        sqlinsert1 = f'SELECT dinheiro FROM dinheiro WHERE id = {membro}'

        cursor.execute(sqlinsert1)

        valores_lidos1 = cursor.fetchone()

        sqlinsert2 = f'SELECT nome FROM dinheiro WHERE id = {membro}'

        cursor.execute(sqlinsert2)

        valores_lidos2 = cursor.fetchone()
        sqlinsert3 = f'SELECT cor FROM dinheiro WHERE id = {member.id}'

        cursor.execute(sqlinsert3)

        valores_lidos3 = cursor.fetchone()

        sqlinsert4 = f'select id from dinheiro ORDER BY dinheiro desc'

        cursor.execute(sqlinsert4)

        valores_lidos4 = cursor.fetchall()

        for index, element in enumerate(valores_lidos4):
            if element[0] == member.id:
                num1 = index + 1
                break

        try:
            embed1 = discord.Embed(
                title=f'Conta do {member.name} no fênix: ',
                description=f'ㅤ\n**Discord name:** {member.name}\n\n**Nome da conta:** {valores_lidos2[0]}\n**Descrição:** {valores_lidos[0]}\n**Dinheiro:** {valores_lidos1[0]} *fenicoins*',
                color=0x0 + int(valores_lidos3[0]))
            embed1.set_footer(text=f'{member} está em #{num1} no ranking')
            embed1.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/811621833484140555/edificio-de-banco-retro-dos-desenhos-animados-ou-tribunal-com-ilustracao-de-colunas-isolada-no-branc.png')
            embed1.set_author(name=member.name, icon_url=str(member.avatar_url))
            await ctx.channel.send(embed=embed1)
        except:
            await ctx.channel.send(embed=discord.Embed(
                title='<:error:788824695184424980> ** Este usuário não possui uma conta no fênix!!**',
                color=0xFF0000))



async def Desc_edit(ctx):
    pessoa = ctx.author.id

    sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert2)

    valores_lidos2 = cursor.fetchone()

    try:
        print(sqlinsert2)
    except:
        await ctx.channel.send(
            embed=discord.Embed(title='<:error:788824695184424980> ** Você não possui uma conta no fênix!!**',
                                color=0xFF0000))
        return

    if valores_lidos2[0] >= 5000:
        a = await ctx.channel.send(ctx.author.mention, embed=discord.Embed(
            title=f'Tem certeza que deseja **mudar a sua descrição** por **5000 de *fenicoins* ** ? Sim ou Não',
            color=0xffff00))

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg25 = await bot.wait_for('message', timeout=1000.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send(
                '***Demorou De Mais Para Aceitar.***')
        else:
            resposta25 = str(msg25.content).lower()

        if resposta25 == 'sim':
            await a.delete()

            d = await ctx.channel.send('**Escreva a sua nova descrição:** ')

            def check(p):
                return p.author == ctx.author and p.channel == ctx.channel

            try:
                msg2 = await bot.wait_for('message', timeout=1000, check=check)
            except asyncio.TimeoutError:
                return await ctx.channel.send('**Acabou O Tempo**')
            else:
                adescriçao = str(msg2.content)
            sqlinsert = f"UPDATE dinheiro SET descrição = '{adescriçao}' WHERE id = {pessoa}"

            cursor.execute(sqlinsert)

            mydb.commit()
            dinheiro = 5000
            await d.delete()
            await msg2.delete()
            sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - dinheiro}' WHERE id = {pessoa}"

            cursor.execute(sqlinsert)

            mydb.commit()
            editar1 = await ctx.channel.send(
                f'<a:loading:785523240944664646>  **Editando descrição**')
            await asyncio.sleep(4)
            await editar1.edit(content=':white_check_mark: **Descrição editada**')

        else:
            a.delete()
            await ctx.channel.send('<:error:788824695184424980> Compra cancelada')

    else:
        await ctx.channel.send('<:error:788824695184424980> Você não possui **5000 *fenicoins* **')


async def Transferir(ctx,  member: discord.Member = None, dinheiro: int = 10):
    if not member or not dinheiro:
        await ctx.channel.send('<:error:788824695184424980> **Rescreva o comando no seguinte formato:** `f!transferir (@user) (valor)`')
        return
    pessoa = ctx.author.id
    membro = member.id
    if 0 < dinheiro:
        try:
            sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {ctx.author.id}'

            cursor.execute(sqlinsert2)

            valores_lidos2 = cursor.fetchone()

            print(valores_lidos2[0])
        except:
            await ctx.channel.send(embed=discord.Embed(title='<:error:788824695184424980> ** Você não possui uma conta no fênix!!**',
                                                   color=0xFF0000))
            return

        if valores_lidos2[0] >= dinheiro:
            await ctx.channel.send(embed=discord.Embed(title=f'Tem certeza que **deseja transferir** {dinheiro} *fenicoins* para {member} ? Sim ou Não',
                                                 color=0xffff00))

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            try:
                msg25 = await bot.wait_for('message', timeout=1000.0, check=check)
            except asyncio.TimeoutError:
                return await ctx.channel.send(
                    '***Demorou De Mais Para Aceitar.***')
            else:
                resposta25 = str(msg25.content).lower()

            if resposta25 == 'sim':

              try:
                sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - dinheiro}' WHERE id = {pessoa}"

                cursor.execute(sqlinsert)

                mydb.commit()

                sqlinsert3 = f'SELECT dinheiro FROM dinheiro WHERE id = {membro}'

                cursor.execute(sqlinsert3)

                valores_lidos3 = cursor.fetchone()
                print(valores_lidos3[0])
                sqlinsert1 = f"UPDATE dinheiro SET dinheiro = '{valores_lidos3[0] + dinheiro}' WHERE id = {membro}"

                cursor.execute(sqlinsert1)

                mydb.commit()

                await ctx.channel.send(f':white_check_mark: {ctx.author.mention} transferiu **{dinheiro} *fenicoins* ** para {member.mention} com sucesso!!')
              except:
                  await ctx.channel.send('<:error:788824695184424980> ** Esse usuário não possui uma conta no fênix!!**')
            else:
                await ctx.channel.send('<:error:788824695184424980> Transferência cancelada!')

        else:
            await ctx.message.delete()
            await ctx.channel.send(f'<:error:788824695184424980> Olá {ctx.author.mention}, Você não possui **saldo suficiente** para a transferência!')

    else:
        await ctx.message.delete()
        await ctx.channel.send(f'<:error:788824695184424980> Ue {ctx.author.mention}, vai transferir **dinheiro negativo**? k k k')



async def Diaria(ctx):
    pessoa = ctx.author.id
    sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert2)

    valores_lidos2 = cursor.fetchone()

    try:
        print(valores_lidos2[0])
    except:
        await ctx.channel.send(
            embed=discord.Embed(title='<:error:788824695184424980> ** Você não possui uma conta no fênix!!**',
                                color=0xFF0000))
        ctx.command.reset_cooldown(ctx)
        return
    num = random.randint(500, 7000)

    sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] + num}' WHERE id = {pessoa}"

    cursor.execute(sqlinsert)

    mydb.commit()

    embed = discord.Embed(title=f'<a:giveway:815050719803211786> Parabéns Você recebeu: {num} *fenicoins*',
                          color=0xffae00)


    await ctx.channel.send(embed=embed)




async def Cor(ctx):
    sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert2)

    valores_lidos2 = cursor.fetchone()
    try:
        print(valores_lidos2[0])
    except:
        await ctx.channel.send(
            embed=discord.Embed(title='<:error:788824695184424980> ** Você não possui uma conta no fênix!!**',
                                color=0xFF0000))
        return

    a = await ctx.channel.send('**Oque você deseja?\n'
                               '[ 1 ] Mudar a cor para a padrão *(gratis)*\n'
                               '[ 2 ] Mudar de cor por 10000 *fenicoins* \n'
                               '[ 3 ] Cancelar**')

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg25 = await bot.wait_for('message', timeout=1000.0, check=check)
    except asyncio.TimeoutError:
        return await ctx.channel.send(
            '***Demorou De Mais Para Aceitar.***')
    else:
        resposta25 = str(msg25.content).lower()

    if resposta25 == '1':
        pessoa = ctx.author.id

        sqlinsert = f"UPDATE dinheiro SET cor = '000000' WHERE id = {pessoa}"

        cursor.execute(sqlinsert)

        mydb.commit()

        await ctx.channel.send(embed=discord.Embed(title=':white_check_mark:  Cor alterada com sucesso!',
                                                   color=0x00FF00))

    elif resposta25 == '2':
        await msg25.delete()
        await a.delete()
        if valores_lidos2[0] >= 10000:

            a = await ctx.channel.send('**Qual cor você deseja?\n'
                                       '[ 1 ] Vinho\n'
                                       '[ 2 ] Verde escuro\n'
                                       '[ 3 ] Azul escuro **')

            def check(m):
                return m.author == ctx.author and m.channel == ctx.channel

            try:
                msg26 = await bot.wait_for('message', timeout=1000.0, check=check)
            except asyncio.TimeoutError:
                return await ctx.channel.send(
                    '***Demorou De Mais Para Aceitar.***')
            else:
                resposta26 = str(msg26.content).lower()

            if resposta26 == '3':
                sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - 10000}' WHERE id = {ctx.author.id}"

                cursor.execute(sqlinsert)

                mydb.commit()

                pessoa = ctx.author.id

                sqlinsert = f"UPDATE dinheiro SET cor = '000080' WHERE id = {pessoa}"

                cursor.execute(sqlinsert)

                mydb.commit()

                await ctx.channel.send(embed=discord.Embed(title=':white_check_mark:  Cor alterada com sucesso!',
                                                           color=0x00FF00))

                sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - 10000}' WHERE id = {ctx.author.id}"

                cursor.execute(sqlinsert)

                mydb.commit()
            elif resposta26 == '2':
                pessoa = ctx.author.id

                sqlinsert = f"UPDATE dinheiro SET cor = '800000' WHERE id = {pessoa}"

                cursor.execute(sqlinsert)

                mydb.commit()

                await ctx.channel.send(embed=discord.Embed(title=':white_check_mark:  Cor alterada com sucesso!',
                                                           color=0x00FF00))

                sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - 10000}' WHERE id = {ctx.author.id}"

                cursor.execute(sqlinsert)

                mydb.commit()

            elif resposta26 == '1':
                pessoa = ctx.author.id

                sqlinsert = f"UPDATE dinheiro SET cor = '000080' WHERE id = {pessoa}"

                cursor.execute(sqlinsert)

                mydb.commit()

                await ctx.channel.send(embed=discord.Embed(title=':white_check_mark:  Cor alterada com sucesso!',
                                                           color=0x00FF00))

                sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - 10000}' WHERE id = {ctx.author.id}"

                cursor.execute(sqlinsert)

                mydb.commit()
        else:
            await ctx.channel.send(
                f'<:error:788824695184424980> Olá {ctx.author.mention}, Você não possui **saldo suficiente** para a compra!')

    else:
        await ctx.channel.send(
            f'**<:error:788824695184424980> Olá {ctx.author.mention}, a sua alteração de cor foi cancelada**')



async def Roubar(ctx, member: discord.Member = None):
    pessoa = ctx.author.id
    if not member:
        await ctx.channel.send('<:error:788824695184424980> **Mencione quem você deseja roubar**')
        ctx.command.reset_cooldown(ctx)
        return

    membro = member.id
    sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert2)

    valores_lidos2 = cursor.fetchone()

    sqlinsert3 = f'SELECT dinheiro FROM dinheiro WHERE id = {membro}'

    cursor.execute(sqlinsert3)

    valores_lidos3 = cursor.fetchone()

    sqlinsert4 = f'SELECT arma FROM dinheiro WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert4)

    valores_lidos4 = cursor.fetchone()
    print(valores_lidos4)
    if ctx.author.id == member.id:

        await ctx.channel.send(embed=discord.Embed(title='<:error:788824695184424980> Você não pode roubar si mesmo!',
                                                   color=0xFF0000))
        ctx.command.reset_cooldown(ctx)
        return
    else:
        a = await ctx.channel.send(
            embed=discord.Embed(title=f'<a:loading:785523240944664646> Você está tentando roubar {member}',
                                color=0xFF6347))
        await asyncio.sleep(4)
        num = random.randint(-5000, 6500)
        if num > 0:
            try:
                if valores_lidos3[0] >= 7000:
                    if valores_lidos2[0] >= 7000:

                        if 0 < valores_lidos4[0] <= 7:

                            sqlinsert = f"UPDATE dinheiro SET arma = '{valores_lidos4[0] - 1}' WHERE id = {pessoa}"

                            cursor.execute(sqlinsert)

                            mydb.commit()

                        else:
                            await a.edit(
                                embed=discord.Embed(title='<:error:788824695184424980> Você não possui uma arma',
                                                    color=0xFF0000))
                            ctx.command.reset_cooldown(ctx)
                            return

                        sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] + num}' WHERE id = {pessoa}"

                        cursor.execute(sqlinsert)

                        mydb.commit()

                        sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos3[0] - num}' WHERE id = {member.id}"

                        cursor.execute(sqlinsert)

                        mydb.commit()

                        await a.edit(embed=discord.Embed(
                            title=f':white_check_mark: Você roubou {num} *fenicoins* do(a) {member}',
                            color=0x00FF00))
                        await member.send(
                            f'Ou, parecer que o `{ctx.author}` acabou de roubar você **`{num} fenicoins`**. **Eu não deixaria sair barato!!**')
                        await asyncio.sleep(2)
                        if valores_lidos4[0] == 1:
                            await ctx.channel.send(
                                embed=discord.Embed(title=f'Após roubar {member.name}, a sua arma quebra! ***track***',
                                                    color=0xFF0000))
                    else:
                        await a.edit(embed=discord.Embed(
                            title=f'**<:error:788824695184424980> Para poder roubar, você {ctx.author.name} precisa de no mínimo 7000 *fenicoins* **',
                            color=0xFF0000))
                        ctx.command.reset_cooldown(ctx)
                        return
                else:
                    await a.edit(embed=discord.Embed(
                        title=f'**<:error:788824695184424980> Olá {ctx.author.name}, eu estou protegendo o(a) {member.name} até ele(a) conseguir 7000 *fenicoins* **',
                        color=0xFF0000))
                    ctx.command.reset_cooldown(ctx)
                    return
            except:
                await a.edit(embed=discord.Embed(
                    title=f'<:error:788824695184424980> ** Ocorreu um erro ao tentar roubar o(a) {member.name}**',
                    color=0xFF0000))
                ctx.command.reset_cooldown(ctx)
                return

        elif num <= 0:
            try:
                if valores_lidos3[0] >= 7000:
                    if valores_lidos2[0] >= 7000:
                        if 0 < valores_lidos4[0] <= 7:

                            sqlinsert = f"UPDATE dinheiro SET arma = '{valores_lidos4[0] - 1}' WHERE id = {pessoa}"

                            cursor.execute(sqlinsert)

                            mydb.commit()

                        else:
                            await a.edit(
                                embed=discord.Embed(title='<:error:788824695184424980> Você não possui uma arma',
                                                    color=0xFF0000))

                            ctx.command.reset_cooldown(ctx)

                            return
                        sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] + num}' WHERE id = {ctx.author.id}"

                        cursor.execute(sqlinsert)

                        mydb.commit()

                        await a.edit(embed=discord.Embed(
                            title=f'<:error:788824695184424980> Um policial te deu uma multa de {num} *fenicoins* por tentar roubar {member.name}',
                            color=0xFF0000
                            ))
                        await member.send(
                            f'Ou, parecer que o `{ctx.author}` acabou de tentar roubar você e perdeu **`{num} fenicoins`**. **Eu não deixaria sair barato!!**')
                        await asyncio.sleep(2)
                        if valores_lidos4[0] == 1:
                            await ctx.channel.send(embed=discord.Embed(
                                title=f'Após tentar roubar {member.name}, a sua arma quebra! ***track***',
                                color=0xFF0000))

                    else:
                        await a.edit(embed=discord.Embed(
                            title=f'**<:error:788824695184424980> Para poder roubar, você {ctx.author.name} precisa de no mínimo 7000 *fenicoins* **',
                            color=0xFF0000))
                        ctx.command.reset_cooldown(ctx)
                        return

                else:
                    await a.edit(embed=discord.Embed(
                        title=f'**<:error:788824695184424980> Olá {ctx.author.name}, eu estou protegendo o(a) {member.name} até ele(a) conseguir 7000 *fenicoins* **',
                        color=0xFF0000))
                    ctx.command.reset_cooldown(ctx)
            except:
                await a.edit(embed=discord.Embed(
                    title=f'<:error:788824695184424980> ** Ocorreu um erro ao tentar roubar o(a) {member.name}**',
                    color=0xFF0000))
                ctx.command.reset_cooldown(ctx)
                return


async def Arma(ctx):
    sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert2)

    valores_lidos2 = cursor.fetchone()

    sqlinsert4 = f'SELECT arma FROM dinheiro WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert4)

    valores_lidos4 = cursor.fetchone()

    try:
        print(valores_lidos2[0])
    except:
        await ctx.channel.send(
            embed=discord.Embed(title='<:error:788824695184424980> **Você não possui uma conta no fênix!!**',
                                color=0xFF0000))
        return

    a = await ctx.channel.send('**Oque você deseja?\n'
                               '[ 1 ] Ver Arma \n'
                               '[ 2 ] Comprar Arma\n'
                               '[ 3 ] Cancelar**')

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        msg25 = await bot.wait_for('message', timeout=1000.0, check=check)
    except asyncio.TimeoutError:
        return await ctx.channel.send(
            f'***Demorou De Mais Para Escolher {ctx.author.mention}.***')
    else:
        resposta25 = str(msg25.content)

    if resposta25[0] == '1':
        if valores_lidos4[0] == -1 or valores_lidos4[0] == 0:
            await ctx.channel.send(embed=discord.Embed(title='<:error:788824695184424980> **Você não possui uma arma**',
                                                       color=0xFF0000))
            return
        embed12 = discord.Embed(title=f'Você possui uma arma com ***{valores_lidos4[0]}*** de resistência',
                                color=0x8A2BE2)
        await ctx.send(embed=embed12)
        return
    if resposta25[0] == '2':
        embed = discord.Embed(title='Arma 1',
                              description='Estatística : 3 de resistência\n'
                                          'Valor : **5000 *fenicoins* **',
                              color=0xFF00FF)
        embed1 = discord.Embed(title='Arma 2',
                               description='Estatística : 5 de resistência\n'
                                           'Valor : **7000 *fenicoins* **',
                               color=0xFF00FF)
        embed2 = discord.Embed(title='Arma 3',
                               description='Estatística : 7 de resistência\n'
                                           'Valor : **9000 *fenicoins* **',
                               color=0xFF00FF)
        embed2.set_image(
            url='https://media.discordapp.net/attachments/788064370722340885/788170522134970429/kisspng-38-special-revolver-firearm-pistol-smith-wesson-5b0b15088c94c1.png')
        embed1.set_image(
            url='https://media.discordapp.net/attachments/788064370722340885/788170572033949696/5bc0eaf503b8e-a0a4375043583f46cdac42d2f6e2d1c7.png')
        embed.set_image(
            url='https://media.discordapp.net/attachments/788064370722340885/788170539964694528/1607959158347.png')
        try:
            b = await ctx.author.send(embed=embed)
            await asyncio.sleep(1)
            c = await ctx.author.send(embed=embed1)
            await asyncio.sleep(1)
            d = await ctx.author.send(embed=embed2)
            await asyncio.sleep(1)
            await ctx.channel.send(':calling: **Enviei as informações das armas que você pode comprar no seu DM!!**')
        except:
            await ctx.channel.send(
                '<:error:788824695184424980> Ops parece que seu DM está bloqueado. Para dar esse comando você precisa desbloquear.')
            return
        await asyncio.sleep(2)
        await ctx.send('**Qual das armas enviadas no seu DM você deseja?** ***ex:*** 1, 2, 3 ou cancelar')
        await a.delete()
        await msg25.delete()

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            msg25 = await bot.wait_for('message', timeout=1000.0, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send(
                f'***Demorou De Mais Para Escolher {ctx.author.mention}.***')
        else:
            resposta27 = str(msg25.content).lower()

        if resposta27 == 'arma 1' or resposta27 == '1' and valores_lidos2[0] >= 5000:
            sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - 5000}' WHERE id = {ctx.author.id}"

            cursor.execute(sqlinsert)

            mydb.commit()

            sqlinsert = f"UPDATE dinheiro SET arma = '{3}' WHERE id = {ctx.author.id}"

            cursor.execute(sqlinsert)

            mydb.commit()
            await ctx.channel.send(':white_check_mark: **Arma comprada com sucesso**')
        elif resposta27 == 'arma 2' or resposta27 == '2' and valores_lidos2[0] >= 7000:
            sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - 7000}' WHERE id = {ctx.author.id}"

            cursor.execute(sqlinsert)

            mydb.commit()

            sqlinsert = f"UPDATE dinheiro SET arma = '{5}' WHERE id = {ctx.author.id}"

            cursor.execute(sqlinsert)

            mydb.commit()
            await ctx.channel.send(':white_check_mark: **Arma comprada com sucesso**')
        elif resposta27 == 'arma 3' or resposta27 == '3' and valores_lidos2[0] >= 9000:
            sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - 9000}' WHERE id = {ctx.author.id}"

            cursor.execute(sqlinsert)

            mydb.commit()

            sqlinsert = f"UPDATE dinheiro SET arma = '{7}' WHERE id = {ctx.author.id}"

            cursor.execute(sqlinsert)

            mydb.commit()
            await ctx.channel.send(':white_check_mark: **Arma comprada com sucesso**')
        elif resposta27 == 'cancelar' or resposta27 == 'cancel':
            await ctx.channel.send(embed=discord.Embed(title='<:error:788824695184424980> Compra Cancelada',
                                                       color=0xFF0000))
        else:
            await ctx.channel.send(embed=discord.Embed(
                title=f'<:error:788824695184424980> Olá {ctx.author.name}, Você não possui **saldo suficiente** para a compra!',

                color=0xFF0000))
    else:
        await ctx.channel.send(f'**<:error:788824695184424980> Olá {ctx.author.mention}, a sua escolha foi cancelada**')
    await b.delete()
    await c.delete()
    await d.delete()



async def Fenicoins(ctx, member: discord.Member = None):
    sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert2)

    valores_lidos2 = cursor.fetchone()

    sqlinsert4 = f'select id from dinheiro ORDER BY dinheiro desc'

    cursor.execute(sqlinsert4)

    valores_lidos4 = cursor.fetchall()

    pessoa = ctx.author.id

    await ctx.message.delete()

    if not member:
        try:
            print(valores_lidos2[0])
        except:
            await ctx.channel.send(embed=discord.Embed(
                title='<:error:788824695184424980> ** Você não possui uma conta no fênix!!**',
                color=0xFF0000))
            return

        for index, element in enumerate(valores_lidos4):
            if element[0] == pessoa:
                num1 = index + 1
                break

        coin = (
            f'<:fenix:787131059669303358>| Olá {ctx.author.mention} parece que você possui **{valores_lidos2[0]} fenicoins** e está em **#{num1} lugar** no ranking!')
        await ctx.channel.send(coin)
    else:
        membro = member.id
        for index, element in enumerate(valores_lidos4):
            if element[0] == membro:
                num2 = index + 1
                break
        sqlinsert3 = f'SELECT dinheiro FROM dinheiro WHERE id = {member.id}'

        cursor.execute(sqlinsert3)

        valores_lidos3 = cursor.fetchone()

        try:
            print(valores_lidos3[0])
        except:
            await ctx.channel.send(embed=discord.Embed(
                title='<:error:788824695184424980> ** Esse usuário não possui uma conta no fênix!!**',
                color=0xFF0000))
            return

        coin = (
            f'<:fenix:787131059669303358>| Olá {ctx.author.mention} parece que o(a) {member.mention} possui **{valores_lidos3[0]} fenicoins** e está em **#{num2} lugar**!')
        await ctx.channel.send(coin)

