import discord
import youtube_dl
from discord.ext import commands



TOKEN = open('api.key','r').readline().rstrip()
client = commands.Bot(command_prefix=commands.when_mentioned_or('!'))
extensions = ['MusicCommands']


@client.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(client.user))

# @client.command(pass_context=True)
# async def play(ctx, url):
#     server = ctx.message.server
#     print(url)
#     voice_client = client.voice_client_in(server)
#     player = await voice_client.create_ytdl_player(url)
#     players[server.id] = player
#     player.start()

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. [{}]'.format(extensions, error))
    client.run(TOKEN)
