# Configuration

This guide explains how to configure the bot with your Discord token and Gemini API key.

## Step 1: Clone the repository

```bash
git clone git@github.com:Marcellin752/EnigmoBot.git
cd EnigmoBot
```

Or download the ZIP from the GitHub repository page.

## Step 2: Create the virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows (PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

## Step 3: Install the dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Create the `.env` file

The repository contains a template file:

```bash
cp .env.example .env
```

Then open `.env` in a text editor and fill in your credentials:

```env
DISCORD_TOKEN="YOUR_DISCORD_TOKEN"
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

| Variable | Value | Where to find it |
|---|---|---|
| `DISCORD_TOKEN` | Your bot token | [Discord Setup](DISCORD_SETUP.md) step 5 |
| `GEMINI_API_KEY` | Your Gemini key | [Gemini Setup](GEMINI_SETUP.md) step 2 |

> **Important**: the `.env` file is **ignored by git** and must never be committed.
> The tokens are loaded at startup and are only used locally.

## Step 5: Customize the bot (optional)

The bot's name and personality are defined in `enigmobot/config.py`:

| Setting | Description | Default |
|---|---|---|
| `NOM_DU_BOT` | Bot display name | `Angelo la Débrouille` |
| `INSTRUCTIONS_SYSTEME` | System instructions given to the AI (personality, game rules) | French Angelo character |

The game word lists are in `enigmobot/game.py` (`MOTS_THEMES`): you can add new themes or words freely.

---

Next step: [Run the bot](RUNNING.md)