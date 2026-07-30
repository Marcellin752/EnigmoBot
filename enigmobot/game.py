import random
from dataclasses import dataclass, field
from collections import defaultdict


MOTS_THEMES = {
    "animaux": ["elephant", "girafe", "dauphin", "pingouin", "chameau", "papillon", "ecureuil", "hibou", "crocodile", "panda", "koala", "renard", "loup", "baleine", "fourmi"],
    "objets": ["parapluie", "marteau", "horloge", "miroir", "balancoire", "bougie", "cles", "chapeau", "boussole", "echiquier", "guitare", "cerfvolant", "lunettes", "batte"],
    "nourriture": ["chocolat", "fraise", "fromage", "pizza", "glace", "crepe", "confiture", "miel", "pasteque", "avocat", "lasagnes", "choucroute", "mangue"],
    "nature": ["arcenciel", "volcan", "cascade", "montagne", "foret", "desert", "etoile", "riviere", "tempete", "geyser", "lagune", "aurore", "glacier", "grotte"],
    "sports": ["velo", "escalade", "natation", "football", "tennis", "ski", "plongeon", "flechettes", "surf", "escrime", "badminton", "volleyball"],
    "musique": ["piano", "violon", "guitare", "batterie", "trompette", "harpe", "flute", "saxophone", "accordéon", "ukulele"],
    "metiers": ["pompier", "astronaute", "archeologue", "veterinaire", "detective", "sculpteur", "pilote", "magicien"],
    "transports": ["fusee", "montgolfiere", "sousmarin", "traineau", "helicoptere", "planchevoile", "deltaplane", "voilier"],
}


@dataclass
class GameSession:
    channel_id: int
    user_id: int = 0
    user_name: str = ""
    secret_word: str = ""
    theme: str = ""
    attempts: int = 0
    hints_given: int = 0
    found: bool = False
    score: int = 0

    def points(self) -> int:
        base = 100
        penalty = self.hints_given * 15 + self.attempts * 5
        return max(10, base - penalty)


class GameManager:
    def __init__(self):
        self._sessions: dict[int, GameSession] = {}
        self._player_scores: dict[int, int] = defaultdict(int)

    def get_or_create(self, channel_id: int) -> GameSession:
        if channel_id not in self._sessions:
            self._sessions[channel_id] = GameSession(channel_id=channel_id)
        return self._sessions[channel_id]

    def reset(self, channel_id: int):
        if channel_id in self._sessions:
            del self._sessions[channel_id]

    def new_game(self, channel_id: int, user_id: int = 0, user_name: str = "", theme: str | None = None) -> GameSession:
        if theme and theme not in MOTS_THEMES:
            theme = random.choice(list(MOTS_THEMES.keys()))
        elif not theme:
            theme = random.choice(list(MOTS_THEMES.keys()))
        secret = random.choice(MOTS_THEMES[theme])
        self._sessions[channel_id] = GameSession(
            channel_id=channel_id,
            user_id=user_id,
            user_name=user_name,
            secret_word=secret,
            theme=theme,
        )
        return self._sessions[channel_id]

    def check_guess(self, channel_id: int, guess: str) -> tuple[bool, str]:
        session = self._sessions.get(channel_id)
        if not session or not session.secret_word:
            return False, "Aucune partie en cours. Lance /play pour commencer."
        session.attempts += 1
        if guess.lower().strip() == session.secret_word.lower():
            points = session.points()
            session.score += points
            self._player_scores[session.user_id] += points
            session.found = True
            return True, f"{session.secret_word}"
        return False, ""

    def get_player_score(self, user_id: int) -> int:
        return self._player_scores.get(user_id, 0)

    def get_leaderboard(self, top_n: int = 5) -> list[tuple[int, int]]:
        return sorted(
            ((uid, pts) for uid, pts in self._player_scores.items() if uid),
            key=lambda x: -x[1],
        )[:top_n]
