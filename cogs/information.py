from nextcord.ext import commands
from nextcord import Interaction, slash_command

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="info", description="Obtener informacion sobre Destiny.")
    async def info(self, interaction: Interaction):
        try:
            message ="👋🏻¡Bienvenido a nuestra tienda de **Amino Coins** y **Proxys**! \n\nAquí encontrarás productos de **alta** calidad 🌟 a precios competitivos 💵. \n\n🤝🏻¡Únete a nosotros hoy y experimenta la diferencia en calidad, precio y servicio!\n\n Dirígete a 👉🏻#bienvenido para empezar!"

            await interaction.send(ephemeral=True, content=message)

        except Exception as e:
            print(f"Error during showing info: {e}")
            await interaction.send(ephemeral=True, content='An error occurred while showing info /info!')

def setup(bot):
    bot.add_cog(Information(bot))
