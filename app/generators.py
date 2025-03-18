from openai import AsyncOpenAI
from config import TOKEN

client = AsyncOpenAI(api_key=TOKEN)

async def gpt4(question):
    response = await client.chat.completions.create(
        messages=[{"role": "user",
                   "content": str(question)}],
        model="gpt-4o"
    )
    return response