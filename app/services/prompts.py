import os 
import yaml

def load_prompt(yaml_path: str = None) -> dict:
    """
    Load a YAML file and return its content as a dictionary.
    
    Args:
        yaml_path (str): Path to the YAML file.
        
    Returns:
        dict: Content of the YAML file as a dictionary.
    """
    if yaml_path is None:
        yaml_path = os.path.join(os.path.dirname(__file__), 'prompt.yaml')
    
    with open(yaml_path, 'r') as file:
        prompt = yaml.safe_load(file)
    
    return prompt


system_prompt = load_prompt("prompt.yaml")