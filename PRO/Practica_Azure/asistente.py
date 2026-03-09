from openai import OpenAI

endpoint = "https://openai-riano.openai.azure.com/openai/v1"
deployment_name = "gpt4o-practica"
api_key = "ngHaMVWIOPiiVctNqwQEnb7qMlt98z7QjoOL8MIlm3KfvrYJTcLGJQQJ99CCACfhMk5XJ3w3AAAAACOGD2Q9"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(completion.choices[0].message)