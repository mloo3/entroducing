import discord
from discord.ext import commands

players = {}

class MusicCommands:
    def __init__(self, client):
        self.client = client
    
    def _createEmbed(self, description, colour=0xDEADBF):
        return discord.Embed(description=description, colour=colour)

    @commands.command(pass_context=True, no_pm=True)
    async def join(self, ctx):
        """Bot joins the channel you are currently in."""
        try:
            channel = ctx.message.author.voice.voice_channel
            await self.client.join_voice_channel(channel)
        except discord.InvalidArgument:
            await self.client.send_message(ctx.message.channel, 
                    embed=self._createEmbed("Get the fuck in a voice channel"))
        except discord.ClientException:
            await self.client.send_message(ctx.message.channel, 
                    embed=self._createEmbed("????\nGet to the over one"))
        else:
            await self.client.send_message(ctx.message.channel, 
                    embed=self._createEmbed(("Waz poppin {}".format(channel.name))))

    @commands.command(pass_context=True, no_pm=True)
    async def leave(self, ctx):
        """Bot leaves the current channel"""
        try:
            server = ctx.message.server
            voice_client = self.client.voice_client_in(server)
            await voice_client.disconnect()
        except Exception:
            await self.client.send_message(ctx.message.channel,
                    embed=self._createEmbed("dont hate me cuz you aint me"))
        else:
            await self.client.send_message(ctx.message.channel,
                    embed=self._createEmbed("I'm out"))

    @commands.command(pass_context=True, no_pm=True)
    async def play(self, ctx, *, song):
    # async def play(self, ctx, url):
        """Plays a song.
        Joins channel if bot is not in voice channel
        """
        options = {
            'default_search': 'auto',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }],
            # 'quiet': True,
        }
        server = ctx.message.server
        voice_client = self.client.voice_client_in(server)
        # try to connect if not already in voice channel
        if not voice_client: 
            try_join = await ctx.invoke(self.join)

            server = ctx.message.server
            voice_client = self.client.voice_client_in(server)
            # if not voice_client:
            #     return

        player = await voice_client.create_ytdl_player(song, ytdl_options=options)
        # players[server.id] = player
        player.start()

    # @commands.command(pass_context=True, no_pm=True)
    # @commands.command(pass_context=True, no_pm=True)
    # @commands.command(pass_context=True, no_pm=True)
    # @commands.command(pass_context=True, no_pm=True)
    # @commands.command(pass_context=True, no_pm=True)


def setup(client):
    client.add_cog(MusicCommands(client))
