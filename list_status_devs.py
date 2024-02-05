import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.presences = True
intents.messages = True
intents.guilds = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.command(name='status_team')
async def status_team(ctx):
    # Verifica se o comando foi enviado em um servidor (guild)
    if ctx.guild:
        # Verifica se o autor do comando possui o cargo 'Lead'
        if discord.utils.get(ctx.author.roles, name='Lead'):
            # Obtém o cargo 'Devs' do servidor
            cargo_devs = discord.utils.get(ctx.guild.roles, name='Devs')

            if cargo_devs:
                # Filtra os membros que possuem o cargo 'Devs'
                membros_devs = [membro for membro in ctx.guild.members if cargo_devs in membro.roles]

                # Cria uma mensagem com o status de cada membro
                mensagem = '\n'.join([f"{membro.display_name}: {membro.activity.name if membro.activity else 'Nenhum status'}" for membro in membros_devs])

                await ctx.send(f"**Status dos Devs:**\n{mensagem}")
            else:
                await ctx.send("Cargo 'Devs' não encontrado.")
        else:
            await ctx.send("Você não tem permissão para executar este comando.")
    else:
        await ctx.send("Este comando só pode ser executado em um servidor (guild).")

# Substitua 'TOKEN' pelo token real do seu bot
bot.run('TOKEN')