import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Emote de "belezinha"
EMOJI_DESEJADA = '\U0001F44D'

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.event
async def on_reaction_add(reaction, user):
    # Verifica se o autor da reação não é o bot
    if user.bot:
        return

    # Verifica se a reação é da emoji desejada
    if str(reaction.emoji) == EMOJI_DESEJADA:
        # Obtém o ID da mensagem que recebeu a reação
        mensagem_id = reaction.message.id
        
        # Obtém o texto da mensagem e define como status
        texto_status = reaction.message.content
        await bot.change_presence(activity=discord.Game(name=f"Trabalhando em: {texto_status}"))

# Executa o bot (substitua 'TOKEN' pelo token real do seu bot)
bot.run('TOKEN')