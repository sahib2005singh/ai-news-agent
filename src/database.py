import sqlite3

db_name = "news.db"

def init_db():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posted_articles(
            link TEXT PRIMARY KEY
        )
    """)

    conn.commit()
    conn.close()


def is_posted(link):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT 1 FROM posted_articles WHERE link = ?", (link,))
    result = cursor.fetchone()

    conn.close()
    return result is not None


def save_article(link):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO posted_articles (link)
        VALUES (?)
    """, (link,))

    conn.commit()
    conn.close()
