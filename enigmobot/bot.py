import asyncio
import logging
import discord
from discord.ext import commands
from . import config
from .ai import GeminiClient
from .game import GameManager

logger = logging.getLogger(__name__)


class EnigmoBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        self.ai = GeminiClient()
        self.games = GameManager()

    async def setup_hook(self):
        from .cogs.commands import GameCog
        await self.add_cog(GameCog(self))
        await self.tree.sync()

    async def on_ready(self):
        logger.info("Agent %s en ligne sur %d serveur(s) !", config.NOM_DU_BOT, len(self.guilds))
        await self.change_presence(activity=discord.Game(name="Jeu du mot secret"))

    async def close(self):
        logger.info("Arrêt du bot %s", config.NOM_DU_BOT)
        await super().close()
