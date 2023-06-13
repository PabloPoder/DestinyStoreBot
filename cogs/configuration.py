import nextcord
from nextcord.ext import commands
from nextcord import Interaction, slash_command
from nextcord import File
from cogs.buying import Buying
from cogs.ui.buttons import MyView

from config import DISCORD_SERVER_TOKEN, CHANNEL_LINK, AMINO_PROFILE_URL, TWITTER_URL


class Configuration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @slash_command(name='setup', description='This command will configure the bot in your server', guild_ids=[DISCORD_SERVER_TOKEN], default_member_permissions=0)
    @commands.has_permissions(administrator=True)
    async def setup(self, interaction: Interaction):
        try:
            if interaction.guild is not None:
                # Creating channels
                welcome_channel = await interaction.guild.create_text_channel(
                    name='bienvenido',
                    topic='En este canal podrás ver información útil sobre el servidor 📜.',
                    overwrites={interaction.guild.default_role: nextcord.PermissionOverwrite(
                            send_messages=False, add_reactions=False
                        ),
                    }
                )
                
                buy_channel = await interaction.guild.create_text_channel(
                    name='comprar',
                    topic='En este canal podrás hacer tus compras 🛒 mediante el uso de Destiny bot 🤖.',
                    overwrites={interaction.guild.default_role: nextcord.PermissionOverwrite(
                            send_messages=False, add_reactions=False
                        ),
                    }
                )

                # Getting link for easy accessibility to the buy channel
                buy_channel_link = f'{CHANNEL_LINK}{buy_channel.id}'

                # Show info in welcome-channel
                banner_image = File("images/destiny_banner.webp", filename="destiny_banner.webp")
                
                await welcome_channel.send(file=banner_image)
                welcome_channel_message = (
                    "👋🏻 ¡Bienvenido a nuestra tienda de **Amino Coins** y **Proxys**! " +
                    "\n\nAquí encontrarás productos de **alta** calidad 🌟 a precios competitivos 💵. " +
                    "\n\n🤝🏻 ¡Únete a nosotros hoy y experimenta la diferencia en calidad, precio y servicio!" +
                    f"\n\nDirígete a 👉🏻{buy_channel_link} para empezar!"
                )
                await welcome_channel.send(content=welcome_channel_message)
                await welcome_channel.send(content="\n📃 Para más información utiliza el comando _/info_\n")
                rules_message = (
                    "**REGLAS 📜** " +
                    "\n**1. Pórtate bien!** Sé cordial y amable con todas y todos los miembros. " +
                    "\n**2. ¡Sé ordenado!** Usa cada canal para su respectiva temática. " +
                    "\n**3. ¡No spam!** No llenes el Discord de un montón de enlaces ni mensajes repetidos."
                )
                await welcome_channel.send(content=rules_message)

                # Configuration end
                config_message = f'Server configured correctly! 🧩 Check it out 👉🏻{CHANNEL_LINK}{welcome_channel.id}'
                await interaction.send(ephemeral=True, content=config_message)
    
        except Exception as e:
            # Handle the exception
            print(f"Error during server configuration: {e}")
            await interaction.send(ephemeral=True, content='An error occurred while configuring the server! /setup')
            

    @slash_command(name='setup-bot', description='Configure the bot for a specific channel', guild_ids=[DISCORD_SERVER_TOKEN], default_member_permissions=0)
    @commands.has_permissions(administrator=True)
    async def setupBot(self, interaction: Interaction):

        try:
            await interaction.response.defer()
            await interaction.delete_original_message()
            
            channel = interaction.channel

            if isinstance(channel, nextcord.TextChannel):
                banner_image = File("images/destiny_banner.webp", filename="destiny_banner.webp")
                shop_image = File("images/destiny_shop.webp", filename="destiny_shop.webp")

                embed = nextcord.Embed(
                    title="Bienvenido a Destiny",
                    description=f"[Amino]({AMINO_PROFILE_URL}) | [Twitter]({TWITTER_URL}) | [Youtube]({TWITTER_URL})",
                    color=0x99231a,
                )
                embed.set_image(url="attachment://destiny_shop.webp")
                embed.set_footer(text="Mas informacion: /info  ·  @ZOMKLAN")

                # Loading buttons
                view = MyView(interaction, buying_cog= Buying)
                view.buying_cog = Buying(self.bot)

                options_message = "__**\nLista de opciones:**__\n👉🏻 Utiliza los botones 🟩 🟥 🟦 para elegir!"

                await channel.send(file=banner_image)
                await channel.send(
                    options_message,
                    file=shop_image,
                    embed=embed,
                    view=view
                )
                await interaction.send(ephemeral=True, content='Bot configured correctly! 💯', delete_after=10)
            else: 
                await interaction.send(ephemeral=True, content='You must be on a text channel❗', delete_after=10)


        except Exception as e:
            print(f"Bot setup error: {e}")
            await interaction.send(ephemeral=True, content='An error occurred while configuring the bot! /setup_bot')

    


def setup(bot):
    bot.add_cog(Configuration(bot))
