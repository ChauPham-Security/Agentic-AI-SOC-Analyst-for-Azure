import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LOG_ANALYTICS_WORKSPACE_ID = os.getenv("LOG_ANALYTICS_WORKSPACE_ID")

if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in .env")

if not LOG_ANALYTICS_WORKSPACE_ID:
    raise ValueError("Missing LOG_ANALYTICS_WORKSPACE_ID in .env")