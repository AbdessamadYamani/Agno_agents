from agno.agent import Agent
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.google import Gemini
from agno.vectordb.lancedb import LanceDb
from agno.embedder.sentence_transformer import SentenceTransformerEmbedder

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

# LanceDB stores data locally in files
knowledge_base = PDFUrlKnowledgeBase(
    urls=[
        "https://www.justice.gov/d9/criminal-ccips/legacy/2015/01/14/ccmanual_0.pdf",
    ],
    vector_db=LanceDb(
        table_name="legal_docs",
        uri="./lancedb_data",  # Local directory for data storage
        embedder=SentenceTransformerEmbedder()
    ),
)
knowledge_base.load(recreate=False)

legal_agent = Agent(
    name="LegalAdvisor",
    knowledge=knowledge_base,
    search_knowledge=True,
    model=Gemini(id="gemini-2.0-flash-exp", api_key=API_KEY),
    markdown=True,
    instructions=[
        "Provide legal information and advice based on the knowledge base.",
        "Include relevant legal citations and sources when answering questions.",
        "Always clarify that you're providing general legal information, not professional legal advice.",
        "Recommend consulting with a licensed attorney for specific legal situations.",
    ],
)

legal_agent.print_response(
    "What are the legal consequences and criminal penalties for spoofing Email Address?",
    stream=True,
)