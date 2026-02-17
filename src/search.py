import feedparser
import ssl
import certifi

ssl._create_default_https_context = lambda: ssl.create_default_context(
    cafile=certifi.where()
)
def search_news(query):
    url = "https://news.google.com/rss/search?q=AI&hl=en-IN&gl=IN&ceid=IN:en"
    articles= []
    news = feedparser.parse(url)
    for entry in news.entries[:5]:
        articles.append({"title":entry.title, "link": entry.link, "published": entry.published})

    return articles
#https://www.technologyreview.com/topic/artificial-intelligence/feed/