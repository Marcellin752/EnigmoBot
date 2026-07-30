# EnigmoBot — Angelo la Débrouille

Bot Discord interactif propulsé par **Gemini** (Google AI). Incarne **Angelo la Débrouille** et défie les joueurs à trouver un mot secret grâce à des indices.

---

## Fonctionnalités

- **Personnalité unique** via les instructions système Gemini
- **8 thèmes** : animaux, objets, nourriture, nature, sports, musique, métiers, transports
- **Système de score** avec points, bonus et classement
- **Commandes slash** : `/play`, `/guess`, `/indice`, `/abandonner`, `/score`, `/leaderboard`, `/theme`, `/help`
- **Sessions isolées par salon** — chaque salon a sa propre partie
- **Validation côté code** du mot secret (pas de triche possible)
- **Logs structurés** avec timestamps

---

## Installation

### Prérequis
- Python 3.10 ou supérieur
- Un compte Discord et une application sur le [Discord Developer Portal](https://discord.com/developers/applications)
- Une clé API Gemini sur [Google AI Studio](https://aistudio.google.com/)

### 1. Cloner
```bash
git clone git@github.com:Marcellin752/EnigmoBot.git
cd EnigmoBot
```

### 2. Environnement virtuel
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Dépendances
```bash
pip install -r requirements.txt
```

### 4. Configuration
```bash
cp .env.example .env
```
Éditez `.env` avec vos tokens :
```
DISCORD_TOKEN="VOTRE_TOKEN_DISCORD"
GEMINI_API_KEY="VOTRE_CLE_API_GEMINI"
```

### 5. Lancer
```bash
python3 main.py
```

---

## Commandes

| Commande | Description |
|---|---|
| `/play [theme]` | Commence une nouvelle partie (thème optionnel) |
| `/guess <mot>` | Propose un mot |
| `/indice` | Demande un indice supplémentaire |
| `/abandonner` | Abandonne et révèle le mot |
| `/score` | Affiche ton score cumulé |
| `/leaderboard` | Classement des meilleurs joueurs |
| `/theme` | Liste des thèmes disponibles |
| `/help` | Aide complète |

Tu peux aussi **parler normalement** dans le salon — l'IA répondra et donnera des indices automatiquement.

---

## Structure du projet

```
enigmobot/                  # Package principal
├── config.py               # Variables d'env + instructions système
├── ai.py                   # Client Gemini (sessions par salon)
├── game.py                 # Logique métier (mots, scores, validation)
├── bot.py                  # Client Discord
├── cogs/game.py            # Commandes slash + événements
├── __main__.py             # Entrée python -m enigmobot
├── main.py                 # Point d'entrée
├── requirements.txt        # 3 dépendances
└── README.md
```
