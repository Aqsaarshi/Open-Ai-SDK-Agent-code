from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, set_default_openai_api, set_default_openai_client, set_tracing_disabled



my_Key = config("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=my_Key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)




set_tracing_disabled(True)         # isko jab disable kron gi jab guardrails chlaon gi tracing ky liy disable krna hoa 
set_default_openai_api("chat_completions")
set_default_openai_client(client)



MODEL = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client=client,
)