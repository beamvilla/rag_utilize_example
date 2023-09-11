from langchain.embeddings import HuggingFaceInstructEmbeddings


text_embedding_model = HuggingFaceInstructEmbeddings(
                            model_name="distiluse-base-multilingual-cased-v2",
                            model_kwargs={"device": "cuda"},
                        )