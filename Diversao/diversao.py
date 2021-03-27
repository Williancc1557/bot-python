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

color = 0x0000FF


async def Coinflip(ctx, bet: str = None):
    if not bet:
        choice = random.randint(1, 2)
        await ctx.message.delete()
        if choice == 1:
            await ctx.channel.send(f'{ctx.author.mention} Deu Cara 🙂')
        if choice == 2:
            await ctx.channel.send(f'{ctx.author.mention} Deu Coroa :crown:')



async def Desafiar(ctx, unit=None):
    cursor.execute("ROLLBACK")
    if unit == 'fenix' or unit == 'fênix' or unit[0].lower == 'f':
        sqlinsert = f'SELECT desafiar FROM block WHERE servid = {ctx.author.guild.id}'

        cursor.execute(sqlinsert)

        valores_lidos = cursor.fetchone()

        try:
            print(valores_lidos[0])

            await ctx.channel.send(
                '<:error:788824695184424980> Esse comando foi **desativado** pela equipe do servidor!!')
            return ctx.command.reset_cooldown(ctx)
        except:
            pass

        confirm = discord.Embed(title='**Você Realmente Deseja Desafiar O Fênix?**', color=color,
                                description='\nCuidado: Não de + de 1 Resposta!!\n\nPara desativar esse comando use `f!desafiar lock`\n\n***Escreva: Sim ou Não***\n\n**Atualizações:**\nPequenas correções\nDesafio 1 atualizado \n\n**Avalie o bot utilizando o comando** : `f!avaliar` ')
        confirm.set_image(
            url='https://media.discordapp.net/attachments/774002343816593409/779146240977535026/fenix.jpg')
        await ctx.channel.send(embed=confirm)

        def check(p):
            return p.author == ctx.author and p.channel == ctx.channel

        try:
            msg = await bot.wait_for('message', timeout=40, check=check)
        except asyncio.TimeoutError:
            return await ctx.channel.send('**Acabou O Tempo Para Aceitar**')
        else:
            aceitar = str(msg.content).lower().strip()

        if aceitar == 'sim':

            computador = int(random.randint(0, 2))
            lista = ('pedra', 'papel', 'tesoura')

            await ctx.channel.send('**Como Ousa Me Desafiar Mero Humano. Irei te propor 5 Desafios, Você aceita?**\n ')

            embed = discord.Embed(color=0x000000)
            embed.set_image(
                url='https://cdn.discordapp.com/attachments/774002343816593409/779817984041549844/unnamed_1.gif')

            embed2 = discord.Embed(color=0x000000)

            await ctx.channel.send(embed=embed)

            embed4 = discord.Embed(color=0x00a000,
                                   title='{}\n ''**Vida do Fênix: 100%**\n ''{}'.format('-=-' * 10, '-=-' * 10))
            await ctx.channel.send(embed=embed4)

            await ctx.channel.send('**Tem 20 segundos para aceitar. Seu Mortal Inutil**\n Digite: Sim ou Não')

            embed2.set_image(
                url='https://media.discordapp.net/attachments/778295088753016903/785845554756321300/InShot_20201122_065408869.gif?width=473&height=473')

            def check(p):
                return p.author == ctx.author and p.channel == ctx.channel

            try:
                msg1 = await bot.wait_for('message', timeout=20, check=check)
            except asyncio.TimeoutError:
                return await ctx.channel.send('**Acabou O Tempo, Vaza Daqui Seu Humano Fraco**')
            else:
                numero = str(msg1.content).lower().strip()

            if numero == 'sim':
                await ctx.channel.send('**Aceitou? Mais Que Humano Ousado.**')
                await asyncio.sleep(2)
                await ctx.channel.send(
                    '**Primeiro Desafio: Jogue pedra, papel ou tesoura com o Fênix:**\n'
                    '**[ 0 ] PEDRA\n'
                    '[ 1 ] PAPEL\n'
                    '[ 2 ] TESOURA\n**')

                def check(m):
                    return m.author == ctx.author and m.channel == ctx.channel

                try:
                    msg = await bot.wait_for('message', timeout=30.0, check=check)
                except asyncio.TimeoutError:
                    return await ctx.channel.send('***Acabou o Tempo, Fênix Te Mata Ao Perder A Paciência***',
                                                  embed=embed2)
                else:
                    jogador = int(msg.content)
                await ctx.channel.send(
                    '{}\n**O HUMANO escolheu** ***{}***\n**O fênix escolheu** ***{}***\n{}'.format('-=' * 11,
                                                                                                   lista[jogador],
                                                                                                   lista[computador],
                                                                                                   '-=' * 11))
                await asyncio.sleep(2)
                if computador == 0:
                    if jogador == 0:
                        await ctx.channel.send('***Você EMPATOU***')
                        await asyncio.sleep(2)
                        await ctx.channel.send('**Humano Sortudo**')
                        await asyncio.sleep(2)
                        await ctx.channel.send('**Nenhum  H U M A N O  Nunca Conseguiu Empatar Comigo**')
                        await asyncio.sleep(2.5)
                        await ctx.channel.send('**Irei Considerar Como Vitória Por Pena De Você**')

                    elif jogador == 1:
                        await ctx.channel.send('**Você GANHOU**')
                        await asyncio.sleep(2)
                        a = await ctx.channel.send('**.**')
                        await asyncio.sleep(1)
                        await a.edit(content='**.  .**')
                        await asyncio.sleep(1)
                        await a.edit(content='**.  .  .**')
                    elif jogador == 2:
                        await ctx.channel.send('**Você PERDEU**')

                if computador == 1:
                    if jogador == 0:
                        await ctx.channel.send('**Você PERDEU**')

                    elif jogador == 1:
                        await ctx.channel.send('**Você EMPATOU**')
                        await asyncio.sleep(2)
                        await ctx.channel.send('**Humano Sortudo**')
                        await asyncio.sleep(2)
                        await ctx.channel.send('**Nenhum  H U M A N O  Nunca Conseguiu Empatar Comigo**')
                        await asyncio.sleep(2.5)
                        await ctx.channel.send('**Irei Considerar Como Vitória Por Pena De Você**')

                    elif jogador == 2:
                        await ctx.channel.send('**Você GANHOU**')
                        await asyncio.sleep(2)
                        a = await ctx.channel.send('**.**')
                        await asyncio.sleep(1)
                        await a.edit(content='**.  .**')
                        await asyncio.sleep(1)
                        await a.edit(content='**.  .  .**')

                if computador == 2:
                    if jogador == 0:
                        await ctx.channel.send('**Você GANHOU**')
                        await asyncio.sleep(2)
                        a = await ctx.channel.send('**.**')
                        await asyncio.sleep(1)
                        await a.edit(content='**.  .**')
                        await asyncio.sleep(1)
                        await a.edit(content='**.  .  .**')

                    elif jogador == 1:
                        await ctx.channel.send('**Você PERDEU**')

                    elif jogador == 2:
                        await ctx.channel.send('**Você EMPATOU**')
                        await asyncio.sleep(2)
                        await ctx.channel.send('**Humano Sortudo**')
                        await asyncio.sleep(2)
                        await ctx.channel.send('**Nenhum  H U M A N O  Nunca Conseguiu Empatar Comigo**')
                        await asyncio.sleep(2.5)
                        await ctx.channel.send('**Irei Considerar Como Vitória Por Pena De Você**')
                        await asyncio.sleep(3)
                if computador == 0 and jogador == 0 or computador == 0 and jogador == 1 or computador == 1 and jogador == 1 or computador == 1 and jogador == 2 or computador == 2 and jogador == 0 or computador == 2 and jogador == 2:
                    embed3 = discord.Embed(color=0xFFFF00,
                                           title='{}\n ''**Vida do Fênix: 80%**\n ''{}'.format('-=-' * 10, '-=-' * 10))
                    await asyncio.sleep(2)
                    await ctx.channel.send('**Provavelmente Foi Sorte**')
                    await asyncio.sleep(1.5)
                    await ctx.channel.send('**Mais Que Seja, Não Irei Mais Pegar Leve**')
                    await asyncio.sleep(1)
                    await ctx.channel.send(embed=embed)
                    await ctx.channel.send(embed=embed3)
                    await asyncio.sleep(2)
                    n1 = random.randint(3, 9)
                    n2 = random.randint(2, 10)
                    n3 = random.randint(1, 10)
                    r = (n1 * n2) + n3
                    await ctx.channel.send(
                        f'**Segundo Desafio : Resolva Essa Conta **\n\n**{n1} . {n2} + {n3}**\n\nColoque a penas a alternativa, Você Tem 60 SEGUNDOS.')

                    def check(m):
                        return m.author == ctx.author and m.channel == ctx.channel

                    try:
                        msg2 = await bot.wait_for('message', timeout=60.0, check=check)
                    except asyncio.TimeoutError:
                        return await ctx.channel.send('***Acabou o Tempo, Fênix Te Mata Ao Perder A Paciência***',
                                                      embed=embed2)
                    else:
                        numero1 = int(msg2.content)

                    if numero1 == r:
                        await ctx.channel.send('**Ops, Acabei Errando Os Numeros :smiling_imp:**')
                        await asyncio.sleep(1)
                        await ctx.channel.send(embed=embed)
                        await asyncio.sleep(2)
                        await ctx.channel.send('**Na Verdade Era Pra Ser:**')
                        await asyncio.sleep(1.5)
                        n4 = random.randint(10, 100)
                        n5 = random.randint(30, 400)
                        n6 = random.randint(50, 200)
                        r2 = n4 + n5 - n6
                        await ctx.channel.send(
                            f'**Segundo Desafio Novamete: Resolva Essa Conta**\nTem 60 segundos para resolver!!\n\n **x = {n4} + {n5} - {n6}**')

                        def check(m):
                            return m.author == ctx.author and m.channel == ctx.channel

                        try:
                            msg3 = await bot.wait_for('message', timeout=60.0, check=check)
                        except asyncio.TimeoutError:
                            return await ctx.channel.send('***Acabou o Tempo, Fênix Te Mata Ao Perder A Paciência***',
                                                          embed=embed2)
                        else:
                            numero3 = int(msg3.content)

                            if numero3 == r2:
                                await ctx.channel.send('**Não acredito!**')
                                await asyncio.sleep(2)
                                await ctx.channel.send(
                                    '**NÃO SEREI DERROTADO POR UM H U M A N O, ACEITE SEU DESTINO E MORRA**')
                                await asyncio.sleep(3)
                                sangrando = discord.Embed(cor=0x000000)
                                vida = discord.Embed(color=0xFFFF00,
                                                     title='{}\n ''**Vida do Fênix: 60%**\n ''{}'.format('-=-' * 10,
                                                                                                         '-=-' * 10))
                                sangrando.set_image(
                                    url='https://media1.tenor.com/images/30639e64f026da268942ac99f3cd6db6/tenor.gif?itemid=12883093')
                                await ctx.channel.send(embed=sangrando)
                                await ctx.channel.send(embed=vida)
                                await asyncio.sleep(3)
                                await ctx.channel.send(
                                    '**Terceiro desafio: O Que De Noite Tem Cabeça E De Dia Não Tem?**\n\n:man_detective:| tem 60 segundos para resolver a charada . . .\nObs: Escreva Apenas A Resposta, Nada A Mais!! ')
                                try:
                                    msg4 = await bot.wait_for('message', timeout=60.0, check=check)
                                except asyncio.TimeoutError:
                                    return await ctx.channel.send(
                                        '***Acabou o Tempo, Fênix Te Mata Ao Perder A Paciência***', embed=embed2)
                                else:
                                    numero4 = msg4.content.lower()

                                if numero4 == 'travesseiro':
                                    await ctx.channel.send('**Errou**')
                                    await asyncio.sleep(3)
                                    await ctx.channel.send('**A Resposta Correta Seria A Bunda Da Sua . . .**')
                                    await asyncio.sleep(3)
                                    await ctx.channel.send('**Da Suaa. . .** ')
                                    await asyncio.sleep(3)
                                    await ctx.channel.send(
                                        '**Af, Deixa Queto, Essa Piada É Do Nivel Da Classe Humana**')
                                    await asyncio.sleep(1.5)
                                    embed5 = discord.Embed(color=0x000000)
                                    embed5.set_image(
                                        url='https://images-ext-1.discordapp.net/external/mODJ6ndO1zWtpYd0K6ThHhNxKXvnk8gzs2dL_h8sdvw/https/media.discordapp.net/attachments/776911405730889769/780106010974617600/SanPistola.gif')
                                    vida2 = discord.Embed(color=0xFFFF00,
                                                          title='{}\n ''**Vida do Fênix: 40%**\n ''{}'.format(
                                                              '-=-' * 10,
                                                              '-=-' * 10))
                                    await ctx.channel.send(embed=embed5)
                                    await ctx.channel.send(embed=vida2)
                                    await ctx.channel.send(
                                        f'**Parabéns Humano {ctx.author.mention} Por Me Irritar, Agora Sofra As Consequências**')
                                    await asyncio.sleep(2)
                                    await ctx.channel.send(
                                        'Escolha Oque deseja falar:\n**[ A ]**  Como Você Sabe O Meu Nome?\n**[ B ]**  Fênix Seu Fraco\n\nObs: Escreva Apenas Uma Letra.')

                                    def check(m):
                                        return m.author == ctx.author and m.channel == ctx.channel

                                    try:
                                        msg5 = await bot.wait_for('message', timeout=120.0, check=check)
                                    except asyncio.TimeoutError:
                                        return await ctx.channel.send(
                                            '***Demorou De Mais Para Escolher.***', embed=embed2)
                                    else:
                                        resposta1 = str(msg5.content).lower()

                                    if resposta1 == 'a':
                                        await asyncio.sleep(1)
                                        await ctx.channel.send(
                                            '**Por Que Eu Hackeei Todas As Suas Contas Bancarias Nesse Exato Momento.**')
                                        await asyncio.sleep(3)
                                        await ctx.channel.send('**Que Humano Mais Burro**')
                                        await ctx.channel.send(
                                            '<a:Top:815388123039006741>Você Ganhou Uma Conquista, Olhe Seu Privado<a:Top:815388123039006741>')
                                        conquista1 = discord.Embed(
                                            title='<a:Top:815388123039006741> Conquista <a:Top:815388123039006741>',
                                            color=color,
                                            description=f'**Parabéns Esse É O Seu Certificado Para Confimar A Sua Conquista {ctx.author.mention} **\n\n\n***Nome: HUMANO BURRO***\n\n**O Que Eu Posso Fazer Com Esse Certificado?**\nVocê Ganha O Cargo O DESAFIADOR\n\nObs: Se O Cargo Não Apareceu Significa Que O Server Não Possui A Tag Com O Nome  HUMANO BURRO  !')
                                        await ctx.author.send(embed=conquista1)
                                        role = discord.utils.find(lambda r: r.name == "HUMANO BURRO", ctx.guild.roles)
                                        await ctx.author.add_roles(role)
                                    if resposta1 == 'b':
                                        await asyncio.sleep(1)
                                        await ctx.channel.send(
                                            '**Não Acredito Que Você Me Chamou De Fraco, SEU HUMANO INSIGNIFICANTE!**')
                                        await asyncio.sleep(3)
                                        await ctx.channel.send(
                                            '<a:Top:815388123039006741> Você Ganhou Uma Conquista, Olhe Seu Privado <a:Top:815388123039006741>')
                                        conquista = discord.Embed(
                                            title='<a:Top:815388123039006741> Conquista <a:Top:815388123039006741>',
                                            color=color,
                                            description=f'**Parabéns Esse É O Seu Certificado Para Confimar A Sua Conquista {ctx.author.mention} **\n\n\n***Nome: O DESAFIADOR***\n\n**O Que Eu Posso Fazer Com Esse Certificado?**\nVocê Ganha O Cargo O DESAFIADOR\n\nObs: Se O Cargo Não Apareceu Significa Que O Server Não Possui A Tag Com O Nome  O DESAFIADOR  !')
                                        await ctx.author.send(embed=conquista)
                                        role = discord.utils.find(lambda r: r.name == "O DESAFIADOR", ctx.guild.roles)
                                        await ctx.author.add_roles(role)

                                    if resposta1 == 'b' or resposta1 == 'a':
                                        puto = discord.Embed(color=0x000000)
                                        puto.set_image(
                                            url='https://media.discordapp.net/attachments/776911405730889769/780416711152369674/SanPistola.gif')
                                        await asyncio.sleep(3)
                                        await ctx.channel.send('**Irei Te Destruir Humano**')
                                        await asyncio.sleep(3)
                                        await ctx.channel.send('**Quarto Desafio: Qual O Nome Do Criador Do Fênix?**')

                                        def check(m):
                                            return m.author == ctx.author and m.channel == ctx.channel

                                        try:
                                            msg6 = await bot.wait_for('message', timeout=120.0, check=check)
                                        except asyncio.TimeoutError:
                                            return await ctx.channel.send(
                                                '***Demorou De Mais Para Responder.***', embed=embed2)
                                        else:
                                            resposta2 = str(msg6.content).lower()

                                            if resposta2 == 'will':
                                                await ctx.channel.send(embed=puto)
                                                vida4 = discord.Embed(color=0xFF0000,
                                                                      title='{}\n ''**Vida do Fênix: 20%**\n ''{}'.format(
                                                                          '-=-' * 10, '-=-' * 10))
                                                await ctx.channel.send(embed=vida4)

                                                await ctx.channel.send('**AAAHH Quem Não Sabe O Nome Desse Moleque**\n')
                                                await asyncio.sleep(3)
                                                await ctx.channel.send('**WiLL:** hehe Sou famoso :)\n')
                                                await asyncio.sleep(3)
                                                await ctx.channel.send('**Vaza Daqui WiLL\n**')
                                                await asyncio.sleep(3)
                                                await ctx.channel.send('**WiLL:** Respeite O Seu Criador\n')
                                                await asyncio.sleep(3)
                                                await ctx.channel.send('**Você É Um Merda WiLL\n**')
                                                await asyncio.sleep(3)
                                                await ctx.channel.send('**WiLL:** ;-;\n')
                                                await asyncio.sleep(4)
                                                await ctx.channel.send(
                                                    f'**H U M A N O {ctx.author.mention} EU NUNCA IREI TE PERDOAR POR CHEGAR TÃO LONGE NO MEU DESAFIO**')
                                                await asyncio.sleep(3)
                                                b = await ctx.channel.send('**Ultimo Desafio: .**')
                                                await asyncio.sleep(1)
                                                await b.edit(content='**Ultimo Desafio: . .**')
                                                await asyncio.sleep(1)
                                                await b.edit(content='**Ultimo Desafio: . . .**')

                                                await asyncio.sleep(4)
                                                await ctx.channel.send('**NÃO EXISTE ULTIMO DESAFIO HAHAHA**')
                                                await asyncio.sleep(4)
                                                await ctx.channel.send(
                                                    '**Você Acha Que Eu Deixaria Algum H U M A N O Imundo Me Derrotar? ESTÁ MUITO ENGANADO HAHAHA**')
                                                await asyncio.sleep(4)
                                                await ctx.channel.send(
                                                    '**SystemCommand, Coloque A Minha Vida Em 100%**')
                                                await asyncio.sleep(4)
                                                await ctx.channel.send(embed=embed4)

                                                await asyncio.sleep(5)

                                                await ctx.channel.send(
                                                    '**[ A ]**  Fala Para O Fênix Que Ele É Apenas Um Robô\n**[ B ]**  Pedir Ajuda\n**[ C ]**  Desafiar O Fênix Novamente\n**[ D ]** : Se Render\n\nObs: Responda Apenas Colocando A Letra')

                                                def check(m):
                                                    return m.author == ctx.author and m.channel == ctx.channel

                                                try:
                                                    msg7 = await bot.wait_for('message', timeout=1000.0, check=check)
                                                except asyncio.TimeoutError:
                                                    return await ctx.channel.send(
                                                        '***Demorou De Mais Para Responder.***', embed=embed2)
                                                else:
                                                    resposta3 = str(msg7.content).lower()

                                                if resposta3 == 'a':
                                                    await ctx.channel.send(
                                                        f'{ctx.author.mention}: Fênix Você é Ape. . .')
                                                    await ctx.channel.send(
                                                        f'***MORRA H U M A N O {ctx.author.mention}***')
                                                    await ctx.channel.send(embed=embed2)

                                                if resposta3 == 'b':
                                                    await ctx.channel.send(
                                                        f'***MORRA H U M A N O {ctx.author.mention}***')
                                                    await asyncio.sleep(3)
                                                    await ctx.channel.send(
                                                        f'**{ctx.author.mention}:** SOCOOOOORRROOO!!')
                                                    await asyncio.sleep(2)
                                                    await ctx.channel.send('**WiLL:** O MIZERA EU TAVA DORMINDO')
                                                    await asyncio.sleep(2)
                                                    await ctx.channel.send(embed=embed2)
                                                    await asyncio.sleep(4)
                                                    await ctx.channel.send('**WiLL:** EITA, UM HUMANO CHEGOU ATÉ AQUI?')
                                                    await asyncio.sleep(3)
                                                    await ctx.channel.send(
                                                        f'**WiLL: SystemCommand REVIVER {ctx.author.mention}**')
                                                    await asyncio.sleep(4)
                                                    await ctx.channel.send(f'**{ctx.author.mention}: Opa**')
                                                    await asyncio.sleep(3)
                                                    await ctx.channel.send(
                                                        f'**WiLL:** Parabéns Você é o primeiro humano a ganhar o desafio do fênix, Agora Eu irei lhe retribuir com uma escolha')
                                                    await asyncio.sleep(4)
                                                    await ctx.channel.send(
                                                        '**WiLL:**Deseja que eu apague o Fênix Sim Ou Não?')

                                                    def check(m):
                                                        return m.author == ctx.author and m.channel == ctx.channel

                                                    try:
                                                        msg8 = await bot.wait_for('message', timeout=1000.0,
                                                                                  check=check)
                                                    except asyncio.TimeoutError:
                                                        return await ctx.channel.send(
                                                            '***Demorou De Mais Para Escolher.***', embed=embed2)
                                                    else:
                                                        resposta4 = str(msg8.content).lower()

                                                    if resposta4 == 'sim':
                                                        embed10 = discord.Embed(color=color)
                                                        embed10.set_image(
                                                            url='https://media1.tenor.com/images/7004e277fe6ffefaa3f6836c02a030c8/tenor.gif?itemid=7401069')
                                                        await ctx.channel.send(
                                                            '**Adeus, Hoje Eu Aprendi Que Humanos São Seres Sabios**')
                                                        await ctx.channel.send(embed=embed10)
                                                        await ctx.channel.send(
                                                            '<a:Top:815388123039006741>Você Ganhou Uma Conquista, Olhe Seu Privado<a:Top:815388123039006741>')
                                                        conquista2 = discord.Embed(
                                                            title='<a:Top:815388123039006741> Conquista <a:Top:815388123039006741>',
                                                            color=color,
                                                            description=f'**Parabéns Esse É O Seu Certificado Para Confimar A Sua Conquista {ctx.author.mention} **\n\n\n***Nome: O VINGADOR***\n\n**O Que Eu Posso Fazer Com Esse Certificado?**\nVocê Ganha O Cargo O Cargo O VINGADOR\n\nObs: Se O Cargo Não Apareceu Significa Que O Server Não Possui A Tag Com O Nome  O VINGADOR  !')
                                                        await ctx.author.send(embed=conquista2)

                                                        role = discord.utils.find(lambda r: r.name == "O VINGADOR",
                                                                                  ctx.guild.roles)
                                                        await ctx.author.add_roles(role)

                                                        await asyncio.sleep(3)
                                                        await ctx.channel.send(
                                                            '**Obrigado por jogar nosso joguin :), Avalie ele usando** `f!avaliar`')

                                                    if resposta4 == 'não':
                                                        await ctx.channel.send(
                                                            f'**Obrigado {ctx.author.mention} Por Poupar Minha Vida  :)**')
                                                        await ctx.channel.send(embed=embed)
                                                        await asyncio.sleep(2)
                                                        await ctx.channel.send('**Irei Lhe Dar Um Premio:**')
                                                        await ctx.channel.send(
                                                            '<a:Top:815388123039006741>Você Ganhou Uma Conquista, Olhe Seu Privado<a:z_Diamond_1555:778273709865173022>')
                                                        conquista2 = discord.Embed(
                                                            title='<a:Top:815388123039006741> Conquista <a:z_Diamond_1555:778273709865173022>',
                                                            color=color,
                                                            description=f'**Parabéns Esse É O Seu Certificado Para Confimar A Sua Conquista {ctx.author.mention} **\n\n\n***Nome: O SALVADOR***\n\n**O Que Eu Posso Fazer Com Esse Certificado?**\nVocê Ganha O Cargo O SALVADOR\n\nObs: Se O Cargo Não Apareceu Significa Que O Server Não Possui A Tag Com O Nome  O SALVADOR  !')
                                                        await ctx.author.send(embed=conquista2)
                                                        role = discord.utils.find(lambda r: r.name == "O SALVADOR",
                                                                                  ctx.guild.roles)
                                                        await ctx.author.add_roles(role)
                                                        await asyncio.sleep(2)
                                                        await ctx.channel.send(
                                                            '**Obrigado por jogar nosso joguin :), Avalie ele usando** `f!avaliar`')

                                                        await asyncio.sleep(3)

                                                        await ctx.author.send(
                                                            '**Obrigado Por Jogar Nosso Joguinho**\n\nAss: WiLL :)')

                                                if resposta3 == 'c':
                                                    await ctx.channel.send(
                                                        '**Você Vai Querer Mesmo Me desafiar Novamente? OK H U M A N O TOLO**')
                                                    await asyncio.sleep(3)
                                                    await ctx.channel.send('O Ultimo Do Ultimo Desafio:')
                                                    await asyncio.sleep(4)
                                                    num = str(random.randint(100000, 1000000000))
                                                    await ctx.channel.send(
                                                        f'**RESOLVA ESSA EQUAÇÃO: {num} . 7215353423283 + 212445332**\n\n **Não está dificil eu confio em você humano**\n\nTem 10 segundos para responder')

                                                    def check(m):
                                                        return m.author == ctx.author and m.channel == ctx.channel

                                                    try:
                                                        msg11 = await bot.wait_for('message', timeout=10.0, check=check)
                                                    except asyncio.TimeoutError:
                                                        return await ctx.channel.send(
                                                            '***Demorou De Mais Para Responder.***', embed=embed2)



                                                    else:
                                                        resposta5 = str(msg11.content).lower()

                                                    if resposta5 == 13143262354345:
                                                        await ctx.channel.send('. . .')

                                                    else:
                                                        await ctx.channel.send(f'***Errou***', embed=embed2)

                                                if resposta3 == 'd':
                                                    await ctx.channel.send('**HAHAHA COMO FOI FACIL**')
                                                    await asyncio.sleep(3)
                                                    await ctx.channel.send(
                                                        '**Quais São As Suas Ultimas palavras humano?**')
                                                    await asyncio.sleep(2)
                                                    await ctx.channel.send('**A** = Não me mate pfv fênix\n'
                                                                           '**B** = Fênix Você Sempre Um Será Fraco\n'
                                                                           '**C** = Você é muito FORTE F E N I X')

                                                    def check(m):
                                                        return m.author == ctx.author and m.channel == ctx.channel

                                                    try:
                                                        msg20 = await bot.wait_for('message', timeout=1000.0,
                                                                                   check=check)
                                                    except asyncio.TimeoutError:
                                                        return await ctx.channel.send(
                                                            '***Demorou De Mais Para Escolher.***', embed=embed2)
                                                    else:
                                                        resposta20 = str(msg20.content).lower()

                                                    if resposta20 == 'a':
                                                        await ctx.channel.send('**MORRA H U M A N O')
                                                        await asyncio.sleep(3)
                                                        await ctx.channel.send('***Fênix te mata***', embed=embed2)

                                                    elif resposta20 == 'b':
                                                        await ctx.channel.send('**EU NÃO SOU FRACO**')
                                                        await asyncio.sleep(3)
                                                        await ctx.channel.send('MORRA SEU MIZERAVEL!!0')
                                                        await asyncio.sleep(2)
                                                        await ctx.channel.send(
                                                            '<a:z_Diamond_1555:778273709865173022>Você Ganhou Uma Conquista, Olhe Seu Privado<a:z_Diamond_1555:778273709865173022>')
                                                        conquista2 = discord.Embed(
                                                            title='<a:z_Diamond_1555:778273709865173022> Conquista <a:z_Diamond_1555:778273709865173022>',
                                                            color=color,
                                                            description=f'**Parabéns Esse É O Seu Certificado Para Confimar A Sua Conquista {ctx.author.mention} **\n\n\n***Nome: CAINDO ATIRANDO***\n\n**O Que Eu Posso Fazer Com Esse Certificado?**\nVocê Ganha O Cargo O SALVADOR\n\nObs: Se O Cargo Não Apareceu Significa Que O Server Não Possui A Tag Com O Nome  CAINDO ATIRANDO  !')
                                                        await ctx.author.send(embed=conquista2)
                                                        role = discord.utils.find(lambda r: r.name == "CAINDO ATIRANDO",
                                                                                  ctx.guild.roles)
                                                        await ctx.author.add_roles(role)
                                                        await asyncio.sleep(3)
                                                        await ctx.channel.send('***Fênix te mata***', embed=embed2)

                                                    elif resposta20 == 'c':
                                                        await ctx.channel.send('**OBRIGADO HUMANO**')
                                                        await asyncio.sleep(3)
                                                        await ctx.channel.send('**AGORA MORRRAAA**')
                                                        await asyncio.sleep(2)
                                                        await ctx.channel.send('***Ao elogiar o Fênix, ele te mata***',
                                                                               embed=embed2)













                                            else:
                                                await ctx.channel.send('***Resposta Errada, O Fênix Te Matou***')
                                                await ctx.channel.send(embed=embed2)








                                    else:
                                        await ctx.channel.send('Era Para Falar B ou A ;-;')
                                        await ctx.channel.send(embed=embed2)






                                else:

                                    await ctx.channel.send('***Resposta Errada, O Fênix Te Matou***')
                                    await ctx.channel.send(embed=embed2)

                            else:

                                await ctx.channel.send('***Resposta Errada, O Fênix Te Matou***')
                                await ctx.channel.send(embed=embed2)





                    else:

                        await ctx.channel.send('***Resposta Errada, O Fênix Te Matou***')
                        await ctx.channel.send(embed=embed2)







                else:
                    await asyncio.sleep(1.5)
                    await ctx.channel.send('***Após Perder, O Fênix Te Mata***', embed=embed2)


            else:
                await ctx.channel.send('**HAHAHA SABIA QUE NÃO IA ACEITAR H U M A N O FRACO**')


        else:
            await ctx.channel.send('**Desafio cancelado!!**')




    elif unit == 'lock':
        if ctx.message.author.guild_permissions.administrator or ctx.author == ctx.guild.owner:

            inserir = 'INSERT INTO block (servid, desafiar) VALUES (%s, %s)'
            dados = (ctx.author.guild.id, 1)
            try:
                cursor.execute(inserir, dados)

                mydb.commit()
                await ctx.channel.send(
                    f':white_check_mark: Comando **bloqueado** com sucesso! Utilize `f!desafiar unlock` para desbloquear')
                ctx.command.reset_cooldown(ctx)
                return
            except:
                await ctx.channel.send(
                    f'<:error:788824695184424980> Esse comando já está **bloqueado**. Use `f!desafiar unlock` para desbloquear!')
                cursor.execute("ROLLBACK")
                ctx.command.reset_cooldown(ctx)
                return
        else:
            await ctx.channel.send(
                f'<:error:788824695184424980> Você precisa ter o cargo com a permissão de **administrador** para executar este comando!')
            cursor.execute("ROLLBACK")
            ctx.command.reset_cooldown(ctx)
            return

    elif unit == 'unlock':

        if ctx.message.author.guild_permissions.administrator or ctx.author == ctx.guild.owner:
            pass
        else:
            return await ctx.send('<:error:788824695184424980>| Você não possui **Permissão** de *Administrador*!')

        sqlinsert = f'SELECT desafiar FROM block WHERE servid = {ctx.author.guild.id}'
        try:

            cursor.execute(sqlinsert)

        except:
            pass

        valores_lidos = cursor.fetchone()
        try:
            print(valores_lidos[0])
            inserir = f'DELETE FROM block WHERE servid = {ctx.author.guild.id}'
            cursor.execute(inserir)
            mydb.commit()
            await ctx.channel.send(
                ':white_check_mark: Comando **desbloqueado** com sucesso!! Utilize o comando `f!desafiar lock` para bloquear novamente!')
            ctx.command.reset_cooldown(ctx)
            return
        except:
            await ctx.channel.send('<:error:788824695184424980> Esse comando já está **desbloqueado**!!')

            return ctx.command.reset_cooldown(ctx)
    else:
        return ctx.command.reset_cooldown(ctx)



