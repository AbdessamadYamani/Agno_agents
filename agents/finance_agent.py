from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

api_key=API_KEY

finance_agent = Agent(
    name="Finance Agent",
    role="Handle financial data requests and market analysis",
    model=Gemini(id="gemini-2.0-flash-exp",api_key=api_key),
    tools=[YFinanceTools(stock_price=True, stock_fundamentals=True,analyst_recommendations=True, company_info=True)],
    instructions=[
        "Use tables to display stock prices, fundamentals (P/E, Market Cap), and recommendations.",
        "Clearly state the company name and ticker symbol.",
        "Focus on delivering actionable financial insights.",
    ],
    
    exponential_backoff=True,
    retries=3,
    delay_between_retries=15,
    add_datetime_to_instructions=True,
)
