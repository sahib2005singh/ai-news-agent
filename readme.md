An autonomous AI-powered news agent that:

Fetches latest AI-related articles from RSS

Avoids duplicate postings using SQLite

Selects the most relevant article

Generates a clean bullet-point summary

Posts it automatically to Discord via webhook

Built using:

LangChain

Ollama (Llama 3.1 local model)

Google News RSS

SQLite

Python

🚀 Features

🔎 Real-time RSS news fetching

🧠 AI-powered article selection

✂️ Bullet-point summarization

🗄️ Deduplication with SQLite

📢 Automatic Discord posting

🖥️ Runs fully locally (no external LLM APIs required)

🏗️ Project Structure
news_ai_agent/
│
├── news_agent.py     # Main AI agent pipeline
├── search.py         # RSS fetching logic
├── scraper.py        # Article scraping logic
├── database.py       # SQLite deduplication
├── .env              # Environment variables (NOT committed)
├── requirements.txt
└── README.md
