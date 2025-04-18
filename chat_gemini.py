from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

 
client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents='what is the current weather in Mathura'
)
print(response.text)
