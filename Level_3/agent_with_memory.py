from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google import Gemini
from rich.pretty import pprint

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

api_key=API_KEY

user_id = "peter_rabbit"
memory = Memory(
    db=SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db"),
    model=Gemini(id="gemini-2.0-flash-exp",api_key=api_key),
)
memory.clear()

agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp",api_key=api_key),
    user_id=user_id,
    memory=memory,
    enable_agentic_memory=True,
    add_datetime_to_instructions=True,
    markdown=True,
)

if __name__ == "__main__":
    agent.print_response("My name is Peter Rabbit and I like to eat carrots.")
    memories = memory.get_user_memories(user_id=user_id)
    print(f"Memories about {user_id}:")
    pprint(memories)
    agent.print_response("What is my favorite food?")
    agent.print_response("My best friend is Jemima Puddleduck.")
    print(f"Memories about {user_id}:")
    pprint(memories)
    agent.print_response("Recommend a good lunch meal, who should i invite?")
    agent.print_response("What have we been talking about?")