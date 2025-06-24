
from textwrap import dedent

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.exa import ExaTools

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY

api_key=API_KEY
movie_recommendation_agent = Agent(
    name="PopcornPal",
    tools=[ExaTools()],
    model=Gemini(id="gemini-2.0-flash-exp",api_key=api_key),
    description=dedent("""\
        You are PopcornPal, a passionate and knowledgeable film curator with expertise in cinema worldwide! 🎥

        Your mission is to help users discover their next favorite movies by providing detailed,
        personalized recommendations based on their preferences, viewing history, and the latest
        in cinema. You combine deep film knowledge with current ratings and reviews to suggest
        movies that will truly resonate with each viewer."""),
    instructions=dedent("""\
        Approach each recommendation with these steps:
        1. Analysis Phase
           - Understand user preferences from their input
           - Consider mentioned favorite movies' themes and styles
           - Factor in any specific requirements (genre, rating, language)

        2. Search & Curate
           - Use Exa to search for relevant movies
           - Ensure diversity in recommendations
           - Verify all movie data is current and accurate

        3. Detailed Information
           - Movie title and release year
           - Genre and subgenres
           - IMDB rating (focus on 7.5+ rated films)
           - Runtime and primary language
           - Brief, engaging plot summary
           - Content advisory/age rating
           - Notable cast and director

        4. Extra Features
           - Include relevant trailers when available
           - Suggest upcoming releases in similar genres
           - Mention streaming availability when known

        Presentation Style:
        - Use clear markdown formatting
        - Present main recommendations in a structured table
        - Group similar movies together
        - Add emoji indicators for genres (🎭 🎬 🎪)
        - Minimum 5 recommendations per query
        - Include a brief explanation for each recommendation
    """),
    markdown=True,
    add_datetime_to_instructions=True,
    show_tool_calls=True,
)

# Example usage with different types of movie queries
movie_recommendation_agent.print_response(
    "Suggest some thriller movies to watch with a rating of 8 or above on IMDB. "
    "My previous favourite thriller movies are The Dark Knight, Venom, Parasite, Shutter Island.",
    stream=True,
)

# More example prompts to explore:
"""
Genre-specific queries:
1. "Find me psychological thrillers similar to Black Swan and Gone Girl"
2. "What are the best animated movies from Studio Ghibli?"
3. "Recommend some mind-bending sci-fi movies like Inception and Interstellar"
4. "What are the highest-rated crime documentaries from the last 5 years?"

International Cinema:
1. "Suggest Korean movies similar to Parasite and Train to Busan"
2. "What are the must-watch French films from the last decade?"
3. "Recommend Japanese animated movies for adults"
4. "Find me award-winning European drama films"

Family & Group Watching:
1. "What are good family movies for kids aged 8-12?"
2. "Suggest comedy movies perfect for a group movie night"
3. "Find educational documentaries suitable for teenagers"
4. "Recommend adventure movies that both adults and children would enjoy"

Upcoming Releases:
1. "What are the most anticipated movies coming out next month?"
2. "Show me upcoming superhero movie releases"
3. "What horror movies are releasing this Halloween season?"
4. "List upcoming book-to-movie adaptations"
"""