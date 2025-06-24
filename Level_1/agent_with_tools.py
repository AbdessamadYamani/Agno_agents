from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

api_key=API_KEY
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp",api_key=api_key),
    tools=[YFinanceTools(stock_price=True)],
    markdown=True,
)
agent.print_response("What is the stock price of Apple?", stream=True)