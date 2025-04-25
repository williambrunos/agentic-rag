import random
from llama_index.core.tools import FunctionTool


def get_weather_info(location: str) -> str:
    """
    Comment in english:
    This function checks the weather for a given location.
    Args:
        location (str): The location to check the weather for.
    Returns:
        str: A weather report.
    """
    weather_conditions = [
        {"condition": "Rainy", "temp_c": 15},
        {"condition": "Clear", "temp_c": 25},
        {"condition": "Windy", "temp_c": 20}
    ]
    data = random.choice(weather_conditions)
    return f"Weather in {location}: {data['condition']}, {data['temp_c']}°C"


check_weather_tool = FunctionTool.from_defaults(
    get_weather_info,
    name="check_weather",
    description="Check the weather for a given location."
)