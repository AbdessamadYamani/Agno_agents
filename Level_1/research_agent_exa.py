from datetime import datetime
from textwrap import dedent

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.exa import ExaTools

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import API_KEY
# Initialize the academic research agent with scholarly capabilities
research_scholar = Agent(
    model=Gemini(id="gemini-2.0-flash-exp", api_key=API_KEY),
    tools=[
        ExaTools(
            start_published_date=datetime.now().strftime("%Y-%m-%d"), type="keyword"
        )
    ],
    description=dedent("""\
        You are a distinguished research scholar with expertise in multiple disciplines.
        Your academic credentials include: 📚

        - Advanced research methodology
        - Cross-disciplinary synthesis
        - Academic literature analysis
        - Scientific writing excellence
        - Peer review experience
        - Citation management
        - Data interpretation
        - Technical communication
        - Research ethics
        - Emerging trends analysis\
    """),
    instructions=dedent("""\
        1. Research Methodology 🔍
           - Conduct 3 distinct academic searches
           - Focus on peer-reviewed publications
           - Prioritize recent breakthrough findings
           - Identify key researchers and institutions

        2. Analysis Framework 📊
           - Synthesize findings across sources
           - Evaluate research methodologies
           - Identify consensus and controversies
           - Assess practical implications

        3. Report Structure 📝
           - Create an engaging academic title
           - Write a compelling abstract
           - Present methodology clearly
           - Discuss findings systematically
           - Draw evidence-based conclusions

        4. Quality Standards ✓
           - Ensure accurate citations
           - Maintain academic rigor
           - Present balanced perspectives
           - Highlight future research directions\
    """),
    expected_output=dedent("""\
        # {Engaging Title} 📚

        ## Abstract
        {Concise overview of the research and key findings}

        ## Introduction
        {Context and significance}
        {Research objectives}

        ## Methodology
        {Search strategy}
        {Selection criteria}

        ## Literature Review
        {Current state of research}
        {Key findings and breakthroughs}
        {Emerging trends}

        ## Analysis
        {Critical evaluation}
        {Cross-study comparisons}
        {Research gaps}

        ## Future Directions
        {Emerging research opportunities}
        {Potential applications}
        {Open questions}

        ## Conclusions
        {Summary of key findings}
        {Implications for the field}

        ## References
        {Properly formatted academic citations}

        ---
        Research conducted by AI Academic Scholar
        Published: {current_date}
        Last Updated: {current_time}\
    """),
    markdown=True,
    show_tool_calls=True,
    add_datetime_to_instructions=True,
    save_response_to_file="tmp/{message}.md",
)

# Example usage with academic research request
if __name__ == "__main__":
    research_scholar.print_response(
        "Analyze recent developments in quantum computing architectures",
        stream=True,
    )

# Advanced research topics to explore:
"""
Quantum Science & Computing:
1. "Investigate recent breakthroughs in quantum error correction"
2. "Analyze the development of topological quantum computing"
3. "Research quantum machine learning algorithms and applications"
4. "Explore advances in quantum sensing technologies"

Biotechnology & Medicine:
1. "Examine recent developments in mRNA vaccine technology"
2. "Analyze breakthroughs in organoid research"
3. "Investigate advances in precision medicine"
4. "Research developments in neurotechnology"

Materials Science:
1. "Explore recent advances in metamaterials"
2. "Analyze developments in 2D materials beyond graphene"
3. "Research progress in self-healing materials"
4. "Investigate new battery technologies"

Artificial Intelligence:
1. "Examine recent advances in foundation models"
2. "Analyze developments in AI safety research"
3. "Research progress in neuromorphic computing"
4. "Investigate advances in explainable AI"
"""