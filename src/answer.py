import os
import openai
from dotenv import load_dotenv

from vector_store.similarity_search import get_relevant_document

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_llm_answer(
    question: str, 
    prompter: str = "", 
    max_tokens: int = 1024
) -> str:
    relevant_docs = get_relevant_document(question)

    context = ""
    for doc in relevant_docs:
        context += doc
        context += "\n"

    if not prompter:
        prompter = f"""
                    จงบอก {question} จากเนื้อหาต่อไปนี้
                    เนื้อหา:
                    {context}
                    """
    
    completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompter}
                    ],
                    max_tokens=max_tokens
                )

    return completion.choices[0].message.content


question = "เรื่องย่อ moving"
ans = get_llm_answer(question=question)
print(ans)
