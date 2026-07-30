import asyncio
import logging
import discord
from discord.ext import commands
from .. import config
from ..game import MOTS_THEMES

logger = logging.getLogger(__name__)


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
            logger.error("on_message: %s", e)

    @discord.app_commands.command(name="play", description="Commence une nouvelle partie")
    async def play(self, interaction: discord.Interaction):
        await interaction.response.defer()
        session = self.bot.games.new_game(interaction.channel_id)
        logger.info("Nouvelle partie channel=%d theme=%s mot=%s", interaction.channel_id, session.theme, session.secret_word)
        try:
            texte = await self._ask_ai(
                interaction.channel_id,
                f"Le joueur a lancé /play. Le mot secret de cette partie est : {session.secret_word}. "
                f"Ne le révèle jamais directement. Donne le premier indice.",
            )
            await interaction.followup.send(
                f"🎯 Nouvelle partie ! Thème : **{session.theme}**\n{texte}"
            )
        except Exception as e:
            logger.error("play: %s", e)
            await interaction.followup.send("❌ Erreur lors du lancement de la partie.")

    @discord.app_commands.command(name="guess", description="Propose un mot")
    async def guess(self, interaction: discord.Interaction, mot: str):
        await interaction.response.defer()
        session = self.bot.games.get_or_create(interaction.channel_id)
        if not session.secret_word:
            await interaction.followup.send("Aucune partie en cours. Lance `/play` pour commencer.")
            return
        correct, mot_trouve = self.bot.games.check_guess(interaction.channel_id, mot)
        if correct:
            await self._ask_ai(
                interaction.channel_id,
                f"Bravo ! Le joueur a trouvé le mot secret : {mot_trouve}. "
                f"Félicite-le chaleureusement et proposer de refaire une partie.",
            )
            await interaction.followup.send(
                f"🎉 **Trouvé !** Le mot était **{mot_trouve}**. "
                f"Tu gagnes **{session.score} points** ! "
                f"Utilise `/play` pour recommencer."
            )
        else:
            texte = await self._ask_ai(
                interaction.channel_id,
                f"Le joueur a proposé : {mot}. Ce n'est pas le mot secret. "
                f"Dis-lui que c'est faux avec humour et donne un nouvel indice.",
            )
            await interaction.followup.send(f"❌ Non, ce n'est pas **{mot}**.\n{texte}")

    @discord.app_commands.command(name="indice", description="Demande un indice supplémentaire")
    async def indice(self, interaction: discord.Interaction):
        await interaction.response.defer()
        session = self.bot.games.get_or_create(interaction.channel_id)
        if not session.secret_word:
            await interaction.followup.send("Aucune partie en cours. Lance `/play` pour commencer.")
            return
        session.hints_given += 1
        try:
            texte = await self._ask_ai(
                interaction.channel_id,
                "Donne un indice supplémentaire sur le mot secret (sans le révéler).",
            )
            await interaction.followup.send(f"💡 Indice #{session.hints_given} :\n{texte}")
        except Exception as e:
            logger.error("indice: %s", e)
            await interaction.followup.send("❌ Erreur lors de la demande d'indice.")

    @discord.app_commands.command(name="abandonner", description="Abandonne et révèle le mot secret")
    async def abandonner(self, interaction: discord.Interaction):
        await interaction.response.defer()
        session = self.bot.games.get_or_create(interaction.channel_id)
        if not session.secret_word:
            await interaction.followup.send("Aucune partie en cours. Lance `/play` pour commencer.")
            return
        mot = session.secret_word
        self.bot.games.reset(interaction.channel_id)
        try:
            await self._ask_ai(
                interaction.channel_id,
                f"Le joueur a abandonné. Le mot secret était : {mot}. "
                f"Dis-lui la réponse et propose de refaire une partie.",
            )
            await interaction.followup.send(
                f"😔 Dommage ! Le mot secret était **{mot}**. "
                f"Utilise `/play` pour retenter ta chance."
            )
        except Exception as e:
            logger.error("abandonner: %s", e)
            await interaction.followup.send(f"😔 Le mot secret était **{mot}**.")

    @guess.autocomplete("mot")
    async def mot_autocomplete(self, interaction: discord.Interaction, current: str):
        session = self.bot.games.get_or_create(interaction.channel_id)
        theme = session.theme or "animaux"
        mots = MOTS_THEMES.get(theme, [])
        return [
            discord.app_commands.Choice(name=m, value=m)
            for m in mots if current.lower() in m.lower()
        ][:5]
