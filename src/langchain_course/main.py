from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """ Schema for a source used by the agent"""

    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """ Schema for the agent response with answer and sources"""

    answer: str = Field(description="The agents answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the response")

llm = ChatOllama(model="llama3.1")
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Search agent running...")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for ai engineer in new york city metro area on linkedin and list their details.")})
    print(f"Agent result: {result}")