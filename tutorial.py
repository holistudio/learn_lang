import getpass
import os

from dotenv import load_dotenv

load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

print(model.invoke("Hello, world!"))