#!/usr/bin/env python3

import os
import lancedb
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import LanceDB


# Load environment variables
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'nomic-embed-text')
source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')
chunk_size = 5000
chunk_overlap = 50

loader = DirectoryLoader(source_directory, glob="**/*.md")

data = loader.load()

docs_transformed = [doc for doc in data if len(doc.page_content) > 10]

text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
all_splits = text_splitter.split_documents(docs_transformed)

print("# docs  = %d, # splits = %d" % (len(docs_transformed), len(all_splits)))

oembed = OllamaEmbeddings(base_url="http://localhost:11434", model=embeddings_model_name)
vectorstore = LanceDB.from_documents(documents=all_splits, embedding=oembed)

