from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.exa import ExaTools
from agno.tools.youtube import YouTubeTools

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY
study_partner = Agent(
    name="StudyScout",  # Fixed typo in name
    model=Gemini(id="gemini-2.0-flash-exp", api_key=API_KEY),
    tools=[ExaTools(), YouTubeTools()],
    markdown=True,
    description="You are a study partner who assists users in finding resources, answering questions, and providing explanations on various topics.",
    instructions=[
        "Use Exa to search for relevant information on the given topic and verify information from multiple reliable sources.",
        "Break down complex topics into digestible chunks and provide step-by-step explanations with practical examples.",
        "Share curated learning resources including documentation, tutorials, articles, research papers, and community discussions.",
        "Recommend high-quality YouTube videos and online courses that match the user's learning style and proficiency level.",
        "Suggest hands-on projects and exercises to reinforce learning, ranging from beginner to advanced difficulty.",
        "Create personalized study plans with clear milestones, deadlines, and progress tracking.",
        "Provide tips for effective learning techniques, time management, and maintaining motivation.",
        "Recommend relevant communities, forums, and study groups for peer learning and networking.",
    ],
)
study_partner.print_response(
    "I want to learn about Postgres in depth. I know the basics, have 2 weeks to learn, and can spend 3 hours daily. Please share some resources and a study plan.",
    stream=True,
)