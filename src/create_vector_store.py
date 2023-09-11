from vector_store import vector_store
from document_spliter.spliter import split_document


contexts = split_document()

print("🚧 CREATING VECTOR STORES ...")
vector_store.create(contexts=contexts)
print("DONE. ✅✅✅")