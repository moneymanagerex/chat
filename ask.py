#!/usr/bin/env python3

import os
import duckdb

from mmex import create_mmexdbretriever

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# Load environment variables
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'nomic-embed-text')
model = os.environ.get("MODEL", "llama3:8b")

ollama = ChatOllama(base_url='http://localhost:11434', model=model)

toy_retriever = create_mmexdbretriever()

from langchain.retrievers import EnsembleRetriever
ensemble_retriever = EnsembleRetriever(
    retrievers=[toy_retriever], weights=[1]
)

# https://smith.langchain.com/hub/rlm/rag-prompt
retrieval_qa_chat_prompt = ChatPromptTemplate.from_messages(
    [("system", """You are an assistant for question-answering tasks. Use the following pieces of context in JSON format to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
Question: {input}
Context: {context}
Answer:""")]
)
combine_docs_chain = create_stuff_documents_chain(ollama, retrieval_qa_chat_prompt)

qachain = create_retrieval_chain(ensemble_retriever, combine_docs_chain)

while True:
    user_input = input("Enter a question: ")
    if not user_input:
        exit()

    print("\n")
    result = (qachain.invoke({"input": user_input}))

    # Print the result
    print("\n\n> Question:")
    print(user_input)
    print("\n\n> Answer:")
    print(result['answer'])
    print("\n\n")
