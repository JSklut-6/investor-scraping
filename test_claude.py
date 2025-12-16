import os
from anthropic import Anthropic

api_key = open(".env").read().split("ANTHROPIC_API_KEY=")[1].split()[0]
print("Key:", api_key[:20], "...")

client = Anthropic(api_key=api_key)
response = client.messages.create(
    model="claude-sonnet-4-20250514", 
    max_tokens=20, 
    messages=[{"role":"user","content":"Say hello!"}]
)

print("Claude:", response.content[0].text)
print("SUCCESS!")
