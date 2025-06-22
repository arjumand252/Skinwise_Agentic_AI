from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.wikipedia import WikipediaTools
from phi.tools.crawl4ai_tools import Crawl4aiTools
from phi.tools.baidusearch import BaiduSearch
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
    team = [wiki_agent, crawl_agent],
    instructions = [
        "when the user asks 'what is k?' send to Wikipedia agent.",
        "When the user ask 'suggets products for k' send to Baidu Search Agent",
        "Else send to Crawl4AI Agent",
        "if the user asks multiple questions at once, then return a combined, coherent answer.",
    ],
    show_tool_calls = True,
    markdown = True,
)

# router.print_response("Does retinol help to reduce acne?", stream=True)
# response = router.run("What does a toner do? suggest a toner for combination skin.")
# print(response.content)

# def get_answer(query):
#     response = router.run(query)
#     return response.content

# def main():
#     st.set_page_config(page_title = "Skincare Agentic AI", layout = "centered")
#     st.markdown("""
#     <div style="background-color:#f0e5f5;padding:10px;border-radius:10px">
#         <h2 style="color:#5e548e;text-align:center;">Skincare Query Resolver (Agentic AI)</h2>
#     </div>
#     """, unsafe_allow_html=True)

#     query = st.text_input("Ask your skincare-related question:")

#     if st.button("Submit"):
#         with st.spinner("Thinking..."):
#             answer = get_answer(query)
#             st.success("Asnwer:")
#             st.markdown(answer, unsafe_allow_html=True)

# if __name__ == '__main__':
#     main()