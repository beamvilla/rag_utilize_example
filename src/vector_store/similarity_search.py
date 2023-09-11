from typing import List

from vector_store import vector_store


print("Loading Vector store ...")
db = vector_store.load()
print("Vector store loaded.\n")


def get_relevant_document(question: str) -> List[str]:
    docs = db.similarity_search(question)
    docs_text = [doc.page_content for doc in docs]
    return docs_text