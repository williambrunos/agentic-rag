from llama_index.core.tools import FunctionTool
from huggingface_hub import list_models

def get_hub_stats(author: str) -> str:
    """
    Fetches the most downloaded model from a specific author on the Hugging Face Hub.
    
    Args:
        author (str): The author whose models to check.
    
    Returns:
        str: A message indicating the most downloaded model by the author.
    """
    try:
        # List models from the specified author, sorted by downloads
        models = list(list_models(author=author, sort="downloads", direction=-1, limit=1))

        if models:
            model = models[0]
            return f"The most downloaded model by {author} is {model.id} with {model.downloads:,} downloads."
        else:
            return f"No models found for author {author}."
    except Exception as e:
        return f"Error fetching models for {author}: {str(e)}"


hub_stats_tool = FunctionTool.from_defaults(
    get_hub_stats,
    name="get_hub_stats",
    description="Fetch the most downloaded model from a specific author on the Hugging Face Hub."
)

