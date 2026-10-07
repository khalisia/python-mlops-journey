import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
environment = os.getenv("ENVIRONMENT")
log_level = os.getenv("LOG_LEVEL")

print("===== APPLICATION CONFIG =====")
print(f"App name: {app_name}")
print(f"Environment: {environment}")
print(f"Log level: {log_level}")
