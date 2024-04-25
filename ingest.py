#!/usr/bin/env python3

import os
import duckdb 
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import GitHubIssuesLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import DuckDB

# Load environment variables
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'nomic-embed-text')
source_directory = os.environ.get('SOURCE_DIRECTORY', 'source_documents')
chunk_size = 500
chunk_overlap = 50

loaders = [DirectoryLoader(source_directory, glob="**/*.md", show_progress=True) ,DirectoryLoader(source_directory + "/moneymanagerex/docs/en_US/", glob="**/*.html", show_progress=True)]
loaders.extend([GitHubIssuesLoader(repo="moneymanagerex/android-money-manager-ex", include_prs=False, show_progress=True, state='closed'), GitHubIssuesLoader(repo="moneymanagerex/moneymanagerex", include_prs=False, show_progress=True, state='closed')])

docs = []
for loader in loaders:
    docs.extend(loader.load())

docs_transformed = [doc for doc in docs if len(doc.page_content) > 10]

text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
all_splits = text_splitter.split_documents(docs_transformed)

print("# docs  = %d, # splits = %d" % (len(docs_transformed), len(all_splits)))

oembed = OllamaEmbeddings(base_url="http://localhost:11434", model=embeddings_model_name)

conn = duckdb.connect(database='./db/duck.db',
    config={
        }
)
vectorstore = DuckDB(connection=conn, embedding=oembed)
vectorstore.add_documents(all_splits)
