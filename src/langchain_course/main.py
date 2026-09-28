from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch



llm = ChatOllama(model="llama3.1")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from search agent")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for ai engineer in new york city metro area on linkedin and list their details.")})
    print(f"Agent result: {result}")