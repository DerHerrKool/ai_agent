import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError ("There is no API key")

from google import genai

client = genai.Client(api_key=api_key)

user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

response = client.models.generate_content(
    model="gemini-2.5-flash", contents=user_prompt,
)


usage = response.usage_metadata
if usage is None:
    raise RuntimeError("There is no usage metadata")
else:
    prompt_tokens = usage.prompt_token_count
    response_tokens = usage.candidates_token_count

print(f"User prompt: {user_prompt}") 
print(f"Prompt tokens: {prompt_tokens}")
print(f"Response tokens: {response_tokens}")
print(response.text)

