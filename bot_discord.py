import os
import discord
import google.generativeai as genai
from dotenv import load_dotenv
import config
import asyncio

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GENAI_KEY = os.getenv("GEMINI_API_KEY")

#genai.configure(api_key=GENAI_KEY)
genai.configure(api_key=GENAI_KEY, transport="rest")
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Configuration de l'agent à utilier
model = genai.GenerativeModel(
    model_name='gemini-flash-latest',
    system_instruction=config.INSTRUCTIONS_SYSTEME
)

@client.event
async def on_ready():
    print(f"L'agent {config.NOM_DU_BOT} est en ligne sur Discord !")

@client.event
async def on_message(message):
    if message.author == client.user: return

    try:
        async with message.channel.typing():
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                lambda: model.generate_content(message.content)
            )
            texte_ia = response.text
        
            if len(texte_ia) > 2000:
                texte_ia = texte_ia[:1900] + "..."
            await message.reply(texte_ia)
    except Exception as e:
        print(f"Erreur : {e}")

client.run(DISCORD_TOKEN)
