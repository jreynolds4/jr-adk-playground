from google.adk.agents import Agent
from google.adk.tools import google_search
from .prompt import SENTIMENT_ANALYSIS_PROMPT

root_agent = Agent(
    name="sentiment_analysis_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about overall market sentiment."
    ),
    instruction=SENTIMENT_ANALYSIS_PROMPT,
    tools=[google_search],
)