import asyncio
from textwrap import dedent
import nest_asyncio

# Allow nested event loops - fixes Windows asyncio issues
nest_asyncio.apply()

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.mcp import MCPTools
from agno.tools.thinking import ThinkingTools

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

api_key=API_KEY

async def run_agent(message: str) -> None:
    async with MCPTools(
        "npx -y @openbnb/mcp-server-airbnb --ignore-robots-txt"
    ) as mcp_tools:
        agent = Agent(
            model=Gemini(id="gemini-2.0-flash-exp",api_key=api_key),
            tools=[ThinkingTools(), mcp_tools],
            instructions=dedent("""\
            ## General Instructions
            - Always start by using the think tool to map out the steps needed to complete the task.
            - After receiving tool results, use the think tool as a scratchpad to validate the results for correctness
            - Before responding to the user, use the think tool to jot down final thoughts and ideas.
            - Present final outputs in well-organized tables whenever possible.
            - Always provide links to the listings in your response.
            - Show your top 10 recommendations in a table and make a case for why each is the best choice.

            ## Using the think tool
            At every step, use the think tool as a scratchpad to:
            - Restate the object in your own words to ensure full comprehension.
            - List the  specific rules that apply to the current request
            - Check if all required information is collected and is valid
            - Verify that the planned action completes the task\
            """),
            add_datetime_to_instructions=True,
            show_tool_calls=True,
            markdown=True,
        )
        await agent.aprint_response(message, stream=True)


if __name__ == "__main__":
    task = dedent("""\
    I'm traveling to San Francisco from April 20th - May 8th. Can you find me the best deals for a 1 bedroom apartment?
    I'd like a dedicated workspace and close proximity to public transport.\
    """)
    asyncio.run(run_agent(task))