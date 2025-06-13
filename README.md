#ADK Agent Setup Guide
Clone the Repository
git clone https://github.com/your-username/jr-adk-playground.git
cd jr-adk-playground
Create and Activate Virtual Environment
> python3 -m venv .venv
#Activate:
source .venv/bin/activate # macOS/Linux
.venv\Scripts\activate.bat # Windows (Command Prompt):
.venv\Scripts\Activate.ps1 # Windows (PowerShell)
#Install ADK Dependencies
Ensure your virtual environment is active.
> pip install google-adk
