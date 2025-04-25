from llama_index.core.agent.workflow import AgentWorkflow
from app.services.llm_wrapper import llm
from app.tools.check_hub_stats import check_hub_stats_tool
from app.tools.check_weather import check_weather_tool
from app.tools.perform_websearch import duckduckgo_search_tool
from app.tools.perform_retrieval import perform_retrieval_tool
from app.services.prompts import system_prompt


alfred = AgentWorkflow.from_tools_or_functions(
    [
        check_hub_stats_tool, 
        check_weather_tool, 
        duckduckgo_search_tool, 
        perform_retrieval_tool
    ],
    llm=llm,
    system_prompt=system_prompt["system_prompt"]
)