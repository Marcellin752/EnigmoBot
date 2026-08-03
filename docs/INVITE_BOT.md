# Invite the Bot to Your Server

Once your Discord application is created (see [Discord Bot Setup](DISCORD_SETUP.md)), you need to generate an invite link and add the bot to your server.

## Step 1: Generate the invite link

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click your application.
3. In the left sidebar, click **OAuth2 > URL Generator**.

## Step 2: Select the scopes and permissions

Under **Scopes**, check:

- `bot`
- `applications.commands` (required for slash commands like `/play`)

Under **Bot Permissions**, check:

- `Send Messages`
- `Read Messages / View Channels`
- `Read Message History` (so the bot can see earlier messages)
- `Use Slash Commands` (also called `Use Application Commands`)

The generated **permission integer** should be `277229477888`.

## Step 3: Open the invite link

1. Scroll to the bottom of the page.
2. Copy the generated URL. It looks like:
   `https://discord.com/oauth2/authorize?client_id=...&permissions=...`
3. Open it in a browser.
4. Select your server from the dropdown.
5. Click **Authorize** and complete any captcha.

## Step 4: Verify

In your Discord server, you should now see:

- The bot in the **member list** (showing as offline until it runs)
- If you click it, the bot's role is **@everyone** by default

> If the bot does not appear, check that you are the **owner** of the server or have the **Manage Server** permission.

## Troubleshooting

| Problem | Solution |
|---|---|
| "Bot requires code grant" | Disable **Require OAuth2 Code Grant** in the Bot settings |
| Server not in the dropdown | You must be the owner or have Manage Server permission |
| Slash commands not showing | The bot must have `applications.commands` scope and be online at least once |

---

Next step: [Get your Gemini API key](GEMINI_SETUP.md)