import discord
import asyncio
import random
import re
import time
import secreto

TOKEN = secreto.seu_token()

client = discord.Client()

msg_id = None
msg_user = None
msg_author = None

qntdd = int

def toint(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

@client.event
async def on_ready():
    print('BOT ONLINE - Hello World!')
    print(client.user.name)
    print(client.user.id)
    print('--------CHED--------')
    await client.change_presence(game=discord.Game(name='!help'))


say =discord.Embed(
        title="AVISO:",
        color=0xA31EF6,
        description=" ",

)

biografia =discord.Embed(
        title="Quem sou eu?",
        color=0x4BF085,
        description="Sou um queijo. Não qualquer tipo de queijo. O melhor tipo de queijo.\n"
                    "Diga não ao presunto. Também não confie em mussarela, eles mentem...\n"
                    "- Atenciosamente, Sr Cheese :cheese:"

)


help =discord.Embed(
        title="AJUDA:",
        color=0xFE9A2E,
        description=":pushpin:  Meu prefixo é :exclamation: (ponto de exclamação)\n"
                    "\n"
                    "**COMANDOS:**\n"
                    "\n"
                    ":cheese: :  **!cheddar** - Estou vivo? \n"
                    "Esse comando mostra a versão atual do meu desenvolvimento.\n"
                    "\n"
                    ":books: :  **!biografia** - Quem sou eu?\n"
                    "Saiba um pouco mais sobre mim. Eu posso ser bem interessante.\n"
                    "\n"
                    ":small_orange_diamond: :  **!moeda** - Cara ou coroa?\n"
                    "Ao usar esse comando, eu jogo uma moeda para o alto, e coloco uma reação na sua mensagem indicando se a moeda caiu cara ou coroa.\n"
                    "\n"
                    ":question: :  **!ask** - Me faça uma pergunta!\n"
                    "Digite `!ask (pergunta)` e obtenha uma resposta. Apenas respostas de sim ou não!\n"
                    "\n"
                    ":bulb: :  **!sugerir** - Envie sua sugestão!\n"
                    "Digite `!sugerir (sua sugestão)`.  Você também pode votar em sugestões enviadas por outros jogadores e contribuir com a sua opinião.\n"
                    "\n"
                    ":satellite: :  **!ping** - Pong!\n"
                    "Use esse comando para ver o ping (é, meio obvio, eu sei).\n"
                    "\n"
                    ":frame_photo: :  **!img** - Quer ibagens?\n"
                    "Peça ibagens como o Datena. Eu quero ibagens!\n"
                    "\n"
                    ":bust_in_silhouette: :  **!info** - Informações do usuário\n"
                    "Digite `!info (usuário)` para ver informações gerais desse membro.\n"
                    "\n"
                    ":raising_hand: :  **!help** ou **!ajuda** - Precisa de ajuda?\n"
                    "Esse comando mostra todos os outros comandos (ou quase todos).\n"
                    "\n"
                    ":cop: :  **!admin** - Comandos de moderação.\n"
                    "Exibe uma lista de comandos que são de uso exclusivo da equipe do servidor.\n"
                    "\n"
                    "É isso que eu faço!\n"
                    "**Abraço do Cheddinha.**"
)


admin =discord.Embed(
        title="ADMIN - Funções:",
        color=0x00BFFF,
        description=":pushpin:  Esses comandos só funcionam se executados por pessoas autorizadas.\n"
                    "\n"
                    "**COMANDOS:**\n"
                    "\n"
                    ":x: :  **!delete** - Limpe o chat\n"
                    "Esse comando deleta um número de mensagens do chat em que ele for executado.\n"
                    "Digite `!delete <numero de 1 a 100>` para deletar as mensagens.\n"
                    "*O comando digitado por você já será automaticamente deletado.\n"
                    "\n"
                    ":loudspeaker: :  **!say** - Mande algum aviso\n"
                    "Digite `!say <mensagem>` para que o bot fale por você.\n"
                    "\n"
                    ":video_game: :  **!jogando** - Altere o status do bot\n"
                    "Digite `!jogando <mensagem>` para que o bot fique com esse status.\n"
                    "\n"
                    ":hammer: :  **!punir** - Alguém infringiu as regras?\n"
                    "Digite `!punir (usuário)` para acessar as opções de punição (ban, kick, mute).\n"
                    "Comando em **DESENVOLVIMENTO** - Ainda não funcional.\n"
                    "\n"
                    ":performing_arts: :  **!status** - Altere o meu status\n"
                    "Selecione o meu status como **ausente** ou **online**.\n"
                    "\n"
                    ":gear: :  **!dev** - Funções do desenvolvedor.\n"
                    "Ignore, você não vai precisar usar isso. O que será que tem aqui?\n"
                    "\n"
                    "Esses são os comandos exclusivos.\n"
                    "**Cheddar BOT - Modo admin.**"
)


chat_filter = ["CU", "CÚ", "CARALHO", "BOSTA", "PUTA", "LIXO", "MERDA", "ARROMBADO", "KRL", "CRL", "FDP", "VSF", "FODE", "FODA-SE", "FODASE", "FODASSE", "FODACE", "FDS", "VADIA", "PORRA", "POHA", "FUDER", "FUDE"]
bypass_list = ["388654625693368331", "430095009614921729"]


@client.event
async def on_message(message):
    if message.content.lower().startswith("!biografia"):
        embed = discord.Embed(title="Quem sou eu?", description="Sou um queijo. Não qualquer tipo de queijo. O melhor tipo de queijo.\nDiga não ao presunto. Também não confie em mussarela, eles não dizem a verdade...", color=0x4BF085)
        embed.set_thumbnail(url='https://i.imgur.com/fGo6HFq.png')
        embed.set_footer(text="- Atenciosamente, Sr Cheese 🧀")
        await client.send_message(message.channel, embed=embed)


    if message.content.lower().startswith('!cheddar'):
        await client.send_message(message.channel, "Eu mesmo!\n***Agora na versão 2.5.8***  :cheese:")

    if message.content.lower().startswith('!moeda'):
        escolha1 = random.randint(1, 2)
        if escolha1 == 1:
            await client.add_reaction(message, '😀')
        if escolha1 == 2:
            await client.add_reaction(message, '👑')


    if message.content.lower().startswith('!dev'):
        if message.author.id == "388654625693368331":  # adicione o seu ID!
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Enviei para você no privado, junto com um nude ( ͡° ͜ʖ ͡°)" % (userID))
            await client.send_message(message.author, "Hey Cheddar:\nLembre-se de desenvolver essa parte.")
        else:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Você não tem permissão para usar esse comando." % (userID))



    if message.content.lower().startswith('!ask '):
        escolha = random.randint(1, 8)
        if escolha == 1:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Sim!" % (userID))
        if escolha == 2:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Não!" % (userID))
        if escolha == 3:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Obviamente não." % (userID))
        if escolha == 4:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Claro que sim." % (userID))
        if escolha == 5:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Hmm, talvez..." % (userID))
        if escolha == 6:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Eu diria que sim." % (userID))
        if escolha == 7:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Creio que não." % (userID))
        if escolha == 8:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Será? :thinking:" % (userID))


    if message.content.lower().startswith('beibe beibe do beibe do biruleibe leibe?'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Ah vai te toma no cu rapa" % (userID))


    if message.content.lower().startswith("!help"):
        await client.send_message(message.channel, embed=help)


    if message.content.lower().startswith("!ajuda"):
        await client.send_message(message.channel, embed=help)


    if message.content.lower().startswith("!admin"):
        if message.author.server_permissions.administrator:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Enviei para você no privado." % (userID))
            await client.send_message(message.author, embed=admin)
        else:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> Você não tem permissão para usar esse comando." % (userID))


    if message.content.lower().startswith('!say'):
        if message.author.server_permissions.administrator:
            await client.delete_message(message)
            args = message.content.split(" ")
            #args[0] = !SAY
            #args[1] = Hey
            #args[2] = There
            #args[1:] = Hey There
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))



    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    userID = message.author.id
                    await client.send_message(message.author, "<@%s> **Hey!** Procure ser educado, sem palavras de baixo calão." % (userID))
                except discord.errors.NotFound:
                    return
                except discord.errors.Forbidden:
                    return



    if message.content.lower().startswith('!sugerir '):
            await client.delete_message(message)
            userID = message.author.id
            await client.send_message(message.channel, "<@%s> **Sua sugestão foi enviada!** :bulb:\nObrigado por contribuir com suas ideias.\nIremos analisar sua sugestão o quanto antes." % (userID))
            args = message.content.split(" ")
            # args[0] = !SAY
            # args[1] = Hey
            # args[2] = There
            # args[1:] = Hey There
            canal2 = client.get_channel("431925429037957141")
            msg_author = message.author.mention
            await client.send_message(canal2, ":small_orange_diamond: **Nova sugestão:**\n\nSugestão: `%s`\nEnviada por: {}\n\n**Você apoia essa sugestão?**".format(msg_author) % (" ".join(args[1:])))


    if message.channel.id == "431925429037957141":
        if message.author.id == "430095009614921729":
            await client.add_reaction(message, '👍')
            await client.add_reaction(message, '👎')



    if message.channel.id == "424724808811675648":
        await client.add_reaction(message, '👍🏻')
        await client.add_reaction(message, '👍🏼')
        await client.add_reaction(message, '👍🏽')
        await client.add_reaction(message, '👍🏾')
        await client.add_reaction(message, '👍🏿')

    if message.content.startswith('!jogando') and message.author.id == message.author.server_permissions.administrator:
        game = message.content[8:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, "Mudando o status para: " + game + "")



    if message.content.lower().startswith('!delete') and message.author.id == message.author.server_permissions.administrator:
        try:
            qntdd = message.content.strip('!delete ')
            qntdd = toint(qntdd)
            if qntdd <= 100:
                msg_author = message.author.mention
                await client.delete_message(message)
                #await asyncio.sleep(1)
                deleted = await client.purge_from(message.channel, limit=qntdd)
                botmsgdelete = await client.send_message(message.channel, '{} Deletei **{}** mensagens com sucesso!\n*Essa mensagem será removida automaticamente em 5 segundos.*'.format(msg_author, len(deleted)))
                await asyncio.sleep(5)
                await client.delete_message(botmsgdelete)

            else:
                await client.delete_message(message)
                msg_author = message.author.mention
                botmsgdelete = await client.send_message(message.channel,'{} Utilize o comando digitando `!delete <numero de 1 a 100>`\n*Essa mensagem será removida automaticamente em 5 segundos.*'.format(msg_author))
                await asyncio.sleep(5)
                await client.delete_message(botmsgdelete)
        except:
            return



    if message.content.lower().startswith('!punir') and message.author.id == message.author.server_permissions.administrator:
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> ***Como aplicar uma punição:***\n- !ban <usuário>\n- !mute <usuário>**\n- !unmute <usuário>\n" % (userID))


    if message.content.lower().startswith('!ping'):
        timep = time.time()
        emb = discord.Embed(title='Aguarde...', color=0x565656)
        pingm0 = await client.send_message(message.channel, embed=emb)
        ping = time.time() - timep
        msg_author = message.author.mention
        pingm1 = discord.Embed(title='Pong!', description=':ping_pong:  {}\nPing - %.01f segundos'.format(msg_author) % ping, color=0xFFFF00)
        await client.edit_message(pingm0, embed=pingm1)


    if message.content.lower().startswith('!img'):
        embed = discord.Embed(color=0x9910CD)
        embed.set_image(url="https://i.imgur.com/cCDKElp.png")
        await client.send_message(message.channel, "{}".format(message.author.mention))
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith("!ban"):
        try:
            # Vai verificar se quem usou o comando tem permissão de adm
            if not message.author.server_permissions.administrator:
                userID = message.author.id
                return await client.send_message(message.channel, '<@%s> ⚠️Permissão insuficiente' % (userID))
            author = message.author.mention
            user = message.mentions[0]
            await client.ban(user)
            await client.send_message(message.channel, ":no_entry_sign: -  ***Jogador banido!***\n\nO usuário {} foi banido!\nBanido por: {}".format(user.mention,
                                                                                                   author))
        # no caso do membro mencionado ser um adm vai enviar uma messagem
        except discord.errors.Forbidden:
            return await client.send_message(message.channel, '{} ⚠️ Não posso banir esse membro: {}'.format(author,user.mention))



    if message.content.lower().startswith("!mute"):
        # vai verificar se quem usou o comando possui permissão de adm
        if not message.author.server_permissions.administrator:
            userID = message.author.id
            return await client.send_message(message.channel, '<@%s> ⚠️ Permissão insuficiente' % (userID))
        author = message.author.mention
        user = message.mentions[0]
        """Lembrando que tem que ter o cargo mutado no seu server"""
        cargo = discord.utils.get(message.author.server.roles, name='Muted')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel,
                                 ':zipper_mouth: -  ***Jogador mutado!***\n\nO usuário {} foi mutado!\nSilenciado por: {}'.format(user.mention, author))

    if message.content.lower().startswith("!unmute"):
        # vai verificar se quem usou o comando possui permissão de adm
        if not message.author.server_permissions.administrator:
            userID = message.author.id
            return await client.send_message(message.channel, '<@%s> ⚠️ Permissão insuficiente' % (userID))
        author = message.author.mention
        user = message.mentions[0]
        """Lembrando que tem que ter o cargo mutado no seu server"""
        cargo = discord.utils.get(message.author.server.roles, name='Muted')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel,
                                  ':speaking_head: -  ***Jogador desmutado!***\n\nO usuário {} foi desmutado!\nSilenciamento removido por: {}'.format(user.mention, author))

    if message.content.lower().startswith("!status") and message.author.server_permissions.administrator:
        embed6 = discord.Embed(
            title="Altere o meu status:",
            color=0x690FC3,
            description="📗 : **Online**\n"
                        "Use `!s online`\n"
                        "\n"
                        "📒 : **Ausente**\n"
                        "Use `!s ausente`", )
        embed6.set_footer(text="*Pode demorar alguns instantes.")
        embed6.set_thumbnail(url="https://i.imgur.com/fGo6HFq.png")
        await client.send_message(message.channel, embed=embed6)

    if message.content.lower().startswith("!s online") and message.author.server_permissions.administrator:
        embed4 = discord.Embed(
            title="Status alterado!",
            color=0x690FC3,
            description="📗 : **Online**\n"
                        "\n"
                        "Agora eu estou online!", )
        embed4.set_footer(text="Use !status para alterar o status")
        embed4.set_thumbnail(url="https://i.imgur.com/fGo6HFq.png")
        await client.change_presence(status=discord.Status("online"))
        await client.send_message(message.channel, embed=embed4)

    if message.content.lower().startswith("!s ausente") and message.author.server_permissions.administrator:
        embed5 = discord.Embed(
            title="Status alterado!",
            color=0x690FC3,
            description="📒 : **Ausente**\n"
                        "\n"
                        "Agora eu estou ausente!", )
        embed5.set_footer(text="Use !status para alterar o status")
        embed5.set_thumbnail(url="https://i.imgur.com/fGo6HFq.png")
        await client.change_presence(status=discord.Status("idle"))
        await client.send_message(message.channel, embed=embed5)

    if message.content.startswith('!info'):
        try:
            user = message.mentions[0]
            userjoinedat = str(user.joined_at).split('.', 1)[0]
            usercreatedat = str(user.created_at).split('.', 1)[0]

            userembed = discord.Embed(
                title="Usuário:",
                description=user.name,
                color=0xe67e22
            )
            userembed.set_author(
                name="Informações do usuário:",
                icon_url="http://www.artmarketdeanmore.com/wp-content/uploads/2015/08/info-logo.png"
            )
            userembed.add_field(
                name="Entrou no servidor em:",
                value=userjoinedat
            )
            userembed.add_field(
                name="Conta criada em:",
                value=usercreatedat
            )
            userembed.add_field(
                name="Tag do Discord:",
                value=user.discriminator
            )
            userembed.add_field(
                name="ID do usuário:",
                value=user.id
            )

            await client.send_message(message.channel, embed=userembed)
        except IndexError:
            await client.send_message(message.channel, "{} Informe um usuário válido.".format(message.author.mention))
        except:
            await client.send_message(message.channel, "{} Algo deu errado ao executar esse comando :/".format(message.author.mention))
        finally:
            pass


@client.event
async def on_member_join(member):
  canal = client.get_channel("431600744383250432")
  regras = client.get_channel("424722034761793550")
  msg = ":inbox_tray:  {} => **Entrou no servidor!**\nSeja bem-vindo! - Recomendamos que leia as {} atentamente.".format(member.mention, regras.mention)
  msg2 = "```HTTP\nBem-vindo ao Servidor de Testes!\n```\nOlá {}!\n**Obrigado por entrar no servidor.**\n:small_orange_diamond: Leia as regras e divirta-se.\n:small_orange_diamond: Convide seus amigos também.\n\n**Abraço do Cheddinha**".format(member.mention)
  await client.send_message(canal, msg) #substitua canal por member para enviar a msg no DM do membro
  try:
      await client.send_message(member, msg2)
  except:
      return

@client.event
async def on_member_remove(member):
   canal = client.get_channel("431600744383250432")
   msg = ":outbox_tray:  {} => **Saiu do servidor!**\nTchau, até mais!".format(member.mention)
   await client.send_message(canal, msg) #substitua canal por member para enviar a msg no DM do membro



@client.event
async def on_member_ban(user):
    #canal que vai mandar: (pode alterar se quiser)
    channel = discord.utils.find(lambda c: c.name == 'banimentos', user.server.channels)
    #O embed: (troque a mensagem pelo que quiser, só não apague o "{0.name}, nem o .format
    embed = discord.Embed(title='Botão do ban acionado!', description='Algum moderador baniu **@{0.name}** do servidor.\n\nA tecla do ban foi apertada com sucesso.'.format(user), color=0xFA5858)
    #Para exibir o gif: (se quiser apagar é escolha sua
    embed.set_image(url='https://media.tenor.com/images/da66a96ca7f65f949a07db8ab9926297/tenor.gif')
    #Manda a mensagem no canal
    await client.send_message(channel, embed=embed)



client.run(TOKEN)