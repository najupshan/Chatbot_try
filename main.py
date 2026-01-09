from dotenv import load_dotenv
import os
from openai import OpenAI

# Load .env
load_dotenv()

# Get token
hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    raise ValueError("HF_TOKEN not found! Please check your .env file.")

# Create client
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=hf_token,
)

# Call GPT-OSS
response = client.chat.completions.create(
    model="openai/gpt-oss-20b:groq",
    messages=[{"role": "user",
                "content": "What is the capital of France?"}],
)

# Print the answer
print("GPT Answer:", response.choices[0].message.content)
