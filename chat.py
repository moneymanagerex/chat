#!/usr/bin/env python3

import os
import lancedb

from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores import LanceDB
from langchain.chains import RetrievalQA

# Load environment variables
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'nomic-embed-text')
model = os.environ.get("MODEL", "gemma:7b")

ollama = Ollama(base_url='http://localhost:11434', model=model)

# default 
db = lancedb.connect("/tmp/lancedb/")
table = db.open_table('vectorstore')

oembed = OllamaEmbeddings(base_url="http://localhost:11434", model=embeddings_model_name)
vectorstore = LanceDB(table, embedding=oembed)

from langchain.chains import RetrievalQA
qachain=RetrievalQA.from_chain_type(ollama, chain_type="stuff", retriever=vectorstore.as_retriever(), return_source_documents = True)

while True:
    user_input = input("Enter a question: ")
    if not user_input:
        exit()

    result = (qachain.invoke({"query": user_input}))

    # Print the result
    print("\n\n> Question:")
    print(user_input)
    print("\n")
    print(result['result'])
    print("\n\n")
