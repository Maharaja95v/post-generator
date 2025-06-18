from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY","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"), model_name="llama-3.1-8b-instant")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)





