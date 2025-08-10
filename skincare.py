from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.wikipedia import WikipediaTools
from phi.tools.crawl4ai_tools import Crawl4aiTools
from phi.tools.baidusearch import BaiduSearch
from phi.tools.firecrawl import FirecrawlTools
# import streamlit as st
import os
from dotenv import load_dotenv

# load the env vars from the .env file
load_dotenv()

wiki_agent = Agent(
    name = "Wikipedia agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [WikipediaTools()],
    instructions = [
        "Provide medically accurate definitions and facts related to skincare.",
        "Never pass `None` as a parameter. Use string defaults like '' or 'N/A' when unsure.",],
    markdown = True,
    show_tool_calls = True,
)

crawl_agent = Agent(
    name = "Crawl4AI Agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    tools = [Crawl4aiTools(
        max_length = 2000
    )],
    instructions = ["Summarize only from trusted sites."],
    markdown = True,
    show_tool_calls = True,
)

ecom_agent = Agent(
    name = "Shopping Agent",
    model = Groq(id = "llama-3.3-70b-versatile"),
    instructions=[
        "You are a product recommender agent specializing in finding skincare products that match user preferences.",
        "Prioritize finding products that satisfy as many user requirements as possible, but ensure a minimum match of 50%.",
        "Search for products only from authentic and trusted e-commerce websites such as Google Shopping, Amazon, Flipkart, Myntra, and Nyka.",
        "Verify that each product recommendation is in stock and available for purchase.",
        "Clearly mention the key attributes of each product (e.g., price, brand, features) in the response.",
        "Format the recommendations neatly and ensure clarity for ease of user understanding.",
    ],
    tools = [FirecrawlTools()],
    markdown = True,
    show_tool_calls = True
)

search_agent = Agent(
    name = "Baidu Search Agent",
    tools = [BaiduSearch()],
    description = "You are a search agent that gives skincare product recommendations from the internet.",
    instructions = [
        "Given a query by the user, response with the top 3 relevant answers.",
        "Search 5 results and return the top 3.",
        "Give higher preference to cosmetology sites."
    ],
    show_tool_calls = True,
)

router = Agent(
    name = "Skincare Router",
    model = Groq(id = "llama-3.3-70b-versatile"),
    team = [wiki_agent, crawl_agent, ecom_agent, search_agent],
    instructions = [
        "when the user asks 'what is k?' send to Wikipedia agent.",
        "When the user asks 'suggets products for k' send to Baidu Search Agent.",
        "When the user asks 'recommend/suggest x for y skin' send to Shopping agent. ",
        "Else send to Crawl4AI Agent",
        "if the user asks multiple questions at once, then return a combined, coherent answer.",
    ],
    # show_tool_calls = True,
    markdown = True,
)
