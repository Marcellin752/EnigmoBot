# EnigmoBot — Angelo la Débrouille

EnigmoBot est un bot Discord interactif propulsé par le modèle **Gemini** (Google AI). Incarnant le personnage d'**Angelo la Débrouille**, le bot garde un mot secret et propose aux utilisateurs un jeu de devinettes à travers des indices.

---

## Fonctionnalités

- **Personnalité unique** : Incarne Angelo la Débrouille via les *System Instructions* du modèle Gemini.
- **Jeu du mot secret** : Le bot donne des indices subtils sans jamais révéler la réponse directement.
- *Asynchrone** : Gestion fluide des requêtes grâce aux exécuteurs asynchrones (`asyncio`).
- **Gestion de la limite Discord** : Tronque automatiquement les messages dépassant 2000 caractères pour éviter les erreurs d'envoi.

---

## Installation & Configuration

### Prerequisites
- Python 3.9 ou supérieur
- Un compte Discord et une application créés sur le [Discord Developer Portal](https://discord.com/developers/applications)
- Une clé API Gemini sur [Google AI Studio](https://aistudio.google.com/)

### 1. Cloner le dépôt
```bash
git clone [https://github.com/votre-nom-utilisateur/EnigmoBot.git](https://github.com/votre-nom-utilisateur/EnigmoBot.git)
cd EnigmoBot
```

### 2. Configurer l'environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Copiez le fichier exemple .env.example vers .env et complétez avec vos identifiants :

```bash
cp .env.example .env
```

Éditez le fichier .env :

```bash
DISCORD_TOKEN="VOTRE_TOKEN_DISCORD"
GEMINI_API_KEY="VOTRE_CLE_API_GEMINI"
```

## Utilisation

Lancez le bot avec la commande :

```bash
python3 bot_discord.py
```

Une fois en ligne, invitez le bot sur votre serveur Discord (en vous assurant de cocher l'intention Message Content Intent dans le portail développeur Discord) et commencez à discuter avec lui sur n'importe quel salon textuel auquel il a accès !

## Personnalisation
Vous pouvez ajuster les instructions système ou changer le mot secret en modifiant le fichier config.py :

```python
NOM_DU_BOT = "Agent Spécial"
INSTRUCTIONS_SYSTEME = "..."
```
