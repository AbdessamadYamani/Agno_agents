from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

api_key=API_KEY

web_agent = Agent(
    name="Web Search Agent",
    role="Handle web search requests and general research",
    model=Gemini(id="gemini-2.0-flash-exp",api_key=api_key),
    tools=[DuckDuckGoTools()],
    instructions="Always include sources",
    add_datetime_to_instructions=True,
    exponential_backoff=True,
    retries=3,
    delay_between_retries=15,
)