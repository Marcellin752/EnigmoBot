import os
import asyncio
import discord
from dotenv import load_dotenv
from google import genai
from google.genai import types
import config

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

ai_client = genai.Client(api_key=GEMINI_API_KEY)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

chat_session = ai_client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=config.INSTRUCTIONS_SYSTEME
    )
)

@client.event
async def on_ready():
    print(f"L'agent {config.NOM_DU_BOT} est en ligne sur Discord !")

@client.event
async def on_message(message):
    if message.author == client.user: 
        return

    try:
        async with message.channel.typing():
            loop = asyncio.get_event_loop()
            
            response = await loop.run_in_executor(
                None, 
                lambda: chat_session.send_message(message.content)
            )
            texte_ia = response.text
        
            if len(texte_ia) > 2000:
                texte_ia = texte_ia[:1900] + "..."
            await message.reply(texte_ia)
            
    except Exception as e:
        print(f"Erreur : {e}")

client.run(DISCORD_TOKEN)
