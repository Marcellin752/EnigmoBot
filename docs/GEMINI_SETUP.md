# Gemini API Setup

This guide explains how to get a free Gemini API key. The bot uses it to power the AI that gives hints and answers.

## Step 1: Open Google AI Studio

Go to [Google AI Studio](https://aistudio.google.com/) and log in with your Google account.

## Step 2: Get an API key

1. Click **Get API key** (or go to the [API keys page](https://aistudio.google.com/apikey)).
2. Click **Create API key**.
3. Select your Google Cloud project (or create a new one).
4. Click **Create key**.
5. Copy the generated key. It looks like:
   `AIzaSyD...`
6. **Store it in a safe place** — you will paste it into the `.env` file in the [Configuration](CONFIGURATION.md) step.

## Free tier

Gemini has a **free tier** that is more than enough for a personal bot:

- **Gemini 2.5 Flash**: free with generous rate limits
- The bot uses the `gemini-2.5-flash` model by default

You can check your current usage and limits on the [API limits page](https://ai.google.dev/gemini-api/docs/rate-limits).

## Security warning

- Never share your API key publicly.
- Google may send you an email warning if your key appears in a public repository — if that happens, **delete the key and create a new one**.

## Troubleshooting

| Problem | Solution |
|---|---|
| "API key not found" | Make sure you copied the full key, including the `AIza` prefix |
| "API key restricted" | Your key may be restricted to certain APIs — check its restrictions in Google Cloud |
| 429 rate limit | The free tier has limits; wait a minute and retry |

---

Next step: [Configure the `.env` file](CONFIGURATION.md)