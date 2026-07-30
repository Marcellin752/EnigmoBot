from dataclasses import dataclass, field


@dataclass
class GameSession:
    channel_id: int
    active: bool = False
    attempts: int = 0
    hints_given: int = 0


class GameManager:
    def __init__(self):
        self._sessions: dict[int, GameSession] = {}

    def get_or_create(self, channel_id: int) -> GameSession:
        if channel_id not in self._sessions:
            self._sessions[channel_id] = GameSession(channel_id=channel_id)
        return self._sessions[channel_id]

    def reset(self, channel_id: int):
        if channel_id in self._sessions:
            del self._sessions[channel_id]
