from agno.agent import Agent
from agno.knowledge.url import UrlKnowledge
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.embedder.sentence_transformer import SentenceTransformerEmbedder
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

api_key=API_KEY

knowledge = UrlKnowledge(
    urls=["https://docs.agno.com/introduction/agents.md"],
    vector_db=LanceDb(
        uri="tmp/lancedb",
        table_name="agno_docs",
        search_type=SearchType.hybrid,
embedder = SentenceTransformerEmbedder()


    ),
)

agent = Agent(
    name="Agno Assist",
    model=Gemini(id="gemini-2.0-flash-exp",api_key=api_key),
    instructions=[
        "Use tables to display data.",
        "Include sources in your response.",
        "Search your knowledge before answering the question.",
        "Only include the output in your response. No other text.",
    ],
    knowledge=knowledge,
    tools=[ReasoningTools(add_instructions=True)],
    add_datetime_to_instructions=True,
    markdown=True,
)

if __name__ == "__main__":
    agent.knowledge.load(recreate=False)
    agent.print_response(
        "What are Agents?",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )