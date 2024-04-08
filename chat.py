#!/usr/bin/env python3

import os
import lancedb

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import LanceDB
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# Load environment variables
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'nomic-embed-text')
model = os.environ.get("MODEL", "gemma:7b")

ollama = Ollama(base_url='http://localhost:11434', model=model)

# default 
db = lancedb.connect("/tmp/lancedb/")
table = db.open_table('vectorstore')

oembed = OllamaEmbeddings(base_url="http://localhost:11434", model=embeddings_model_name)
vectorstore = LanceDB(table, embedding=oembed)

from langchain.retrievers.multi_query import MultiQueryRetriever
# Set logging for the queries
import logging

logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

retrieval_qa_chat_prompt = ChatPromptTemplate.from_messages(
    [("system", "Answer any use questions based solely on the context below:\n\n{context}")]
)
combine_docs_chain = create_stuff_documents_chain(ollama, retrieval_qa_chat_prompt)

retriever = MultiQueryRetriever.from_llm(retriever=vectorstore.as_retriever(), llm=ollama, include_original = True)
qachain = create_retrieval_chain(retriever, combine_docs_chain)

while True:
    user_input = input("Enter a question: ")
    if not user_input:
        exit()

    result = (qachain.invoke({"input": user_input}))

    # Print the result
    print("\n\n> Question:")
    print(user_input)
    print("\n")
    print(result['answer'])
    print("\n\n")
