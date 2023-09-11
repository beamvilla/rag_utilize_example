import re
import os
from typing import List
import sys
sys.path.append("./")

from src.models.tokenizer import tokenizer


DOCS_DIR = "./docs"


def split_document(max_word: int = 100) -> List[str]:
    """
    Only accept .txt file (For demo)
    """
    doc_files_name = os.listdir(DOCS_DIR)
    contexts = []

    for doc_file_name in doc_files_name:
        if not doc_file_name.endswith(".txt"):
            raise ValueError("Not txt file format.")
        
        doc_path = os.path.join(DOCS_DIR, doc_file_name)

        doc_file = open(doc_path, "r").read()
        tokenized_docs = tokenizer(doc_file)

        text = ""
        word_cnt = 0
        for t in tokenized_docs:
            text += t
            word_cnt += 1

            if word_cnt == max_word:
                contexts.append(text)
                text = ""
                word_cnt = 0

    return contexts