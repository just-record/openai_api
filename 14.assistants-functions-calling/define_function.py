from  dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI

def get_assistant(
        client: OpenAI,
        name: str = "Assistant-default",
        instructions: str = "You are a helper assistant. You can help users with their queries.",
        tools: list = [],
        model: str = "gpt-4-turbo"
        ):
    return client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=tools,
        model=model,
    )

if __name__ == '__main__':
    
    client = OpenAI()

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_temperature",
                "description": "Get the current temperature for a specific location",
                "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                    "type": "string",
                    "description": "The city and state, e.g., San Francisco, CA"
                    },
                    "unit": {
                    "type": "string",
                    "enum": ["Celsius", "Fahrenheit"],
                    "description": "The temperature unit to use. Infer this from the user's location."
                    }
                },
                "required": ["location", "unit"]
                }
            }            
        },
        {
            "type": "function",
            "function": {
                "name": "get_rain_probability",
                "description": "Get the probability of rain for a specific location",
                "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                    "type": "string",
                    "description": "The city and state, e.g., San Francisco, CA"
                    }
                },
                "required": ["location"]
                }
            }
        }

    ]

    assistant_params = {
        "name": "Weather bot",
        "instructions": "You are a weather bot. Use the provided functions to answer questions.",
        "tools": tools,
        "model": "gpt-4-turbo"
    }
    assistant = get_assistant(client, **assistant_params)

    print(assistant.model_dump_json())