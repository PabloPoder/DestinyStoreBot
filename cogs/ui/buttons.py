import nextcord
from nextcord.ui import View, button
from config import AMINO_COINS, SCRIPTS, SUPPORT

from cogs.buying import Buying


class MyView(View):
    def __init__(self, interaction: nextcord.Interaction, buying_cog: Buying):
        super().__init__()
        self.interaction = interaction
        self.buying_cog = buying_cog
        self.handle_click

    @button(label="🪙 Amino Coins", style=nextcord.ButtonStyle.green)
    async def button1(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.handle_click(interaction, AMINO_COINS, product=AMINO_COINS)


    @button(label="💻 Scripts", style=nextcord.ButtonStyle.danger)
    async def button2(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.handle_click(interaction, SCRIPTS, product=SCRIPTS)



    @button(label="💪🏻 Support", style=nextcord.ButtonStyle.blurple)
    async def button3(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await self.handle_click(interaction, SUPPORT, product=SUPPORT)


    async def handle_click(self, interaction, button_name, product):
        try:
            await interaction.response.defer()
            await self.buying_cog.create_text_channel(interaction, product)
            
        except Exception as e:
            print(f"Error during pressing button Amino Coins: {e}")
            await interaction.send(ephemeral=True, content=f'An error occurred while pressing button {button_name}!')







    