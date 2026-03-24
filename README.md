# 🍸 Cocktail Manager Bot

A Telegram bot for managing a cocktail database.
Allows you to add, search, view, and delete cocktail recipes.

---

## 🚀 Features

* ➕ Add cocktails via FSM (step-by-step input)
* 📋 List all cocktails
* 🔍 Search by name and ingredients
* 🍸 View full cocktail recipe
* ❌ Delete cocktails
* 📦 Seed script for populating the database

---

## 🧠 Architecture

The project follows a layered architecture:

```
handlers → services → repositories → database
```

* **handlers** — interaction with Telegram (aiogram)
* **services** — business logic
* **repositories** — database access (PostgreSQL)
* **schemas** — Pydantic models

---

## 🛠️ Tech Stack

* Python 3.10+
* aiogram
* PostgreSQL
* psycopg
* Pydantic

---

## ⚙️ Setup

### 1. Clone the repository

```
git clone <your_repo_url>
cd cocktail_manager_bot_tg
```

### 2. Create virtual environment

```
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure `.env`

Create a `.env` file:

```
BOT_TOKEN=your_token
DB_HOST=localhost
DB_PORT=5432
DB_NAME=cocktails
DB_USER=postgres
DB_PASSWORD=your_password
```

---

## ▶️ Run the bot

```
python -m bot.bot
```

---

## 🌱 Seed the database

Populate the database with sample cocktails:

```
python -m scripts.seed_cocktails
```

---

## 📋 Available Commands

```
/start — welcome message
/help — list of commands
/add — create a cocktail
/list — show cocktails
/cocktail <name> — show recipe
/search <query> — search cocktails
/delete <name> — delete cocktail
```

---

## 📦 Project Structure

```
cocktail_manager_bot_tg/
├── bot/
├── handlers/
├── services/
├── repositories/
├── schemas/
├── db/
├── scripts/
│   └── seed_cocktails.py
├── config.py
├── requirements.txt
└── README.md
```

---

## 🧩 Implementation Highlights

* FSM-based cocktail creation flow
* Support for multi-word cocktail names
* SQL JOIN queries for search
* ON DELETE CASCADE for ingredients
* Seed script built on service layer

---

## 📈 Future Improvements

* Pagination for `/list`
* Inline keyboard support
* Image support for cocktails
* Export to Google Sheets
* Improved search functionality

---

## 👤 Author

Stepan Salmin
Python Backend Developer

---
