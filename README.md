# Chat with your Money Manager EX (MMEX) data
This is inspired by [PrivateGPT](here](https://github.com/imartinez/privateGPT), and [Ollama](https://ollama.com/)'s [RAG example](https://github.com/ollama/ollama/edit/main/examples/langchain-python-rag-privategpt)

### Goal
The goal is to build a high-quality QA and assistant system around public and private data

### Document sources
so far, all data source includes:
* MMEX [homesite repo](https://github.com/moneymanagerex/moneymanagerex.github.io)
* MMEX doc for [Desktop repo](https://github.com/moneymanagerex/moneymanagerex)
* MMEX doc for [android repo](https://github.com/moneymanagerex/android-money-manager-ex)
* MMEX4Desktop [repo issues](https://github.com/moneymanagerex/moneymanagerex/issues?q=is%3Aissue+is%3Aclosed)
* MMEX4Android [repo issues](https://github.com/moneymanagerex/android-money-manager-ex/issues?q=is%3Aissue+is%3Aclosed)
  
and here are some todos
* MMEX [forum](https://forum.moneymanagerex.org/)
* MMEX Social networks
* MMEX transaction data from Desktop and Android applications,
  - private data.
  - SQLite3 with encryption 

### Setup

##### install `Ollama`

```
ollama pull llama3:8b
ollama pull nomic-embed-text:latest
```

#### ingest & run
```
git clone git@github.com:moneymanagerex/chat.git
git submodule update --init
cd chat
python3 ingest.py
python3 chat.py
```


### Stacks 
* `Ollama` as inference framework
* `llama3:8b` as LLM, configurable via `MODEL`
* `nomic-embed-text` as an embedding model, configurable via `EMBEDDINGS_MODEL_NAME`
* `LangChain` as the application framework 
