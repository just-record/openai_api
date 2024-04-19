from dotenv import load_dotenv # type: ignore
load_dotenv()
from openai import OpenAI
import random
import json

# 호출할 함수 정의
def get_current_weather(location: str, unit: str = "celsius"):
    temperature = random.randint(0, 100)
    if not unit:
        unit = "celsius"
    return f"The current weather in {location} is {temperature} degrees {unit}."

client = OpenAI()

# AI가 tool을 사용 할 경우 반환 할 함수를 정의
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather", # 함수 이름
            # 함수 설명: 아주 중요함, 이 설명을 참조 하여 AI가 이 tool을 사용할지 결정
            "description": "Get the current weather in a given location", 
            "parameters": { # 함수의 인자
                "type": "object",
                "properties": { # 인자의 속성
                    "location": { # 인자의 이름
                        "type": "string",
                        # 인자의 설명
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string", 
                        "description": "The unit of temperature to return. Default is celsius.",
                        "enum": ["celsius", "fahrenheit"]
                    }, # 인자의 이름
                },
                "required": ["location"], # 필수 인자
            },
        }
    }
]
messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]
completion = client.chat.completions.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

if completion.choices[0].message.tool_calls:
    tool_call = completion.choices[0].message.tool_calls[0]
    print(tool_call.function)
    if tool_call.function.name == "get_current_weather":
        arguments = json.loads(tool_call.function.arguments)
        location = arguments.get('location')
        unit = arguments.get('unit')
        response = get_current_weather(location=location, unit=unit)
        print(response)
else:
    if completion.choices[0].message.content:
        print(completion.choices[0].message.content)
    else:
        print("No response from the model.")
