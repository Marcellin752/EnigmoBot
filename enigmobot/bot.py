import asyncio
import discord
from discord.ext import commands
from . import config
from .ai import GeminiClient
from .game import GameManager


class EnigmoBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)
        self.ai = GeminiClient()
        self.games = GameManager()

    async def setup_hook(self):
        from .cogs.game import GameCog
        await self.add_cog(GameCog(self))
        await self.tree.sync()

    async def on_ready(self):
        print(f"L'agent {config.NOM_DU_BOT} est en ligne sur Discord !")
        await self.change_presence(activity=discord.Game(name="🔍 Jeu du mot secret"))
