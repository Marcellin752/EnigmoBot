import logging
from enigmobot.bot import EnigmoBot
from enigmobot.config import DISCORD_TOKEN

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)


def main():
    bot = EnigmoBot()
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
