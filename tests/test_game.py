import pytest
from enigmobot.game import GameManager, GameSession, MOTS_THEMES


class TestGameSession:
    def test_points_no_penalty(self):
        session = GameSession(channel_id=1)
        assert session.points() == 100

    def test_points_with_hints(self):
        session = GameSession(channel_id=1, hints_given=2)
        assert session.points() == 70

    def test_points_with_attempts(self):
        session = GameSession(channel_id=1, attempts=4)
        assert session.points() == 80

    def test_points_minimum(self):
        session = GameSession(channel_id=1, attempts=100, hints_given=100)
        assert session.points() == 10


class TestGameManager:
    def setup_method(self):
        self.manager = GameManager()

    def test_get_or_create_creates(self):
        session = self.manager.get_or_create(channel_id=42)
        assert session.channel_id == 42
        assert session.secret_word == ""

    def test_get_or_create_returns_same(self):
        first = self.manager.get_or_create(channel_id=42)
        second = self.manager.get_or_create(channel_id=42)
        assert first is second

    def test_reset_removes_session(self):
        self.manager.get_or_create(channel_id=42)
        self.manager.reset(channel_id=42)
        session = self.manager.get_or_create(channel_id=42)
        assert session is not None

    def test_new_game_theme_and_word(self):
        session = self.manager.new_game(channel_id=1, theme="animaux")
        assert session.theme == "animaux"
        assert session.secret_word in MOTS_THEMES["animaux"]

    def test_new_game_invalid_theme_falls_back(self):
        session = self.manager.new_game(channel_id=1, theme="inconnu")
        assert session.theme in MOTS_THEMES

    def test_new_game_no_theme_random(self):
        session = self.manager.new_game(channel_id=1)
        assert session.theme in MOTS_THEMES
        assert session.secret_word in MOTS_THEMES[session.theme]

    def test_new_game_stores_user(self):
        session = self.manager.new_game(channel_id=1, user_id=123, user_name="toto")
        assert session.user_id == 123
        assert session.user_name == "toto"

    def test_check_guess_no_game(self):
        correct, msg = self.manager.check_guess(channel_id=999, guess="mot")
        assert correct is False
        assert "play" in msg

    def test_check_guess_correct(self):
        self.manager.new_game(channel_id=1, user_id=123, theme="animaux")
        secret = self.manager.get_or_create(1).secret_word
        correct, word = self.manager.check_guess(channel_id=1, guess=secret.upper())
        assert correct is True
        assert word == secret
        session = self.manager.get_or_create(1)
        assert session.attempts == 1
        assert session.found is True
        assert session.score == 100

    def test_check_guess_wrong(self):
        self.manager.new_game(channel_id=1, theme="animaux")
        correct, word = self.manager.check_guess(channel_id=1, guess="xxxxxxxx")
        assert correct is False
        session = self.manager.get_or_create(1)
        assert session.attempts == 1
        assert session.found is False

    def test_check_guess_case_insensitive_with_spaces(self):
        self.manager.new_game(channel_id=1, theme="animaux")
        secret = self.manager.get_or_create(1).secret_word
        correct, _ = self.manager.check_guess(channel_id=1, guess=f"  {secret.upper()}  ")
        assert correct is True

    def test_player_score_accumulates_across_games(self):
        manager = self.manager
        for i in range(2):
            manager.new_game(channel_id=100 + i, user_id=123, theme="animaux")
            secret = manager.get_or_create(100 + i).secret_word
            manager.check_guess(channel_id=100 + i, guess=secret)
        assert manager.get_player_score(123) == 200

    def test_get_player_score_unknown_user(self):
        assert self.manager.get_player_score(999) == 0

    def test_leaderboard_sorted(self):
        manager = self.manager
        for i in range(3):
            manager.new_game(channel_id=200 + i, user_id=1000 + i, theme="animaux")
            secret = manager.get_or_create(200 + i).secret_word
            manager.check_guess(channel_id=200 + i, guess=secret)
        board = manager.get_leaderboard()
        scores = [pts for _, pts in board]
        assert scores == sorted(scores, reverse=True)
        assert len(board) == 3

    def test_leaderboard_excludes_anonymous(self):
        manager = self.manager
        manager.new_game(channel_id=300, theme="animaux")
        secret = manager.get_or_create(300).secret_word
        manager.check_guess(channel_id=300, guess=secret)
        assert manager.get_leaderboard() == []
