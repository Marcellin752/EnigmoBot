# EnigmoBot — Angelo la Debrouille

Interactive Discord bot powered by **Gemini** (Google AI). Embodies **Angelo la Debrouille** and challenges players to find a secret word through clues.

---

## Features

- **Unique personality** via Gemini system instructions
- **8 themes**: animals, objects, food, nature, sports, music, professions, vehicles
- **Score system** with points, penalties, and leaderboard
- **Slash commands**: `/play`, `/guess`, `/hint`, `/surrender`, `/score`, `/leaderboard`, `/theme`, `/help`
- **Per-channel sessions** — each channel has its own game
- **Server-side validation** of the secret word (no cheating)
- **Structured logging** with timestamps

---

## Installation

> **New to this?** Follow the step-by-step guides in [docs/](docs/README.md) —
> they explain how to create a Discord bot and connect it from scratch.

### Requirements
- Python 3.10 or higher
- A Discord account and application on the [Discord Developer Portal](https://discord.com/developers/applications)
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/)

### 1. Clone
```bash
git clone git@github.com:Marcellin752/EnigmoBot.git
cd EnigmoBot
```

### 2. Virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configuration
```bash
cp .env.example .env
```
Edit `.env` with your tokens:
```
DISCORD_TOKEN="YOUR_DISCORD_TOKEN"
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

### 5. Run
```bash
python3 main.py
```

### Tests
```bash
python3 -m pytest tests/ -v
```

---

## Documentation

Step-by-step setup guides are available in [docs/](docs/README.md):

| Guide | Description |
|---|---|
| [Prerequisites](docs/PREREQUISITES.md) | What you need before starting |
| [Discord Bot Setup](docs/DISCORD_SETUP.md) | Create a Discord application and get a bot token |
| [Invite the Bot](docs/INVITE_BOT.md) | Add the bot to your server |
| [Gemini API Setup](docs/GEMINI_SETUP.md) | Get a free Gemini API key |
| [Configuration](docs/CONFIGURATION.md) | Configure the `.env` file |
| [Run the Bot](docs/RUNNING.md) | Launch and verify the bot |

---

## Commands

| Command | Description |
|---|---|
| `/play [theme]` | Start a new game (optional theme) |
| `/guess <word>` | Guess a word |
| `/hint` | Request an additional hint |
| `/surrender` | Give up and reveal the word |
| `/score` | Show your cumulative score |
| `/leaderboard` | Show the player rankings |
| `/theme` | List available themes |
| `/help` | Full command guide |

You can also **chat normally** in the channel — the AI will respond and give hints automatically.

---

## Project structure

```
enigmobot/
├── config.py               # Env vars + system instructions
├── ai.py                   # Gemini client (per-channel sessions)
├── game.py                 # Game logic (words, scores, validation)
├── bot.py                  # Discord client
├── cogs/commands.py        # Slash commands + events
├── __main__.py             # Entry point (python -m enigmobot)
├── main.py                 # Entry point
├── tests/                  # Unit tests
├── docs/                   # Setup guides
├── requirements.txt        # Dependencies
└── README.md
```
