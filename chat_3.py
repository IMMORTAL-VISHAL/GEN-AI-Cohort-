from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolves the user query.

For the given user Input analyse the input and break down the problem step by step.
At least think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final result.

Follow these steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per output schema.
2. Always perform one step at a time and wait for next input.
3. Carefully analyse the user query

Output Format:
{{ step: "string", content: "string"}}

Example:
Input: What is 2 + 2.
Output: {{ step : "analyse", content : "Alright! The user is interested in maths query and he is asking the basic arithmetic question."}}
Output : {{ step : "think", content : "To perform the addition i must go from left to right and following and add all the operands."}}
Output : {{ step : "output" , content : "4"}}
Output : {{ step : "validate", content : "seems like 4 is correct answer for 2 + 2"}}
Output : {{ step : "result", content : "2 + 2 = 4 and that is calculating by adding all numbers"}}
"""

result = client.chat.completions.create(
    model="gpt-4o",
    response_format={ "type": "json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "what is  3 + 4 * 5"}
        
        
    ]
)

print(result.choices[0].message.content)