
import json
from textwrap import dedent

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.exa import ExaTools

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

api_key = API_KEY

# Define the research schema
research_schema = {
    "type": "object",
    "properties": {
        "major_players": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "role": {"type": "string"},
                    "contributions": {"type": "string"},
                },
                "required": ["name", "role", "contributions"]
            },
        },
    },
    "required": ["major_players"],
}

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp", api_key=api_key),
    tools=[ExaTools()],  # Remove research parameters
    instructions=dedent("""
        You are an expert research analyst with access to advanced search tools.
        
        When conducting research:
        1. Use the search_exa tool to find relevant, recent information
        2. Search for multiple queries to get comprehensive coverage
        3. Focus on authoritative sources and recent data
        4. Structure your findings according to any provided schema
        
        For semiconductor company research, focus on:
        - Market leaders by revenue and market share
        - Key technological contributions and innovations
        - Recent developments and strategic positions
        
        Present findings in a clear, structured format with proper citations.
    """),
    show_tool_calls=True,
    markdown=True,
    exponential_backoff=True,
    retries=3,
    delay_between_retries=15,
)

# Use the agent with a clear research request
# agent.print_response(
#     f"""Research the top 3 semiconductor companies in 2024. 
    
#     Please structure your response according to this JSON schema:
#     {json.dumps(research_schema, indent=2)}
    
#     For each company, include:
#     - Company name
#     - Their role in the semiconductor industry
#     - Key contributions and innovations
    
#     Focus on the largest companies by revenue and market impact.""",
#     stream=True,
# )