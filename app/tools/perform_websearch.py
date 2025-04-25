from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from llama_index.core.tools import FunctionTool

tool_spec = DuckDuckGoSearchToolSpec()

duckduckgo_search_tool = FunctionTool.from_defaults(
    tool_spec.duckduckgo_full_search,
    name="DuckDuckGoSearch",
    description="Search the web using DuckDuckGo."
)