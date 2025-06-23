from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.vectordb.pgvector import PgVector, SearchType

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"  # Replace with your database URL

knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],  # Replace with your PDF URL
    vector_db=PgVector(table_name="recipes", db_url=db_url, search_type=SearchType.hybrid),
)

# Load the knowledge base (comment out after the first run)
#knowledge_base.load(upsert=True)

agent = Agent(
    model=OpenAIChat(id="gpt-4o"),
    knowledge=knowledge_base,
    add_references=True,  # Enable RAG
    search_knowledge=False,  # Explicitly disable search_knowledge as add_references is used
    markdown=True,
)

response = agent.run("How do I make chicken and galangal in coconut milk soup")