import asyncio
import discord
from discord.ext import commands
from .. import config


class GameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def _ask_ai(self, channel_id: int, content: str) -> str:
        loop = asyncio.get_running_loop()
        response = await loop.run_in_executor(
            None,
            lambda: self.bot.ai.send_message(channel_id, content)
        )
        if len(response) > 2000:
            response = response[:1900] + "..."
        return response

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        try:
            async with message.channel.typing():
                texte = await self._ask_ai(message.channel.id, message.content)
            await message.reply(texte)
        except Exception as e:
            print(f"Erreur on_message : {e}")

    @discord.app_commands.command(name="play", description="Commence une nouvelle partie")
    async def play(self, interaction: discord.Interaction):
        await interaction.response.defer()
        self.bot.games.reset(interaction.channel_id)
        try:
            texte = await self._ask_ai(
                interaction.channel_id,
                "Nouvelle partie ! Choisis un mot secret et donne le premier indice."
            )
            await interaction.followup.send(texte)
        except Exception as e:
            print(f"Erreur play : {e}")
            await interaction.followup.send("❌ Erreur lors du lancement de la partie.")

    @discord.app_commands.command(name="guess", description="Propose un mot")
    async def guess(self, interaction: discord.Interaction, mot: str):
        await interaction.response.defer()
        try:
            texte = await self._ask_ai(
                interaction.channel_id,
                f"Le joueur propose le mot: {mot}. Est-ce la bonne réponse ?"
            )
            await interaction.followup.send(texte)
        except Exception as e:
            print(f"Erreur guess : {e}")
            await interaction.followup.send("❌ Erreur lors de la vérification.")

    @discord.app_commands.command(name="indice", description="Demande un indice supplémentaire")
    async def indice(self, interaction: discord.Interaction):
        await interaction.response.defer()
        try:
            texte = await self._ask_ai(
                interaction.channel_id,
                "Donne un indice supplémentaire sur le mot secret."
            )
            await interaction.followup.send(texte)
        except Exception as e:
            print(f"Erreur indice : {e}")
            await interaction.followup.send("❌ Erreur lors de la demande d'indice.")

    @discord.app_commands.command(name="abandonner", description="Abandonne et révèle le mot secret")
    async def abandonner(self, interaction: discord.Interaction):
        await interaction.response.defer()
        try:
            texte = await self._ask_ai(
                interaction.channel_id,
                "Le joueur abandonne. Révèle le mot secret et propose de recommencer."
            )
            self.bot.games.reset(interaction.channel_id)
            await interaction.followup.send(texte)
        except Exception as e:
            print(f"Erreur abandonner : {e}")
            await interaction.followup.send("❌ Erreur lors de l'abandon.")
