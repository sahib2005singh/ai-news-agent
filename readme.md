📰 AI News Agent

Automated RSS → AI Summary → Discord Bot (Fully Local)

An autonomous AI-powered news automation system that:

Fetches latest AI-related articles from Google News RSS

Selects the most relevant article using a local LLM

Generates a concise bullet-point summary

Prevents duplicate posts using SQLite

Posts automatically to Discord via webhook

Runs entirely locally — no external LLM APIs required.

🛠️ Built With

LangChain – Tool-calling agent framework

Ollama (Llama 3.1) – Local LLM for reasoning and summarization

Google News RSS – Real-time AI news feed

SQLite – Lightweight persistence for deduplication

Python – Core implementation

🚀 Features

🔎 Real-time AI news aggregation

🧠 LLM-powered article selection

✂️ Clean 3–5 bullet-point summaries

🗄️ Duplicate prevention via SQLite database

📢 Automatic Discord webhook integration

⏰ Cron-based scheduling support

🖥️ Fully local execution (no cloud dependencies)


news_ai_agent/
│
├── news_agent.py      # Main AI agent pipeline
├── search.py          # RSS fetching logic
├── scraper.py         # Article scraping logic (if enabled)
├── database.py        # SQLite deduplication layer
├── .env               # Environment variables (ignored in Git)
├── requirements.txt   # Python dependencies
└── README.md
