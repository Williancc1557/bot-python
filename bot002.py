import discord
import asyncio
from discord.ext import commands
import random
from discord.ext.commands.cooldowns import BucketType
import datetime
import psycopg2

from time import sleep

from adm.suporte import Add_suporte, Remove_suporte, Identificar, Clean_fenix, Ajuda_suporte, Add_fenicoins, Remove_fenicoins, Set_fenicoins, Ban_fenix, Unban_fenix
from Principais.principais import Avaliar, bot, Avatar, Invite, mydb
from moderacao.Moderacao import Mute, Ban, Unban, Unmute, Warn, Warn_remove, Check_warns, Limpar, Embed
from events.events import On_ready, On_command_error, On_message, On_guild_remove, On_member_join, On_guild_join
from Diversao.diversao import Desafiar, Coinflip
from Economia.economia import Criar_conta, Conta, Desc_edit, Transferir, Diaria, Cor, Roubar, Arma, Fenicoins, Top_global, Roubar_banco



intents = discord.Intents.default()
intents.members = True
x = datetime.datetime.now()

bot = bot
mydb = mydb

bot.remove_command("help")
prefix = 'f!'
color = 0x0000FF





async def manutenção(ctx):

    await ctx.reply('<:error:788824695184424980>| Esse comando foi **Desativado** temporariamente pela equipe de suporte do fênix!')
    return False



def check_ban(ctx):
    sqlinsert3 = f'SELECT idban FROM ban WHERE idban = {ctx.author.id}'

    cursor.execute(sqlinsert3)

    valores_lidos3 = cursor.fetchone()


    if valores_lidos3 == None:
        return True
    else:
        return False



@bot.event
@commands.guild_only()
@commands.check(check_ban)
async def on_ready():
   return await On_ready()





t = BucketType.default



@bot.event
@commands.guild_only()
@commands.check(check_ban)
async def on_command_error(ctx, error):
    return await On_command_error(ctx,error=error)



@bot.event
@commands.guild_only()
@commands.check(check_ban)

async def on_message(message):
    return await On_message(message)








#Girar moeda

@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def coinflip(ctx, bet: str = None):
    return await Coinflip(ctx, bet=bet)








                                         #BANIR

@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def ban(ctx, member: discord.Member, *, reason = '*Motivo não especificado*'):
    return await Ban(ctx, member=member, reason=f'{reason}')

@ban.error
async def on_ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
         await ctx.reply(
            '<:error:788824695184424980>| **Reescreva** o comando no seguinte formato `f!ban <@user> <Motivo>`')

    if isinstance(error, commands.MemberNotFound):
        await ctx.reply(f'<:error:788824695184424980>| Não encontrei o `{error.argument}` em lugar algum!')





                                                        #desbanir

@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def unban(ctx, id: int):
    await Unban(ctx, id=id)

@unban.error
async def on_unban_error(ctx, error):

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('<:error:788824695184424980>| **Reescreva** o comando no seguinte formato `f!unban <user_id>`')

                                                   #convidar o bot


@bot.command()
@commands.guild_only()
@commands.check(check_ban)
@commands.cooldown(1, 40, commands.BucketType.user)
async def invite(ctx):
    await Invite(ctx)


@invite.error
async def invite(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send('**<:error:788824695184424980>| {} Você Precisa Esperar `{:.0f} Segundos` Para Dar O Comando Novamente**'.format(ctx.author.mention ,error.retry_after))


                                                 #mutar alguém:


@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def mute(ctx, member: discord.Member = None, mute_minutes: int = 0, unit=None):
    await Mute(ctx, member, mute_minutes, unit)




bot.reactionsm = {}

@bot.command(name='welcome', aliases=['bemvindo', 'BemVindo', 'BEMVINDO'])
@commands.guild_only()
@commands.check(check_ban)
async def welcome(ctx):
        if ctx.message.author.guild_permissions.administrator or ctx.author == ctx.guild.owner:
            pass
        else:
            return await ctx.reply('<:error:788824695184424980>| Você não possui a permissão de **Administrador!**')

        embed = discord.Embed(
               title='*** Olá, meu nome é Fênix 🐦***',
               description='Fui criado com o objetivo de ajudar os servidores tanto na moderação quanto na diversão!!\n'
                           '\n'
                           '\n'
                           '**<a:feliz:815313006937899009> Mensagens De Bem Vindo **\n'
                           '\n'
                           '\n'
                           '\n'
                           '<a:number_1:815207357751361536> **: Primeira Mensagem**\n'
                           '\n'
                           '<a:number_2:815207379988905994> **: Segunda Mensagem**\n'
                           '\n'
                           '<a:number_3:815207399686144030> **: Terceira Mensagem**\n'
                           '\n'
                           '<a:number_4:815207421316300840> **: Quarta mensagem**\n'
                           '\n'
                           '<:error:788824695184424980> **: Apagar Configuração**\n ㅤㅤ',
               color=0x00BFFF)
        embed.set_thumbnail(
               url='https://media.discordapp.net/attachments/788064370722340885/788170896363618345/1607735746221.png')


        msg = await ctx.reply(ctx.author.mention, embed=embed)

        await msg.add_reaction('<a:number_1:815207357751361536>')
        await msg.add_reaction('<a:number_2:815207379988905994>')
        await msg.add_reaction('<a:number_3:815207399686144030>')
        await msg.add_reaction('<a:number_4:815207421316300840>')
        await msg.add_reaction('<:error:788824695184424980>')

        bot.reactionsm[str(msg.id)] = ctx.author

        await asyncio.sleep(250)

        await msg.delete()
        bot.reactionsm.pop(str(msg.id))





           #desmutar alguém:


@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def unmute(ctx, member: discord.Member = None):
    await Unmute(ctx, member=member)
                                        #. . . . . . .












                                           #APAGAR MENSAGENS EM MASSA



@bot.command(pass_context=True, name='limpar',aliases=['clean', 'clear'])
@commands.guild_only()
@commands.cooldown(1, 3.5, commands.BucketType.user)
async def limpar(ctx, amount: int = None):
  await Limpar(ctx, amount=amount)



@limpar.error
async def ajuda_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send('<:error:788824695184424980>| {} Você Precisa Esperar  **Milissegundos** Para Dar O Comando Novamente'.format(ctx.author.mention, error.retry_after))










@bot.command()
async def avatar(ctx, member: discord.Member = None):
    await Avatar(ctx, member)










@bot.command()
@commands.check(check_ban)
@commands.guild_only()
async def warn(ctx, member: discord.Member = None, *, motivo: str = 'Motivo Não Especificado!'):
    return await Warn(ctx, member=member, motivo=motivo)




@warn.error
async def warn_error(ctx, error):
                if isinstance(error, commands.MemberNotFound):
                    await ctx.channel.send(
                        f'<:error:788824695184424980>| Desculpe {ctx.author.mention}, Procurei o membro `{error.argument}` por todo canto, mas acabei não o encontrando')







@bot.command(name='warn_remove', aliases=['remove_warn', 'warn_r', 'REMOVE_WARN'])
@commands.check(check_ban)
@commands.guild_only()
async def warn_remove(ctx, member: discord.Member = None):
    await Warn_remove(ctx, member=member)



@warn_remove.error
async def warn_remove_error(ctx, error):
                if isinstance(error, commands.MemberNotFound):
                    await ctx.channel.send(
                        f'<:error:788824695184424980>| Desculpe {ctx.author.mention}, Procurei o membro `{error.argument}` por todo canto, mas acabei não o encontrando')










@bot.command(name='check_warns', aliases=['warns_check', 'w_c', 'check_warn'])
@commands.check(check_ban)
@commands.guild_only()
async def check_warns(ctx, member: discord.Member = None):
    await Check_warns(ctx, member=member)











@check_warns.error
async def check_warns_error(ctx, error):
                if isinstance(error, commands.MemberNotFound):
                    await ctx.channel.send(
                        f'<:error:788824695184424980>| Desculpe {ctx.author.mention}, Procurei o membro `{error.argument}` por todo canto, mas acabei não o encontrando')

                    #Criar embed


@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def embed(ctx):
      await Embed(ctx)




                                                     #painel de ajuda:

bot.reactions = {}
@bot.command(name='ajuda', aliases=['help', 'Help', 'HELP'])
@commands.guild_only()
@commands.check(check_ban)
@commands.cooldown(1, 15, commands.BucketType.user)
async def ajuda(ctx):
    embed = discord.Embed(
        title='*** Olá, meu nome é Fênix 🐦***',
        description='Fui criado com o objetivo de ajudar os servidores tanto na moderação quanto na diversão!!\n'
                    '\n'
                    '\n'
                    '**👮 Servidor Para Suporte**\n'
                    '[Clique aqui](https://discord.gg/VDTAt3Qb9X) para entrar no servidor de suporte!\n'
                    '\n'
                    '\n'
                    '<a:emoji_42:815378184219918336> **: Comandos Principais**\n'
                    '\n'
                    '<a:emoji_44:815378316617580575> **: Comandos De Diversão**\n'
                    '\n'
                    '<a:emoji_43:815378237563207680> **: Comandos De Economia**\n'
                    '\n'
                    '<a:emoji_45:815378376528887859> **: Comandos Para Moderadores**\n'
                    '\n'
                    '<a:seta:796356802760933387> **: Pagina Inicial**\n ㅤㅤ',
        color=0x00BFFF)
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/788064370722340885/823220448351354910/20210317_111410.jpg?width=650&height=650')

    global msg
    msg = await ctx.reply(ctx.author.mention, embed=embed)

    await msg.add_reaction('<a:emoji_42:815378184219918336>')
    await msg.add_reaction('<a:emoji_44:815378316617580575>')
    await msg.add_reaction('<a:emoji_43:815378237563207680>')
    await msg.add_reaction('<a:emoji_45:815378376528887859>')
    await msg.add_reaction('<a:seta:796356802760933387>')

    bot.reactions[str(msg.id)] = ctx.author

    await asyncio.sleep(200)

    await msg.delete()
    bot.reactions.pop(str(msg.id))

@ajuda.error
async def ajuda_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send('**<:error:788824695184424980>| {} Você Precisa Esperar `{:.0f} Segundos` Para Dar O Comando Novamente**'.format(ctx.author.mention, error.retry_after))



                                                      #Avaliar o bot

@bot.command()
@commands.guild_only()
@commands.check(check_ban)
@commands.cooldown(1, 7200, commands.BucketType.user)
async def avaliar(ctx):
    await Avaliar(ctx)


@avaliar.error
async def avaliar_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send('**<:error:788824695184424980>| {} Você Precisa Esperar `{:.0f} Segundos` Para Dar O Comando Novamente**'.format(ctx.author.mention ,error.retry_after))


                                                                 #Desafiar o fênix:

cursor = mydb.cursor()
@bot.command()
@commands.guild_only()
@commands.check(check_ban)
@commands.check(manutenção)
@commands.cooldown(1, 70, commands.BucketType.channel)
async def desafiar(ctx, unit=None):
  return await Desafiar(ctx, unit=unit)


@desafiar.error
async def desafiar_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send('**<:error:788824695184424980>| {} Esse canal precisa esperar `{:.0f} Segundos` Para Dar O Comando `f!desafiar fênix`Novamente**'.format(ctx.author.mention, error.retry_after))






















#----------------------------------------------------------------------------------------------------------------------------------------------






















print(f'\033[1;35m{mydb}\033[m')


#CRIAR CONTA



@bot.command(name='criar_conta',aliases=['criar', 'create'])
@commands.guild_only()
@commands.check(check_ban)
async def criar_conta(ctx):
    await Criar_conta(ctx)

                   #OLHAR A CONTA



@bot.command(name='conta',aliases=['cont', 'con', 'account', 'CONTA'])
@commands.guild_only()
@commands.check(check_ban)
async def conta(ctx,  member: discord.Member = None):
    return await Conta(ctx, member=member)


#EDITAR DESCRIÇÃO



@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def desc_edit(ctx):
    return await Desc_edit(ctx=ctx)



                       #transferir dinheiro


@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def transferir(ctx,  member: discord.Member = None, dinheiro: int = 10):
    await Transferir(ctx, member=member, dinheiro=dinheiro)



@transferir.error
async def transferir_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        await ctx.channel.send(
            f'<:error:788824695184424980> Desculpe {ctx.author.mention}, Procurei o membro `{error.argument}` por todo canto mas acabei não o encontrando')
        ctx.command.reset_cooldown(ctx)

@bot.command(name='diaria',aliases=['daily', 'diária', 'diario'])
@commands.guild_only()
@commands.check(check_ban)
@commands.cooldown(1, 86400, commands.BucketType.user)
async def diaria(ctx):
        await Diaria(ctx)



@diaria.error
async def diaria_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send(
            '**<:error:788824695184424980> {} Você precisa esperar `{:.1f} horas` Para Dar O Comando `f!diaria`Novamente**'.format(ctx.author.mention, error.retry_after/3600))




@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def cor(ctx):
    await Cor(ctx)





@bot.command(name='roubar',aliases=['rob'])
@commands.guild_only()
@commands.check(check_ban)
@commands.cooldown(1, 43200, commands.BucketType.user)
async def roubar(ctx, member: discord.Member = None):
    await Roubar(ctx, member=member)


@roubar.error
async def roubar_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send(
            '**<:error:788824695184424980> {} Você precisa esperar `{:.1f}` **Horas** Para Dar O Comando `f!roubar` Novamente**'.format(ctx.author.mention, error.retry_after/3600))
    if isinstance(error, commands.MemberNotFound):
        await ctx.channel.send(
            f'<:error:788824695184424980> Desculpe {ctx.author.mention}, Procurei o membro `{error.argument}` por todo canto mas acabei não o encontrando!')
        ctx.command.reset_cooldown(ctx)


@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def arma(ctx):
    await Arma(ctx)


@bot.command(name='fenicoins', aliases=['feni', 'coins', 'fenic', 'coin'])
@commands.guild_only()
@commands.check(check_ban)
async def fenicoins(ctx, member: discord.Member = None):
    await Fenicoins(ctx, member=member)




@bot.command(name='top_global', aliases=['global', 'top', 'top_g', 'top_'])
@commands.guild_only()
@commands.check(check_ban)
async def top_global(ctx):
    await Top_global(ctx)






@bot.command()
@commands.guild_only()
@commands.check(check_ban)
@commands.cooldown(1, 43200, commands.BucketType.member and commands.BucketType.user)
async def roubar_banco(ctx, member1: discord.Member = None):
    await Roubar_banco(ctx, member1=member1)


@roubar_banco.error
async def banco_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send('**<:error:788824695184424980>| {} Você precisa esperar `{:.0f} Horas` Para Dar O Comando `f!roubar_banco`Novamente**'.format(ctx.author.mention, error.retry_after / 3600))


bot.reactions_autor = {}
bot.reactions_member = {}
@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def apostar(ctx, member: discord.Member = None, dindin : int = None):


    if member == ctx.author:
        await ctx.channel.send('<:error:788824695184424980> Você não pode apostar fenicoins com **si mesmo**, seu bobinho.')
        return

    if not dindin and not member:
        embed = discord.Embed(title='Comandin de aposta!!\n'
                                                         '`f!apostar`',
                                                   description='Esse comandinho serve para você apostar uns *fenicoins* com seu amiguinho!',
                                                   color=0x00BFFF)
        embed.add_field(name='📚 Como usar', value = '`f!apostar @WiLL 1000`')
        await ctx.channel.send(embed=embed)
        return

    if not dindin:
        await ctx.channel.send('<:error:788824695184424980> Você precisa escrever a **quantidade** de *fenicoins* que deseja apostar!!')
        return


    if dindin <= 10:
        await ctx.channel.send('<:error:788824695184424980> Ai não da meu parceiro, tem q apostar **um pouquinho mais de fenicoins** *para eu poder cobrar aquela taxinha de entrada massa de 5%*.')
        return


    sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {ctx.author.id}'

    cursor.execute(sqlinsert2)

    valores_lidos2 = cursor.fetchone()

    try:
        print(valores_lidos2[0])
    except:
        await ctx.channel.send(
            embed=discord.Embed(
                title=f'<:error:788824695184424980> **Você não possui uma conta no fênix!!**',
                color=0xFF0000))
        ctx.command.reset_cooldown(ctx)
        return


    global dindon
    dindon = dindin

    if valores_lidos2[0] < dindin:
        await ctx.channel.send(f'<:error:788824695184424980>| Você {ctx.author.mention}, não possui **fenicoins** suficiente para a aposta!')
        return

    try:
        try:
            sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {member.id}'

            cursor.execute(sqlinsert2)

            valores_lidos3 = cursor.fetchone()
            print(valores_lidos3[0])
        except:
            await ctx.channel.send(
                embed=discord.Embed(
                    title=f'<:error:788824695184424980> **O(a) `{member.name}` não possui uma conta no fênix!!**',
                    color=0xFF0000))
            ctx.command.reset_cooldown(ctx)
            return

        if valores_lidos3[0] < dindin:
            await ctx.channel.send(f'<:error:788824695184424980>| O(a) {member.mention} não possui **fenicoins** suficiente para a aposta!')
            return
    except:
        pass

    if member:
        global a
        a = await ctx.channel.send(f'Ei {member.mention}, parece que o(a) {ctx.author.mention} quer fazer uma aposta com você! Onde cada um cada um vai pagar **{dindin - (dindin * 0.05)} fenicoin ( Vou cobrar uma taxa de {0.05 * dindin:.0f} fenicoin xD )**\n\n🤝| Para aceitar a aposta, você {member.mention} deve clicar na reação ✅')
        await a.add_reaction('✅')
        bot.reactions_member[str(a.id)] = member
        bot.reactions_autor[str(a.id)] = ctx.author

        await asyncio.sleep(100)

        bot.reactions_member.pop(str(a.id))
        bot.reactions_autor.pop(str(a.id))




@apostar.error
async def apostar_error(ctx, error):
    if isinstance(error, commands.MemberNotFound):
        return await ctx.channel.send(
            f'<:error:788824695184424980> Desculpe {ctx.author.mention}, Procurei o membro `{error.argument}` por todo canto mas acabei não o encontrando')






#---------------------------------------------------------------------------------------------------------------------------------------------------------------







@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def add_suporte(ctx, member: discord.Member = None):
    await Add_suporte(ctx, member=member)




@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def remove_suporte(ctx, member: discord.Member = None):
    await Remove_suporte(ctx, member=member)


@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def identificar(ctx, member: discord.Member = None):
    await Identificar(ctx, member=member)



@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def clean_fenix(ctx, amount=10):
    await Clean_fenix(ctx,amount=amount)


@bot.command()
@commands.guild_only()
@commands.check(check_ban)
@commands.cooldown(1, 20, commands.BucketType.user)
async def ajuda_suporte(ctx):
    await Ajuda_suporte(ctx)

@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def add_fenicoins(ctx, member: discord.Member, valor: int):
    await Add_fenicoins(ctx, member=member, valor=valor)

@bot.command()
@commands.guild_only()
async def remove_fenicoins(ctx, member: discord.Member, valor: int):
    await Remove_fenicoins(ctx, member=member, valor=valor)

@bot.command()
@commands.guild_only()
@commands.check(check_ban)
async def set_fenicoins(ctx, member: discord.Member, valor: int):
    await Set_fenicoins(ctx, member=member, valor=valor)



@bot.command()
@commands.check(check_ban)
async def ban_fenix(ctx, member, *, motivo: str = 'Motivo não especificado!'):
    await Ban_fenix(ctx, member=member, motivo=motivo)


@bot.command()
@commands.check(check_ban)
async def unban_fenix(ctx, member: int):
    await Unban_fenix(ctx, member=member)



#----------------------------------------------------------------------------------------------------------------

@bot.event
@commands.check(check_ban)
async def on_reaction_add(reaction, user):
        cursor.execute("ROLLBACK")
        mydb.commit()

        wellcomeUser = bot.reactionsm.get(str(reaction.message.id))
        member1 = bot.reactions_member.get(str(reaction.message.id))
        autor1 = bot.reactions_autor.get(str(reaction.message.id))
        autor = bot.reactions.get(str(reaction.message.id))
        react = str(reaction)



        sqlinsert3 = f'SELECT mensagem FROM welcome WHERE idserv = {reaction.message.guild.id}'

        cursor.execute(sqlinsert3)

        valores_lidos3 = cursor.fetchone()




        # COMANDO DE AJUDA:

        if autor == user and react == '<a:emoji_42:815378184219918336>':
            embed = discord.Embed(
                title='<a:feliz:815313006937899009> Comandos Principais <a:feliz:815313006937899009>',
                description=''
                ,

                color=0x00BFFF)
            embed.add_field(name='ㅤ\n<a:Upd:815312986528677899> Avaliar O Fênix', value='`f!avaliar`\nㅤ', inline=False)
            embed.add_field(name='<a:Upd:815312986528677899> Convidar O Fênix', value='`f!invite`\nㅤ', inline=False)
            embed.add_field(name=':frame_photo: Ver Avatar', value='`f!avatar <@user>`\nㅤ', inline=False)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/823220448351354910/20210317_111410.jpg?width=650&height=650')
            await reaction.message.edit(embed=embed)
            await reaction.remove(user)
        if autor == user and react == '<a:emoji_44:815378316617580575>':
            embed = discord.Embed(
                title='Comandos De Diversão',
                color=0x00BFFF,
                description=f'\n\n**meu prefixo é** `f!`\n\n'

            )
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/823220448351354910/20210317_111410.jpg?width=650&height=650')

            embed.add_field(name='ㅤ\n<:moeda:815324002649767986> Girar Moeda', value='`f!coinflip`\nㅤ', inline=False)
            embed.add_field(name=':crossed_swords: Desafiar Fênix', value='`f!desafiar fênix`\nㅤ', inline=False)

            await reaction.message.edit(embed=embed)
            await reaction.remove(user)

        if autor == user and react == '<a:emoji_43:815378237563207680>':
            embed = discord.Embed(
                title=':moneybag: Bem Vindo ao painel de economia!!',
                description='***Comandos de economia***\n'

                ,
                color=0x00BFFF)
            embed.add_field(name='ㅤ\n<a:Upd:815312986528677899> Criar Sua Conta', value='`f!criar_conta`\nㅤ',
                            inline=False)
            embed.add_field(name=':bank:  Olhar Conta', value='`f!conta` ou `f!conta <@user>`\nㅤ', inline=False)
            embed.add_field(name='<a:giveway:815050719803211786> Pegar Sua Diária', value='`f!diária`\nㅤ', inline=False)
            embed.add_field(name='<a:transferir:815378076250800139> Transferir Fenicoins',
                            value='`f!transferir <@user> <valor>`\nㅤ', inline=False)
            embed.add_field(name=':scroll: Editar Descrição', value='`f!desc_edit`\nㅤ', inline=False)
            embed.add_field(name=':art: Cor Da Conta', value='`f!desc_edit`\nㅤ', inline=False)
            embed.add_field(name='<a:gun_1:815387129999130636> Roubar Alguém', value='`f!roubar <@user>`\nㅤ',
                            inline=False)
            embed.add_field(name='<a:gun_1:815387129999130636> Armamento', value='`f!roubar <@user>`\nㅤ', inline=False)
            embed.add_field(name='<:moeda:815324002649767986> Ver Fenicoins', value='`f!coin` ou `f!coin <@user>`\nㅤ',
                            inline=False)
            embed.add_field(name='<a:Top:815388123039006741> Ver Os Ricos', value='`f!top_global`\nㅤ', inline=False)
            embed.add_field(name='<a:gun_1:815387129999130636> Roubar Banco',
                            value='`f!roubar_banco` ou `f!roubar_banco <@user>`\nㅤ', inline=False)
            embed.add_field(name='<:moeda:815324002649767986> Apostar Fenicoins', value='`f!apostar <@user>`\nㅤ',
                            inline=False)

            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/823220448351354910/20210317_111410.jpg?width=650&height=650')

            await reaction.message.edit(embed=embed)
            await reaction.remove(user)

        if autor == user and react == '<a:emoji_45:815378376528887859>':
            embed = discord.Embed(
                title='<:reforma:774259152829677589> Comandos para Moderadores <:reforma:774259152829677589>',
                description=''
                ,

                color=0x00BFFF)
            embed.add_field(name='ㅤ\n<a:ban:815316725402566666> Banimento', value='`f!ban <@user> <motivo>`',
                            inline=False)
            embed.add_field(name='<a:ban:815316725402566666> Unbanimento', value='`f!unban <user_id>`\nㅤ', inline=False)

            embed.add_field(name='<a:muted:815317083427569665> Mutar', value='`f!mute <@user>`', inline=False)
            embed.add_field(name='<a:muted:815317083427569665> Desmutar', value='`f!unmute <@user>`\nㅤ', inline=False)

            embed.add_field(name=':octagonal_sign: Desafiar (lock/unlock)', value='`f!desafiar (lock/unlock)`',
                            inline=False)
            embed.add_field(name=':book: Embed', value='`f!embed`', inline=False)
            embed.add_field(name='<a:lixo:818920412233859083> Limpar Chat', value='`f!limpar <quantidade>`', inline=False)
            embed.add_field(name='<:emoji_12:778982435920150538> Mensagem De Bem Vindo', value='`f!welcome` ou `f!bemvindo`\nㅤ', inline=False)
            embed.add_field(name='<a:warn:818918476915540020> Penalizar Alguém (warn)', value='`f!warn <@user> <motivo>`',
                            inline=False)
            embed.add_field(name='<a:warn:818918476915540020> Despenalizar Alguém (warn_remove)', value='`f!warn_remove <@user>`', inline=False)
            embed.add_field(name='<a:warn:818918476915540020> Ver Penalidade (warn)', value='`f!warn_checks <@user>` ou `f!checks_warn <@user>`\nㅤ', inline=False)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/823220448351354910/20210317_111410.jpg?width=650&height=650')

            await reaction.message.edit(embed=embed)
            await reaction.remove(user)

        if autor == user and react == '<a:seta:796356802760933387>':
            embed = discord.Embed(
                title='*** Olá, meu nome é Fênix 🐦***',
                description='Fui criado com o objetivo de ajudar os servidores tanto na moderação quanto na diversão!!\n'
                            '\n'
                            '\n'
                            '**👮 Servidor Para Suporte**\n'
                            '[Clique aqui](https://discord.gg/VDTAt3Qb9X) para entrar no servidor de suporte!\n'
                            '\n'
                            '\n'
                            '<a:emoji_42:815378184219918336> **: Comandos Principais**\n'
                            '\n'
                            '<a:emoji_44:815378316617580575> **: Comandos De Diversão**\n'
                            '\n'
                            '<a:emoji_43:815378237563207680> **: Comandos De Economia**\n'
                            '\n'
                            '<a:emoji_45:815378376528887859> **: Comandos Para Moderadores**\n'
                            '\n'
                            '<a:seta:796356802760933387> **: Pagina Inicial**\n ㅤㅤ',
                color=0x00BFFF)

            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/823220448351354910/20210317_111410.jpg?width=650&height=650')

            await reaction.message.edit(embed=embed)

            await reaction.remove(user)

                # COINFLIP BET:

        if member1 == user and react == '✅':

            sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {autor1.id}'

            cursor.execute(sqlinsert2)

            valores_lidos2 = cursor.fetchone()

            sqlinsert2 = f'SELECT dinheiro FROM dinheiro WHERE id = {member1.id}'

            cursor.execute(sqlinsert2)

            valores_lidos3 = cursor.fetchone()

            randon = random.randint(1, 2)

            # se o autor ganhar:
            if randon == 1:
                await reaction.message.delete()

                sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] - (dindon * 0.05 - dindon):.0f}' WHERE id = {autor1.id}"

                cursor.execute(sqlinsert)

                mydb.commit()

                sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos3[0] + (dindon * 0.05 - dindon):.0f}' WHERE id = {member1.id}"

                cursor.execute(sqlinsert)

                mydb.commit()

                await reaction.message.channel.send(
                    f'Opa!! Parabéns {autor1.mention}, você ganhou a aposta de **{dindon - (dindon * 0.05):.0f} fenicoins** do(a) {member1.mention}')
                bot.reactions_member.pop(str(a.id))
                bot.reactions_autor.pop(str(a.id))
            # se o membro ganhar

            if randon == 2:
                await reaction.message.delete()
                sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos2[0] + (dindon * 0.05 - dindon):.0f}' WHERE id = {autor1.id}"

                cursor.execute(sqlinsert)

                mydb.commit()

                sqlinsert = f"UPDATE dinheiro SET dinheiro = '{valores_lidos3[0] - (dindon * 0.05 - dindon):.0f}' WHERE id = {member1.id}"

                cursor.execute(sqlinsert)

                mydb.commit()

                await reaction.message.channel.send(
                    f'Opa!! Parabéns {member1.mention}, você ganhou a aposta de **{dindon - (dindon * 0.05):.0f} fenicoins** do(a) {autor1.mention}')
                bot.reactions_member.pop(str(a.id))
                bot.reactions_autor.pop(str(a.id))



        if wellcomeUser == user and react == '<a:number_1:815207357751361536>' or wellcomeUser == user and react == '<a:verificao_1:815313840354361384>':

            embed = discord.Embed(
                title='<a:number_1:815207357751361536>   Primeira Mensagem',
                description='**<a:verificao_1:815313840354361384> Definir Mensagem!**\n'
                            '\n'
                            '**<a:seta:796356802760933387> Cancelar**',

                color=0x00BFFF)
            embed.set_image(
                url='https://media.discordapp.net/attachments/788064370722340885/816084509966729286/Screenshot_20210301-200702.png')
            await reaction.message.remove_reaction('<a:number_1:815207357751361536>', bot.user)
            await reaction.message.remove_reaction('<a:number_1:815207357751361536>', user)
            await reaction.message.remove_reaction('<a:number_2:815207379988905994>', bot.user)
            await reaction.message.remove_reaction('<a:number_3:815207399686144030>', bot.user)
            await reaction.message.remove_reaction('<a:number_4:815207421316300840>', bot.user)
            await reaction.message.remove_reaction('<:error:788824695184424980>', bot.user)

            message = await reaction.message.edit(embed=embed)

            await reaction.message.add_reaction('<a:verificao_1:815313840354361384>')
            await reaction.message.add_reaction('<a:seta:796356802760933387>')

            if react == '<a:verificao_1:815313840354361384>':
                await reaction.message.remove_reaction('<a:verificao_1:815313840354361384>', bot.user)
                await reaction.message.remove_reaction('<a:verificao_1:815313840354361384>', user)
                await reaction.message.remove_reaction('<a:seta:796356802760933387>', bot.user)

                msg1 = await reaction.message.channel.send(
                    '<a:verificao_1:815313840354361384> Escreva o **Id do chat** onde vai ser enviado a mensagem:')

                def check(p):
                    return p.author == user and p.channel == reaction.message.channel

                try:
                    til = await bot.wait_for('message', timeout=1000, check=check)
                except asyncio.TimeoutError:
                    return await reaction.message.channel.send('**Acabou O Tempo Para Aceitar**')
                else:

                    try:
                        idchannel = int(til.content)

                    except:
                        await reaction.message.add_reaction('<a:verificao_1:815313840354361384>')
                        await reaction.message.add_reaction('<a:seta:796356802760933387>')
                        error = await reaction.message.channel.send(
                            '<:error:788824695184424980>| isso não é um ID válido')
                        await asyncio.sleep(10)
                        return await error.delete()
                try:
                    channel = bot.get_channel(id=idchannel)
                    msg2 = await reaction.message.channel.send('<a:loading:785523240944664646> Verificando o ID')
                    await asyncio.sleep(10)
                    if channel.guild.id != reaction.message.guild.id:
                        await reaction.message.add_reaction('<a:verificao_1:815313840354361384>')
                        await reaction.message.add_reaction('<a:seta:796356802760933387>')
                        return await msg2.edit(
                            content='<:error:788824695184424980>| Esse chat **não faz parte** desse servidor!')
                    teste = await channel.send('<a:loading:785523240944664646>')
                    await teste.delete()
                except:
                    await reaction.message.add_reaction('<a:verificao_1:815313840354361384>')
                    await reaction.message.add_reaction('<a:seta:796356802760933387>')
                    await til.delete()
                    await msg1.delete()
                    return await msg2.edit(
                        content='<:error:788824695184424980>| **Não encontrei** nenhum chat com esse *ID* ')
                try:
                    inserir = 'INSERT INTO welcome (idserv, mensagem, channel) VALUES (%s, %s, %s)'
                    dados = (reaction.message.guild.id, 1, idchannel)
                    cursor.execute(inserir, dados)
                    mydb.commit()
                except:
                    await msg1.delete()
                    await til.delete()
                    await reaction.message.add_reaction('<a:verificao_1:815313840354361384>')
                    await reaction.message.add_reaction('<a:seta:796356802760933387>')
                    return await msg2.edit(content=
                                           f'<:error:788824695184424980>| Olá {user.mention} parece que esse servidor **já possui** mensagem de *bem vindo!*')
                await msg1.delete()
                await msg2.edit(
                    content=f'<a:Upd:815312986528677899> Mensagem de *Bem Vindo* Ativada no chat `{channel.name}` com **Sucesso!!**')
                await til.delete()
                await reaction.message.add_reaction('<a:verificao_1:815313840354361384>')
                await reaction.message.add_reaction('<a:seta:796356802760933387>')

                # NUMBER_2






        elif wellcomeUser == user and react == '<a:number_2:815207379988905994>' or wellcomeUser == user and react == '<a:verificao_2:815561265463164978>':
            embed = discord.Embed(
                title='<a:number_2:815207379988905994>   Segunda Mensagem',
                description='**<a:verificao_2:815561265463164978> Definir Mensagem!**\n'
                            '\n'
                            '**<a:seta:796356802760933387> Cancelar**',

                color=0x00BFFF)
            embed.set_image(
                url='https://media.discordapp.net/attachments/788064370722340885/816106100256276501/Screenshot_20210301-213253.png')
            await reaction.message.remove_reaction('<a:number_1:815207357751361536>', bot.user)
            await reaction.message.remove_reaction('<a:number_2:815207379988905994>', user)
            await reaction.message.remove_reaction('<a:number_2:815207379988905994>', bot.user)
            await reaction.message.remove_reaction('<a:number_3:815207399686144030>', bot.user)
            await reaction.message.remove_reaction('<a:number_4:815207421316300840>', bot.user)
            await reaction.message.remove_reaction('<:error:788824695184424980>', bot.user)

            message = await reaction.message.edit(embed=embed)

            await reaction.message.add_reaction('<a:verificao_2:815561265463164978>')
            await reaction.message.add_reaction('<a:seta:796356802760933387>')

            if react == '<a:verificao_2:815561265463164978>':
                await reaction.message.remove_reaction('<a:verificao_2:815561265463164978>', bot.user)
                await reaction.message.remove_reaction('<a:verificao_2:815561265463164978>', user)
                await reaction.message.remove_reaction('<a:seta:796356802760933387>', bot.user)

                msg1 = await reaction.message.channel.send(
                    '<a:verificao_1:815313840354361384> Escreva o **Id do chat** onde vai ser enviado a mensagem:')

                def check(p):
                    return p.author == user and p.channel == reaction.message.channel

                try:
                    til = await bot.wait_for('message', timeout=1000, check=check)
                except asyncio.TimeoutError:
                    return await reaction.message.channel.send(
                        '<:error:788824695184424980>| **Acabou O Tempo Para Responder**')
                else:

                    try:
                        idchannel = int(til.content)

                    except:
                        await reaction.message.add_reaction('<a:verificao_2:815561265463164978>')
                        await reaction.message.add_reaction('<a:seta:796356802760933387>')
                        error = await reaction.message.channel.send(
                            '<:error:788824695184424980>| isso não é um ID válido')
                        await til.delete()
                        await msg1.delete()
                        await asyncio.sleep(10)
                        return await error.delete()
                try:
                    channel = bot.get_channel(id=idchannel)
                    msg2 = await reaction.message.channel.send('<a:loading:785523240944664646> Verificando o ID')
                    await asyncio.sleep(10)

                    if channel.guild.id != reaction.message.guild.id:
                        await reaction.message.add_reaction('<a:verificao_1:815313840354361384>')
                        await reaction.message.add_reaction('<a:seta:796356802760933387>')
                        return await msg2.edit(
                            content='<:error:788824695184424980>| Esse chat **não faz parte** desse servidor!')
                    teste = await channel.send('<a:loading:785523240944664646>')
                    await teste.delete()
                except:
                    await reaction.message.add_reaction('<a:verificao_2:815561265463164978>')
                    await reaction.message.add_reaction('<a:seta:796356802760933387>')
                    await til.delete()
                    await msg1.delete()
                    return await msg2.edit(
                        content='<:error:788824695184424980>| **Não encontrei** nenhum chat com esse *ID* ')

                try:
                    inserir = 'INSERT INTO welcome (idserv, mensagem, channel) VALUES (%s, %s, %s)'
                    dados = (reaction.message.guild.id, 2, idchannel)
                    cursor.execute(inserir, dados)
                    mydb.commit()
                except:
                    await msg1.delete()
                    await reaction.message.add_reaction('<a:verificao_2:815561265463164978>')
                    await reaction.message.add_reaction('<a:seta:796356802760933387>')
                    return await msg2.edit(
                        content=f'<:error:788824695184424980>| Olá {user.mention} parece que esse servidor **já possui** mensagem de *bem vindo!*')
                await msg1.delete()
                await msg2.edit(
                    content=f'<a:Upd:815312986528677899> Mensagem de *Bem Vindo* Ativada no chat `{channel.name}` com **Sucesso!!**')
                await til.delete()
                await msg1.delete()
                await reaction.message.add_reaction('<a:verificao_2:815561265463164978>')
                await reaction.message.add_reaction('<a:seta:796356802760933387>')

                # NUMBER 3







        elif wellcomeUser == user and react == '<a:number_3:815207399686144030>' or wellcomeUser == user and react == '<a:verificao_3:815561286522765345>':
            embed = discord.Embed(
                title='<a:number_3:815207399686144030>   Terceira Mensagem',
                description='**<a:verificao_3:815561286522765345> Definir Mensagem!**\n'
                            '\n'
                            '**<a:seta:796356802760933387> Cancelar**',

                color=0x00BFFF)
            embed.set_image(
                url='https://media.discordapp.net/attachments/788064370722340885/816112025959923752/Screenshot_20210301-215627.png')
            await reaction.message.remove_reaction('<a:number_1:815207357751361536>', bot.user)
            await reaction.message.remove_reaction('<a:number_3:815207399686144030>', user)
            await reaction.message.remove_reaction('<a:number_2:815207379988905994>', bot.user)
            await reaction.message.remove_reaction('<a:number_3:815207399686144030>', bot.user)
            await reaction.message.remove_reaction('<a:number_4:815207421316300840>', bot.user)
            await reaction.message.remove_reaction('<:error:788824695184424980>', bot.user)

            message = await reaction.message.edit(embed=embed)

            await reaction.message.add_reaction('<a:verificao_3:815561286522765345>')
            await reaction.message.add_reaction('<a:seta:796356802760933387>')

            if react == '<a:verificao_3:815561286522765345>':
                await reaction.message.remove_reaction('<a:verificao_3:815561286522765345>', bot.user)
                await reaction.message.remove_reaction('<a:verificao_3:815561286522765345>', user)
                await reaction.message.remove_reaction('<a:seta:796356802760933387>', bot.user)

                msg1 = await reaction.message.channel.send(
                    '<a:verificao_3:815561286522765345> Escreva o **Id do chat** onde vai ser enviado a mensagem:')

                def check(p):
                    return p.author == user and p.channel == reaction.message.channel

                try:
                    til = await bot.wait_for('message', timeout=1000, check=check)
                except asyncio.TimeoutError:
                    return await reaction.message.channel.send(
                        '<:error:788824695184424980>| **Acabou O Tempo Para Responder**')
                else:

                    try:
                        idchannel = int(til.content)

                    except:
                        await reaction.message.add_reaction('<a:verificao_3:815561286522765345>')
                        await reaction.message.add_reaction('<a:seta:796356802760933387>')
                        error = await reaction.message.channel.send(
                            '<:error:788824695184424980>| isso não é um ID válido')
                        await til.delete()
                        await msg1.delete()
                        await asyncio.sleep(10)
                        return await error.delete()
                try:
                    channel = bot.get_channel(id=idchannel)
                    msg2 = await reaction.message.channel.send('<a:loading:785523240944664646> Verificando o ID')
                    await asyncio.sleep(10)

                    if channel.guild.id != reaction.message.guild.id:
                        await reaction.message.add_reaction('<a:verificao_3:815561286522765345>')
                        await reaction.message.add_reaction('<a:seta:796356802760933387>')
                        return await msg2.edit(
                            content='<:error:788824695184424980>| Esse chat **não faz parte** desse servidor!')
                    teste = await channel.send('<a:loading:785523240944664646>')
                    await teste.delete()
                except:
                    await reaction.message.add_reaction('<a:verificao_3:815561286522765345>')
                    await reaction.message.add_reaction('<a:seta:796356802760933387>')
                    await til.delete()
                    await msg1.delete()
                    return await msg2.edit(
                        content='<:error:788824695184424980>| **Não encontrei** nenhum chat com esse *ID* ')

                try:
                    inserir = 'INSERT INTO welcome (idserv, mensagem, channel) VALUES (%s, %s, %s)'
                    dados = (reaction.message.guild.id, 3, idchannel)
                    cursor.execute(inserir, dados)
                    mydb.commit()
                except:
                    await msg1.delete()
                    await reaction.message.add_reaction('<a:verificao_3:815561286522765345>')
                    await reaction.message.add_reaction('<a:seta:796356802760933387>')
                    return await msg2.edit(
                        content=f'<:error:788824695184424980>| Olá {user.mention} parece que esse servidor **já possui** mensagem de *bem vindo!*')
                await msg1.delete()
                await msg2.edit(
                    content=f'<a:Upd:815312986528677899> Mensagem de *Bem Vindo* Ativada no chat `{channel.name}` com **Sucesso!!**')
                await til.delete()

                await reaction.message.add_reaction('<a:verificao_3:815561286522765345>')
                await reaction.message.add_reaction('<a:seta:796356802760933387>')

                # MENSAGEM 4




        elif wellcomeUser == user and react == '<a:number_4:815207421316300840>' or wellcomeUser == user and react == '<a:verificao_4:815561308577464321>':
            embed = discord.Embed(
                title='<a:number_4:815207421316300840>   Terceira Mensagem',
                description='**<a:verificao_4:815561308577464321> Definir Mensagem!**\n'
                            '\n'
                            '**<a:seta:796356802760933387> Cancelar**',

                color=0x00BFFF)
            embed.set_image(
                url='https://media.discordapp.net/attachments/788064370722340885/816114550457106482/Screenshot_20210301-220616.png')
            await reaction.message.remove_reaction('<a:number_1:815207357751361536>', bot.user)
            await reaction.message.remove_reaction('<a:number_4:815207421316300840>', user)
            await reaction.message.remove_reaction('<a:number_2:815207379988905994>', bot.user)
            await reaction.message.remove_reaction('<a:number_3:815207399686144030>', bot.user)
            await reaction.message.remove_reaction('<a:number_4:815207421316300840>', bot.user)
            await reaction.message.remove_reaction('<:error:788824695184424980>', bot.user)

            message = await reaction.message.edit(embed=embed)

            await reaction.message.add_reaction('<a:verificao_4:815561308577464321>')
            await reaction.message.add_reaction('<a:seta:796356802760933387>')

            if react == '<a:verificao_4:815561308577464321>':
                await reaction.message.remove_reaction('<a:verificao_4:815561308577464321>', bot.user)
                await reaction.message.remove_reaction('<a:verificao_4:815561308577464321>', user)
                await reaction.message.remove_reaction('<a:seta:796356802760933387>', bot.user)

                msg1 = await reaction.message.channel.send(
                    '<a:verificao_4:815561308577464321> Escreva o **Id do chat** onde vai ser enviado a mensagem:')

                def check(p):
                    return p.author == user and p.channel == reaction.message.channel

                try:
                    til = await bot.wait_for('message', timeout=1000, check=check)
                except asyncio.TimeoutError:
                    return await reaction.message.channel.send(
                        '<:error:788824695184424980>| **Acabou O Tempo Para Responder**')
                else:

                    try:
                        idchannel = int(til.content)

                    except:
                        await reaction.message.add_reaction('<a:verificao_4:815561308577464321>')
                        await reaction.message.add_reaction('<a:seta:796356802760933387>')
                        error = await reaction.message.channel.send(
                            '<:error:788824695184424980>| isso não é um ID válido')
                        await til.delete()
                        await msg1.delete()
                        await asyncio.sleep(10)
                        return await error.delete()
                try:
                    channel = bot.get_channel(id=idchannel)
                    msg2 = await reaction.message.channel.send('<a:loading:785523240944664646> Verificando o ID')
                    await asyncio.sleep(10)

                    if channel.guild.id != reaction.message.guild.id:
                        await reaction.message.add_reaction('<a:verificao_4:815561308577464321>')
                        await reaction.message.add_reaction('<a:seta:796356802760933387>')
                        return await msg2.edit(
                            content='<:error:788824695184424980>| Esse chat **não faz parte** desse servidor!')
                    teste = await channel.send('<a:loading:785523240944664646>')
                    await teste.delete()
                except:
                    await reaction.message.add_reaction('<a:verificao_4:815561308577464321>')
                    await reaction.message.add_reaction('<a:seta:796356802760933387>')
                    await til.delete()
                    await msg1.delete()
                    return await msg2.edit(
                        content='<:error:788824695184424980>| **Não encontrei** nenhum chat com esse *ID* ')

                try:
                    inserir = 'INSERT INTO welcome (idserv, mensagem, channel) VALUES (%s, %s, %s)'
                    dados = (reaction.message.guild.id, 4, idchannel)
                    cursor.execute(inserir, dados)
                    mydb.commit()
                except:
                    await msg1.delete()
                    await reaction.message.add_reaction('<a:verificao_4:815561308577464321>')
                    await reaction.message.add_reaction('<a:seta:796356802760933387>')
                    return await msg2.edit(
                        content=f'<:error:788824695184424980>| Olá {user.mention} parece que esse servidor **já possui** mensagem de *bem vindo!*')
                await msg1.delete()
                await msg2.edit(
                    content=f'<a:Upd:815312986528677899> Mensagem de *Bem Vindo* Ativada no chat `{channel.name}` com **Sucesso!!**')
                await til.delete()

                await reaction.message.add_reaction('<a:verificao_4:815561308577464321>')
                await reaction.message.add_reaction('<a:seta:796356802760933387>')











        elif wellcomeUser == user and react == '<:error:788824695184424980>':
            try:
                if valores_lidos3 == None:
                    msg2 = await reaction.message.channel.send(
                        f'<:error:788824695184424980>| Esse servidor **Não Possui** mensagem de *Boas Vindas* do Fênix!')
                    await reaction.remove(user)
                    await asyncio.sleep(10)
                    await msg2.delete()
                    return

                inserir = f'DELETE FROM welcome WHERE idserv = {reaction.message.guild.id}'
                cursor.execute(inserir)
                mydb.commit()
                msg1 = await reaction.message.channel.send(
                    f'<a:Upd:815312986528677899> Mensagem de *Bem Vindo* **Removida!**')
                await reaction.remove(user)
                await asyncio.sleep(10)
                await msg1.delete()
            except:
                msg2 = await reaction.message.channel.send(
                    f'<:error:788824695184424980>| Esse servidor **Não Possui** mensagem de *Boas Vindas* do Fênix!')
                await asyncio.sleep(10)
                await msg2.delete()

        elif wellcomeUser == user and react == '<a:seta:796356802760933387>':
            embed = discord.Embed(
                title='*** Olá, meu nome é Fênix 🐦***',
                description='Fui criado com o objetivo de ajudar os servidores tanto na moderação quanto na diversão!!\n'
                            '\n'
                            '\n'
                            '**<a:feliz:815313006937899009> Mensagens De Bem Vindo **\n'
                            '\n'
                            '\n'
                            '\n'
                            '<a:number_1:815207357751361536> **: Primeira Mensagem**\n'
                            '\n'
                            '<a:number_2:815207379988905994> **: Segunda Mensagem**\n'
                            '\n'
                            '<a:number_3:815207399686144030> **: Terceira Mensagem**\n'
                            '\n'
                            '<a:number_4:815207421316300840> **: Quarta mensagem**\n'
                            '\n'
                            '<:error:788824695184424980> **: Apagar Configuração**\n ㅤㅤ',
                color=0x00BFFF)
            embed.set_thumbnail(
                url='https://media.discordapp.net/attachments/788064370722340885/788170896363618345/1607735746221.png')

            await reaction.message.edit(embed=embed)

            await reaction.message.remove_reaction('<a:verificao_1:815313840354361384>', bot.user)
            await reaction.message.remove_reaction('<a:verificao_2:815561265463164978>', bot.user)
            await reaction.message.remove_reaction('<a:verificao_3:815561286522765345>', bot.user)
            await reaction.message.remove_reaction('<a:verificao_4:815561308577464321>', bot.user)
            await reaction.message.remove_reaction('<a:seta:796356802760933387>', user)
            await reaction.message.remove_reaction('<a:seta:796356802760933387>', bot.user)

            await reaction.message.add_reaction('<a:number_1:815207357751361536>')
            await reaction.message.add_reaction('<a:number_2:815207379988905994>')
            await reaction.message.add_reaction('<a:number_3:815207399686144030>')
            await reaction.message.add_reaction('<a:number_4:815207421316300840>')
            await reaction.message.add_reaction('<:error:788824695184424980>')











        #------------------------------------------------------------------------------------------------------------------





@bot.event
async def on_guild_join(guild):
    return await On_guild_join(guild)

@bot.event
async def on_guild_remove(guild):
    return await On_guild_remove(guild)


@bot.event
async def on_member_join(member):
    return await On_member_join(member)



bot.run('Nzc2NjEzMjA5NDIzMjE2NjUw.X63baQ.w6TRoWGmiDtXBKYLEyRRtQKNt38')
