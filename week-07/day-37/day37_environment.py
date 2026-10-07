import os
from dotenv import load_dotenv

load_dotenv()

name = os.getenv("NAME")
api_key = os.getenv("API_KEY")

print(f"Name: {name}")
print(f"API Key: {api_key}")

