from agno.models.google import Gemini
from agno.team.team import Team
from agno.tools.reasoning import ReasoningTools
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
from config import API_KEY

from Level_1.finance_agent import finance_agent
from Level_1.web_search_agent import web_agent
api_key=API_KEY



reasoning_finance_team = Team(
    name="Reasoning Finance Team",
    mode="coordinate",
    model=Gemini(id="gemini-2.0-flash-exp",api_key=api_key),
    members=[web_agent, finance_agent],
    tools=[ReasoningTools(add_instructions=True)],
    instructions=[
        "Collaborate to provide comprehensive financial and investment insights",
        "Consider both fundamental analysis and market sentiment",
        "Use tables and charts to display data clearly and professionally",
        "Present findings in a structured, easy-to-follow format",
        "Only output the final consolidated analysis, not individual agent responses",
    ],
    markdown=True,
    show_members_responses=True,
    enable_agentic_context=True,
    add_datetime_to_instructions=True,
    success_criteria="The team has provided a complete financial analysis with data, visualizations, risk assessment, and actionable investment recommendations supported by quantitative analysis and market research.",
)

if __name__ == "__main__":
    reasoning_finance_team.print_response("""Compare the tech sector giants (AAPL, GOOGL, MSFT) performance:
        1. Get financial data for all three companies
        2. Analyze recent news affecting the tech sector
        3. Calculate comparative metrics and correlations
        4. Recommend portfolio allocation weights""",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )