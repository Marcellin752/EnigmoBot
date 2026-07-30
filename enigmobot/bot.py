import asyncio
import discord
from . import config
from .ai import GeminiClient
from .game import GameManager


class EnigmoBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.ai = GeminiClient()
        self.games = GameManager()

    async def on_ready(self):
        print(f"L'agent {config.NOM_DU_BOT} est en ligne sur Discord !")

    async def on_message(self, message):
        if message.author == self.user:
            return

        try:
            async with message.channel.typing():
                loop = asyncio.get_event_loop()
                response = await loop.run_in_executor(
                    None,
                    lambda: self.ai.send_message(message.channel.id, message.content)
                )

                if len(response) > 2000:
                    response = response[:1900] + "..."
                await message.reply(response)
        except Exception as e:
            print(f"Erreur : {e}")
