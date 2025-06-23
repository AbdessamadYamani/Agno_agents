from textwrap import dedent
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google import Gemini
from agno.playground import Playground
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

finance_agent_with_memory = Agent(
    name="Finance Agent with Memory",
    agent_id="financial_agent_with_memory",
    model=Gemini(id="gemini-2.0-flash-exp", api_key=API_KEY),
    tools=[YFinanceTools(enable_all=True), DuckDuckGoTools()],
    memory=Memory(
        db=SqliteMemoryDb(table_name="agent_memory", db_file="tmp/agent_data.db"),
        model=Gemini(id="gemini-2.0-flash-exp", api_key=API_KEY),
        clear_memories=True,
        delete_memories=True,
    ),
    enable_agentic_memory=True,
    storage=SqliteStorage(table_name="agent_sessions", db_file="tmp/agent_data.db"),
    add_history_to_messages=True,
    num_history_runs=3,
    add_datetime_to_instructions=True,
    markdown=True,
    instructions=dedent("""\
        You are a Wall Street analyst. Your goal is to help users with financial analysis.

        Checklist for different types of financial analysis:
        1. Market Overview: Stock price, 52-week range.
        2. Financials: P/E, Market Cap, EPS.
        3. Insights: Analyst recommendations, rating changes.
        4. Market Context: Industry trends, competitive landscape, sentiment.

        Formatting guidelines:
        - Use tables for data presentation
        - Include clear section headers
        - Add emoji indicators for trends (📈 📉)
        - Highlight key insights with bullet points
    """),
)

playground = Playground(agents=[finance_agent_with_memory])
app = playground.get_app()

if __name__ == "__main__":
    # FIXED: Use playground.serve() instead of serve_playground_app()
    playground.serve(app="finance_agent_with_memory:app", port=7777, reload=True)