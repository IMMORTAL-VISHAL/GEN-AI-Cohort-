import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def get_weather(city:str):
    #TODO!: Do an actual API Call
    return "31 Degree celcius"

available_tools = {
    "get_weather":{
        "fn": get_weather,
        "description": "Takes a city name as an input and return the current weather for the city"
    }
}

system_prompt = f"""
You are an helpfull AI Assistant who is specialized in resolving user query.
You work on start, Plan, action, observe mode.
For the given user query and available tools, plan the step by step execution, based on the planning, select the relevant tool from the available tool. and based on the tool selection you perform an action to call the tool.
Wait for the observation and based on the observation from the tool call resolve the user query.

Rules:
1. Follow the Output JSON Format.
2. Always perform one step at a time and wait for next input.
3. Carefully analyse the user query

Output JSON Format:
{{
    "step": "string",
    "content": "string",
    "function": "The name of function if the step is action",
    "input": "The input parameter for the function", 
}}

Available Tools:
- get_weather: Takes a city name as an input and returns the current weather for the city

Example:
User Query: What is the weather of new york?
Output: {{ "step": "plan", "content": "The user is interseted in weather data of new york"}}
Output: {{ "step": "plan", "content": "From the available tools I should call get_weather"}}
Output: {{ "step": "action", "function": "get_weather", "input":"new york"}}
Output: {{ "step": "observe", "output": "12 Degree Cel"}}
Output: {{ "step": "output", "content": "The weather for new york seems to be 12 degrees."}}
"""

messages = [
    { "role": "system", "content": system_prompt}
]

user_query = input('> ')
messages.append({ "role": "user", "content":user_query})
while True:
    response = client.completions.create(
        model="gpt-4o",
        response_format={"type":"json_object"},
        messages=messages
    )
    
    parsed_output = json.loads(response.choices[0].message.content)
    messages.append({ "role": "assistant", "content": json.dumps(parsed_output) })
    
    if parsed_output.get("step") == "plan":
        print(f"🧠:{parsed_response.get("content")} ")
        continue
    
    if parsed_output.get("step") == "action":
        tool_name = parsed_output.get("function")
        tool_input = parsed_output.get("input")
        
        if available_tools.get(tool_name, False) != False:
            output = available_tools[tool_name].get("fn")(tool_input)
            messages.append({ "role": "assistant", "content": json.dumps({ "step": "observe", "output": output})})
            continue
        
    if parsed_output.get("step") == "output":
        print(f"🤖:{parsed_response.get("content")}")
        break
    

# response = client.completions.create(
#     model="gpt-4o",
#     response_format={"type": "json_object"},
#     message = [
#         {"role": "system", "content": system_prompt},
#         {"role": "user", "content": "What is the current weather in Mathura?"},
#         { "role": "assistant", "content": json.dumps({"step": "plan", "content": "The user is interseted in weather data of new york"})}
#     ]
# )

# print(response.choices[0].message['content'])