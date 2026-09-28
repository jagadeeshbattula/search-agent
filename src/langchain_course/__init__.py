from dotenv import load_dotenv
import os

load_dotenv()

def main() -> None:
    print("Hello from langchain-course!")
    print(os.getenv("OLAMA_API_KEY"))
