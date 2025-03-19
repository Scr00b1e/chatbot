from openai import OpenAI
from config import ORTOKEN

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=ORTOKEN,
)

completion = client.chat.completions.create(
  model="deepseek/deepseek-chat",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)