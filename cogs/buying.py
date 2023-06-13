import nextcord
from nextcord.ext import commands
from nextcord.utils import get
from config import CHANNEL_LINK, AMINO_COINS, SCRIPTS, SUPPORT


class Buying(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.existing_channels = []

    async def create_text_channel(self, interaction: nextcord.Interaction, product):
        # Fetching channels with the same name
        for channel in interaction.guild.channels:
            if str(interaction.user.id) in channel.name:
                await interaction.send(ephemeral=True, content=f"Dirígete a 👉🏻{CHANNEL_LINK}{channel.id} para continuar!", delete_after=10)
                return

        # Check if the "ticket" category exists, otherwise create it
        category_name = "tickets"
        category = get(interaction.guild.categories, name=category_name)

        if not category:
            category = await interaction.guild.create_category(category_name)

        # Create the new channel with the name of the user who clicked
        text_channel = await interaction.guild.create_text_channel(
            name=f"{interaction.user.name}-ticket-{interaction.user.id}",
            topic='En este canal puedes contactarte con el vendedor. 😁',
            overwrites={
                interaction.guild.default_role: nextcord.PermissionOverwrite(
                    view_channel=False
                ),
                interaction.user: nextcord.PermissionOverwrite(
                    view_channel=True,
                    read_messages=True,
                    send_messages=True
                )
            },
            category=category
        )

        # # Add the new channel to the list of existing channels
        # self.existing_channels.append({
        #     'user_id': interaction.user.id,
        #     'channel_id': text_channel.id
        # })

        gretting_embed = nextcord.Embed(title=product.upper(
        ), color=0x99231a, description=f"Hola {interaction.user.name} 👋🏻\nPronto un moderador se pondrá en contacto contigo!")

        prices_embed = nextcord.Embed(title='Precios 🎟️', color=0x99231a,
                                      description='Precios de Amino Coins | Pago en dolar (USD) 💵')
        prices_embed.add_field(name='200K 🪙', value="1.2 USD")
        prices_embed.add_field(name='500K 🪙', value="2.5 USD")
        prices_embed.add_field(name='1M 🪙', value="5 USD")
        prices_embed.add_field(name='2M 🪙', value="10 USD")
        prices_embed.add_field(name='3M 🪙', value="15 USD")
        prices_embed.add_field(name='5M 🪙', value="25 USD")
        prices_embed.add_field(name='6M 🪙', value="30 USD")
        prices_embed.add_field(name='10M 🪙', value="50 USD")
        prices_embed.add_field(name='20M 🪙', value="100 USD")
        prices_embed.add_field(name='40M 🪙', value="150 USD")
        prices_embed.add_field(name='80M 🪙', value="300 USD")
        prices_embed.add_field(name='100M 🪙', value="400 USD")
        prices_embed.set_footer(
            text='Si tienes preguntas no dudes en consultar! 😁')

        # Inform the user that the channel has been created successfully on the new channel
        if (product == AMINO_COINS):
            await text_channel.send(embeds=[gretting_embed, prices_embed])
        else:
            await text_channel.send(embed=gretting_embed)


def setup(bot):
    bot.add_cog(Buying(bot))
