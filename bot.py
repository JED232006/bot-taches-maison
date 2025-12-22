import os

TOKEN = os.environ.get("TOKEN_TELEGRAM")

print("=== DEBUG TOKEN ===")
print("TOKEN value:", TOKEN)
print("TOKEN is None ?", TOKEN is None)
