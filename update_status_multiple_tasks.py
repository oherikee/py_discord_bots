import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.reactions = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Função para configurar o comportamento do bot com base nos parâmetros
def setup_bot(emoji_desejada, status_prefix):
    @bot.event
    async def on_ready():
        print(f'Bot conectado como {bot.user.name}')

    @bot.event
    async def on_reaction_add(reaction, user):
        # Verifica se o autor da reação não é o bot
        if user.bot:
            return

        # Verifica se a reação é da emoji desejada
        if str(reaction.emoji) == emoji_desejada:
            # Obtém o ID da mensagem que recebeu a reação
            mensagem_id = reaction.message.id

            # Obtém o texto da mensagem e define como status
            texto_status = reaction.message.content
            await bot.change_presence(activity=discord.Game(name=f"{status_prefix} {texto_status}"))

# Configuração para a primeira tarefa
setup_bot('\U0001F44C', 'Finalizei o:')

# Configuração para a segunda tarefa
# Limpeza do cache
bot.remove_listener(on_ready)
bot.remove_listener(on_reaction_add)
setup_bot('\U0001F44D', 'Trabalhando em:')

bot.run('TOKEN')
