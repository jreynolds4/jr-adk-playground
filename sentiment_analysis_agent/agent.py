from google.adk.agents import Agent
from google.adk.tools import google_search
from .prompt import SENTIMENT_ANALYSIS_PROMPT

import vertexai
from vertexai.preview import reasoning_engines
from vertexai import agent_engines

PROJECT_ID = "test-boondocks"
LOCATION = "us-central1"
STAGING_BUCKET = "gs://adk-playground-bucket"

vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

root_agent = Agent(
    name="sentiment_analysis_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about overall market sentiment."
    ),
    instruction=SENTIMENT_ANALYSIS_PROMPT,
    tools=[google_search],
)

app = reasoning_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)

session = app.create_session(user_id="u_123")
session

remote_app = agent_engines.create(
    agent_engine=root_agent,
    requirements=[
        "google-cloud-aiplatform[adk,agent_engines]"   
    ]
)