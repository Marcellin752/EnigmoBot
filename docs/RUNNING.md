# Run the Bot

Once the configuration is done (see [Configuration](CONFIGURATION.md)), you can launch the bot.

## Start the bot

Make sure your virtual environment is activated:

```bash
source venv/bin/activate
```

Then run:

```bash
python3 main.py
```

Or, equivalently:

```bash
python3 -m enigmobot
```

## Expected output

You should see logs similar to:

```
12:00:00 [INFO] discord.gateway: Shard ID None has connected to Gateway (Session ID: ...)
12:00:01 [INFO] root: Agent Angelo la Débrouille en ligne sur 1 serveur(s) !
```

The bot now appears **online** in your server.

## Play a game

In any text channel where the bot has access:

1. Type `/play` — the bot starts a new game with a secret word and gives a first hint
2. Type `/guess <word>` — propose a word (autocomplete suggests words from the theme)
3. Type `/hint` — get an additional hint (costs points)
4. Type `/surrender` — reveal the secret word and start over
5. Type `/score` or `/leaderboard` — check scores and rankings
6. Type `/help` — show the full command guide

You can also **just chat normally**: the AI responds to any message with hints in Angelo's style.

## Stop the bot

Press `Ctrl+C` in the terminal. The bot logs a clean shutdown message:

```
12:30:00 [INFO] root: Arrêt du bot Angelo la Débrouille
```

## Run the tests

The project includes unit tests for the game logic:

```bash
python3 -m pytest tests/ -v
```

All tests should pass (19 tests).

## Troubleshooting

| Problem | Solution |
|---|---|
| `Login failure` | Your `DISCORD_TOKEN` is invalid — reset it in the Developer Portal |
| Bot offline in server | Check the terminal for errors and verify the token in `.env` |
| Slash commands missing | Re-invite the bot with the `applications.commands` scope, then restart it |
| `No module named 'enigmobot'` | You are running from outside the project folder — `cd` into it first |
| Gemini errors | Check your `GEMINI_API_KEY` and the [free tier limits](GEMINI_SETUP.md#free-tier) |
