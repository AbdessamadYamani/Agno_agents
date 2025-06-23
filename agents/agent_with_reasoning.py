from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

api_key=API_KEY

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp",api_key=api_key),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        ),
    ],
    instructions=[
        "Use tables to display data.",
        "Include sources in your response.",
        "Only include the report in your response. No other text.",
    ],
    markdown=True,
)
agent.print_response(
    "Write a report on NVDA",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
)