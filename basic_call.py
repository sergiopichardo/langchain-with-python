import os
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()



def run(input: str):
    model = ChatOpenAI(
        openai_api_key=os.getenv('OPENAI_API_KEY'),
        temperature=0.1
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful and honest AI model"),
        ("user", "{input}")
    ])

    output_parser = StrOutputParser()
    
    chain = prompt | model | output_parser

    return chain.invoke({"input": input})

result = run("What is the capital of France?")

print(result)
    



