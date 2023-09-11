import os
from typing import List

from langchain.vectorstores import Chroma
from chromadb.config import Settings

from models.text_embedding import text_embedding_model


PERSIST_DIRECTORY = f"./DB"

# Define the Chroma settings
chroma_setting = Settings(
    chroma_db_impl="duckdb+parquet", 
    persist_directory=PERSIST_DIRECTORY, 
    anonymized_telemetry=False
)


def create(contexts: List[str]) -> None:
    db = Chroma.from_texts(
            contexts,
            text_embedding_model,
            persist_directory=PERSIST_DIRECTORY,
            client_settings=chroma_setting,
        )
    db.persist()
    db = None


def load() -> Chroma:
    db = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=text_embedding_model,
        client_settings=chroma_setting,
    )
    return db