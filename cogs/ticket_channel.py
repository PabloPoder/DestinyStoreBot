import datetime
import asyncio
from nextcord import slash_command, Interaction
from nextcord.ext import commands
import nextcord
from cogs.buying import Buying

from config import DISCORD_SERVER_TOKEN


class TicketChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.sleep_task = None

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     # Get the channel text
    #     text_channel = message.channel

    #     # Verifying if the channel contains the keyword "ticket" in its name
    #     if "ticket" in text_channel.name.lower():
    #         # Cancel the previous sleep task, if any
    #         if self.sleep_task is not None:
    #             self.sleep_task.cancel()

    #         # Start a new sleep task for 5 minutes
    #         self.sleep_task = asyncio.create_task(asyncio.sleep(330))

    #         try:
    #             # Wait for 5 minutes
    #             await self.sleep_task

    #             # Get the date of the last message
    #             last_message_time = text_channel.last_message.created_at

    #             # Calculate the time difference from the last message to now
    #             current_time = datetime.datetime.now(datetime.timezone.utc)
    #             time_difference = (
    #                 current_time - last_message_time).total_seconds() / 60
    #             print(time_difference)

    #             # Check if the channel is idle for more than a certain period of time (for example, 5 minutes)
    #             if time_difference >= 5:
    #                 print(
    #                     f"El canal {text_channel.name} ha sido borrado debido a inactividad.")
    #                 await text_channel.delete()
    #             else:
    #                 print(f"El canal {text_channel.name} está activo.")
    #         except asyncio.CancelledError:
    #             # The sleep task was cancelled, do nothing
    #             pass

    #     # Continue with normal message processing
    #     await self.bot.process_commands(message)

    @slash_command(name="delete_tickets", description="Borrar canales ticket inactivos.", guild_ids=[DISCORD_SERVER_TOKEN], default_member_permissions=0)
    @commands.has_permissions(administrator=True)
    async def delete_tickets(self, interaction: Interaction):
        await interaction.response.defer()

        channels = interaction.guild.text_channels
        deleted_channels = []

        for channel in channels:
            try:
                if "ticket" in channel.name.lower():
                    deleted_channels.append(channel.name)
                    channel.delete()
                    # if channel.last_message is None:
                    #     print(
                    #         f"El canal {channel.name} ha sido borrado debido a inactividad.")
                    #     deleted_channels.append(channel.name)
                    #     await channel.delete()
                    # else:
                    #     last_message_time = channel.last_message.created_at
                    #     current_time = datetime.datetime.now(
                    #         datetime.timezone.utc)
                    #     time_difference = (
                    #         current_time - last_message_time).total_seconds() / 60

                    #     if time_difference >= 5:
                    #         print(
                    #             f"El canal {channel.name} ha sido borrado debido a inactividad.")
                    #         await channel.delete()
                    #         deleted_channels.append(channel.name)

            except (nextcord.Forbidden, nextcord.NotFound) as e:
                print(f"Can't access channel {channel.name}: {e}")
            except Exception as e:
                print(f"Error deleting channel: {e}")
                await interaction.followup.send(ephemeral=True, content="¡Se produjo un error al mostrar la información!")

        if deleted_channels:
            await interaction.followup.send(ephemeral=True, content="Canales eliminados: " + ", ".join(deleted_channels), delete_after=10)
        else:
            await interaction.followup.send(ephemeral=True, content="No se eliminaron canales.", delete_after=10)


def setup(bot):
    bot.add_cog(TicketChannel(bot))
