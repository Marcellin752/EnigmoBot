from google import genai
from google.genai import types
from . import config


class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=config.GEMINI_API_KEY)
        self._sessions: dict[int, genai.chats.Chat] = {}

    def get_or_create_session(self, channel_id: int):
        if channel_id not in self._sessions:
            self._sessions[channel_id] = self.client.chats.create(
                model="gemini-2.5-flash",
                config=types.GenerateContentConfig(
                    system_instruction=config.INSTRUCTIONS_SYSTEME
                )
            )
        return self._sessions[channel_id]

    def send_message(self, channel_id: int, content: str) -> str:
        session = self.get_or_create_session(channel_id)
        response = session.send_message(content)
        return response.text
