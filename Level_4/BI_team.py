from agno.models.google import Gemini
from agno.team.team import Team
from agno.tools.reasoning import ReasoningTools
import sys
import os
import time

# Setup project path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config import API_KEY

# Import all required agents
from Level_3.competitor_analysis_agent import competitor_analysis_agent
from Level_1.finance_agent import finance_agent
from Level_1.web_search_agent import web_agent
from Level_1.media_trend_analysis_agent import agent as media_trend_agent
from Level_1.deep_research_agent_exa import agent as deep_research_agent

api_key = API_KEY

# Create Gemini model with rate limiting
gemini_model = Gemini(
    id="gemini-2.0-flash-exp", 
    api_key=api_key
)

business_intelligence_team = Team(
    name="Business Intelligence & Strategy Team",
    mode="coordinate",
    model=gemini_model,
    members=[
        competitor_analysis_agent,
        finance_agent,
        web_agent,
        media_trend_agent,
        deep_research_agent
    ],
    tools=[ReasoningTools(add_instructions=True)],
    instructions=[
        "Collaborate to provide comprehensive business intelligence and strategic insights",
        "Each agent should focus on their specialty while supporting the overall analysis:",
        "- Competitor Analysis Agent: Market positioning, competitive landscape, SWOT analysis",
        "- Finance Agent: Financial metrics, market sizing, revenue models, ROI calculations",
        "- Web Search Agent: Real-time market data, news, and general research support",
        "- Media Trend Agent: Public sentiment, media coverage analysis, trend identification",
        "- Legal Consultant: Regulatory compliance, legal risks, industry regulations",
        "- Deep Research Agent: In-depth industry research, emerging technologies, market gaps",
        "Present findings in a structured, executive-ready format with clear actionable recommendations",
        "Use data visualization, tables, and charts to support analysis",
        "Consider both quantitative metrics and qualitative factors in recommendations",
        "Assess risks, opportunities, and implementation feasibility for all strategic recommendations",
        "Provide timeline estimates and resource requirements for recommended strategies",
        "Cross-reference findings between agents to ensure consistency and completeness",
        "Only output the final consolidated strategic analysis, not individual agent responses",
        "Ensure all recommendations are backed by credible data and market research"
    ],
    markdown=True,
    show_members_responses=False,
    enable_agentic_context=True,
    add_datetime_to_instructions=True,
    success_criteria="The team has delivered a comprehensive business intelligence report with competitive analysis, financial assessment, regulatory compliance review, market trend analysis, strategic recommendations, and implementation roadmap with clear ROI projections.",
)

def run_market_analysis_example():
    """Example: Comprehensive market analysis"""
    print("\n🔍 Starting AI Chatbot Market Analysis...")
    print("This analysis will cover competitive landscape, financial projections, media trends, regulatory considerations, and strategic recommendations.\n")
    
    # Add a small delay before starting to respect rate limits
    time.sleep(2)
    
    return business_intelligence_team.print_response(
        """Analyze the AI chatbot market for a startup planning to enter this space:
        1. Conduct competitive landscape analysis (key players, market share, positioning)
        2. Perform financial analysis of market size, growth projections, and revenue models
        3. Research current media trends and public sentiment around AI chatbots
        4. Identify regulatory considerations and compliance requirements
        5. Conduct deep research on emerging technologies and market gaps
        6. Develop go-to-market strategy with specific recommendations
        7. Provide risk assessment and mitigation strategies
        8. Estimate required investment and potential ROI""",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )

def run_business_expansion_analysis():
    """Example: Business expansion analysis"""
    time.sleep(2)  # Rate limiting delay
    return business_intelligence_team.print_response(
        """Evaluate expansion opportunities for a fintech company into the European market:
        1. Analyze competitive landscape in key European markets
        2. Assess financial requirements and market potential
        3. Research regulatory frameworks and compliance requirements across EU
        4. Analyze media coverage and market sentiment toward fintech in Europe
        5. Conduct deep research on cultural and business practice differences
        6. Recommend market entry strategy and timeline
        7. Identify partnership opportunities and potential acquisition targets
        8. Provide comprehensive risk-reward analysis""",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )

def run_product_strategy_analysis():
    """Example: Product strategy analysis"""
    time.sleep(2)  # Rate limiting delay
    return business_intelligence_team.print_response(
        """Develop strategic recommendations for a SaaS company considering adding AI features:
        1. Analyze competitors who have successfully integrated AI features
        2. Evaluate financial impact of AI integration (costs, pricing strategies, ROI)
        3. Research market trends and customer sentiment around AI in SaaS
        4. Assess legal and regulatory implications of AI feature implementation
        5. Conduct deep research on AI technologies suitable for SaaS integration
        6. Recommend feature prioritization and development roadmap
        7. Suggest pricing and positioning strategies
        8. Provide implementation timeline and resource allocation recommendations""",
        stream=True,
        show_full_reasoning=True,
        stream_intermediate_steps=True,
    )

if __name__ == "__main__":
    print("🚀 Business Intelligence & Strategy Team - Available Analysis Types:")
    print("1. AI Chatbot Market Analysis")
    print("2. European Market Expansion")
    print("3. AI Feature Integration Strategy")
    print("4. Custom Analysis")
    
    choice = input("\nSelect analysis type (1-4): ").strip()
    
    if choice == "1":
        print("\n🔍 Running AI Chatbot Market Analysis...")
        run_market_analysis_example()
    elif choice == "2":
        print("\n🌍 Running European Market Expansion Analysis...")
        run_business_expansion_analysis()
    elif choice == "3":
        print("\n🤖 Running AI Feature Integration Strategy...")
        run_product_strategy_analysis()
    elif choice == "4":
        custom_query = input("Enter your custom business intelligence query: ")
        print(f"\n📊 Running Custom Analysis...")
        time.sleep(2)  # Rate limiting delay
        business_intelligence_team.print_response(
            custom_query,
            stream=True,
            show_full_reasoning=True,
            stream_intermediate_steps=True,
        )
    else:
        print("\n📈 Running Default Analysis (AI Chatbot Market)...")
        run_market_analysis_example()