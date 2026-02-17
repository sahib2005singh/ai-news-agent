from langchain_ollama import ChatOllama
from langchain.tools import tool
import json
import re
import requests
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from search import search_news
from database import is_posted, save_article
import os
from dotenv import load_dotenv
load_dotenv()

llm = ChatOllama(
    model="llama3.1",
    temperature=0
)

discord_webhook = os.getenv("DISCORD_WEBHOOK")

@tool
def news_searcher(query: str) -> str:
    """Return fresh AI-related RSS articles as JSON list."""
    result = search_news(query)

    fresh_articles = [
        article for article in result
        if not is_posted(article["link"])
    ]

    return json.dumps(fresh_articles)

@tool
def post_to_discord(message: str):
    """post the summarized articles at discord"""
    response = requests.post(
        discord_webhook,
        json={"content": message}
    )

    if response.status_code == 204:
        print("Posted successfully.")
    else:
        print("Failed:", response.status_code)
        
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an AI news agent.\n"
     "1. Call news_searcher with query='AI'.\n"
     "2. Select ONE most relevant article.\n"
     "3. Return a Discord-ready message in this format:\n\n"
     "Title\n\n"
     "• Point 1\n"
     "• Point 2\n"
     "• Point 3\n\n"
     "Read more: <URL>\n\n"
     "Return ONLY this formatted text.\n"
     "Do not explain anything."
    ),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])
tools = [news_searcher]

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor( 
    agent=agent,
    tools=tools,
    verbose=True
)

response = agent_executor.invoke({
    "input": "Find best AI article and prepare Discord post."
})

final_text = response["output"]

url_match = re.search(r'Read more:\s*(.*)', final_text)
url = url_match.group(1).strip() if url_match else None

if url and not is_posted(url):
    post_to_discord.invoke({"message": final_text})
    save_article(url, None, None)
    print("Posted successfully.")
else:
    print("Article already posted or URL missing.")

