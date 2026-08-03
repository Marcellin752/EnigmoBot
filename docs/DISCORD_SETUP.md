# Discord Bot Setup

This guide explains how to create a Discord application and generate the bot token needed to run EnigmoBot.

## Step 1: Open the Discord Developer Portal

Go to the [Discord Developer Portal](https://discord.com/developers/applications) and log in with your Discord account.

## Step 2: Create a new application

1. Click the **New Application** button (top right).
2. Give your application a name (e.g., `EnigmoBot`).
3. Click **Create**.
4. Accept the terms of service if prompted.

## Step 3: Create the bot user

1. In the left sidebar, click **Bot**.
2. Click **Add Bot**, then confirm with **Yes, do it!**.

## Step 4: Enable the Message Content Intent

This is **required** — the bot needs to read and respond to messages.

1. In the **Bot** section, scroll down to **Privileged Gateway Intents**.
2. Enable **Message Content Intent**.
3. Save your changes.

## Step 5: Copy the bot token

1. In the **Bot** section, click **Reset Token**.
2. Click **Yes, do it!** and confirm your password.
3. Click the **Copy** button next to the new token.
4. **Store it in a safe place** — it looks like:
   `MTI5Njg3ODI5MzU4MDM5MDQ4NA.Gabcdef.hijklmnop`
5. You will paste it into the `.env` file in the [Configuration](CONFIGURATION.md) step.

> **Security warning**: Never share your token publicly. Anyone with this token can control your bot.
> If you commit it to a public repository, **reset the token immediately**.

## Useful settings

In the **Bot** section you can also:

- Change the bot's **username** (e.g., "Angelo la Debrouille")
- Enable **Public Bot** to let anyone invite it
- Keep **Require OAuth2 Code Grant** disabled (this bot uses a token, not OAuth)

---

Next step: [Invite the bot to your server](INVITE_BOT.md)