import os
from dotenv import load_dotenv

# Load from .env if present
load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", "YOUR_SENDGRID_API_KEY_HERE")
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "bajaj.finservhealth@almonds.ai")
