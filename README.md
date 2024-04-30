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

### Stats
```
D .tables
vectorstore
D select * from vectorstore;
┌──────────────────────┬──────────────────────┬──────────────────────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│          id          │         text         │      embedding       │                                                                                                                     metadata                                                                                                                     │
│       varchar        │       varchar        │       float[]        │                                                                                                                     varchar                                                                                                                      │
├──────────────────────┼──────────────────────┼──────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 05a3f1f4-43b3-4ea3…  │ Installing Money M…  │ [1.3362232, 1.0252…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ 89fa3ee2-68d1-450a…  │ Use unstable pre-r…  │ [-0.1654804, -0.31…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ 8d6a3b4f-da25-42af…  │ To try the latest …  │ [0.32451722, 0.691…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ 7ccacacb-12eb-40f4…  │ You must have perm…  │ [0.43995818, 1.276…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ 45abaa3b-9399-4fd2…  │ MMEX can be starte…  │ [-0.42747283, 1.05…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ 8f8c1f4a-1144-44eb…  │ MMEX developers cr…  │ [-0.43720704, 2.03…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ dd2c1b20-dbc5-4361…  │ You can add MMEX r…  │ [0.10934828, 1.452…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ e92c0a97-c0d5-4660…  │ You can use packag…  │ [-0.15496743, 1.42…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ 97688e60-e61f-4746…  │ Use unstable pre-r…  │ [0.10321432, -0.42…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ 71bb8c43-068c-45d0…  │ Distribution Insta…  │ [0.8691554, 1.1287…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ 770643c8-167d-4a9f…  │ Slackware requires…  │ [-0.09068614, 1.21…  │ {"source": "source_documents/moneymanagerex/INSTALL.md"}                                                                                                                                                                                         │
│ e746c265-ed0d-4585…  │ Money Manager Ex (…  │ [0.3924375, 2.1113…  │ {"source": "source_documents/moneymanagerex/README.md"}                                                                                                                                                                                          │
│ d1a6dde1-a2b1-44e3…  │ Features\n\nFast, …  │ [0.7776978, 0.2996…  │ {"source": "source_documents/moneymanagerex/README.md"}                                                                                                                                                                                          │
│ 82a8e2fc-0ce9-4ca0…  │ Custom Reports\n\n…  │ [0.4158724, 1.2726…  │ {"source": "source_documents/moneymanagerex/README.md"}                                                                                                                                                                                          │
│ f75a8751-5e1d-488f…  │ Download developme…  │ [0.8128123, 0.9333…  │ {"source": "source_documents/moneymanagerex/README.md"}                                                                                                                                                                                          │
│ 46366c03-838f-4d65…  │ Download dozens of…  │ [0.2653921, 0.3419…  │ {"source": "source_documents/moneymanagerex/README.md"}                                                                                                                                                                                          │
│ 64964839-0dc1-4a50…  │ Building Money Man…  │ [0.47461718, 0.737…  │ {"source": "source_documents/moneymanagerex/BUILD.md"}                                                                                                                                                                                           │
│ 8882371d-d4ed-4bed…  │ Older versions of …  │ [0.5182575, 0.3229…  │ {"source": "source_documents/moneymanagerex/BUILD.md"}                                                                                                                                                                                           │
│ 595562ea-8f5c-440c…  │ Download wxWidgets…  │ [0.1364667, 0.7587…  │ {"source": "source_documents/moneymanagerex/BUILD.md"}                                                                                                                                                                                           │
│ d67a37f5-7ca5-46bc…  │ Or start the follo…  │ [-0.30819768, 0.14…  │ {"source": "source_documents/moneymanagerex/BUILD.md"}                                                                                                                                                                                           │
│          ·           │          ·           │          ·           │                           ·                                                                                                                                                                                                                      │
│          ·           │          ·           │          ·           │                           ·                                                                                                                                                                                                                      │
│          ·           │          ·           │          ·           │                           ·                                                                                                                                                                                                                      │
│ ccb7680b-4ce0-4528…  │ make: **\* [mmex_a…  │ [0.027516425, 1.16…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/268", "title": "build errors due to unimplemented compiler features", "creator": "howff", "created_at": "2014-11-06T14:45:44Z", "comments": 2, "state": "closed", "labels": […  │
│ b7ddffc8-c455-41f3…  │ using this compile…  │ [0.35747665, 1.180…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/268", "title": "build errors due to unimplemented compiler features", "creator": "howff", "created_at": "2014-11-06T14:45:44Z", "comments": 2, "state": "closed", "labels": […  │
│ 2452cca4-94ab-4d1d…  │ Configured with: .…  │ [1.5434697, 0.8948…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/268", "title": "build errors due to unimplemented compiler features", "creator": "howff", "created_at": "2014-11-06T14:45:44Z", "comments": 2, "state": "closed", "labels": […  │
│ 60ee3079-e383-46ee…  │ --enable-clocale=g…  │ [0.17030136, 0.710…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/268", "title": "build errors due to unimplemented compiler features", "creator": "howff", "created_at": "2014-11-06T14:45:44Z", "comments": 2, "state": "closed", "labels": […  │
│ 139e73fd-1b1f-4c91…  │ Thread model: posi…  │ [0.5815328, 0.7802…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/268", "title": "build errors due to unimplemented compiler features", "creator": "howff", "created_at": "2014-11-06T14:45:44Z", "comments": 2, "state": "closed", "labels": […  │
│ 231cf5ee-a86f-4728…  │ The latest moneyma…  │ [0.43270323, 1.058…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/267", "title": "build errors with wxsqlite3", "creator": "howff", "created_at": "2014-11-06T11:43:47Z", "comments": 1, "state": "closed", "labels": [], "assignee": "guanlish…  │
│ b8c98299-717b-455f…  │ /users/local/arb/D…  │ [0.68784934, 1.547…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/267", "title": "build errors with wxsqlite3", "creator": "howff", "created_at": "2014-11-06T11:43:47Z", "comments": 1, "state": "closed", "labels": [], "assignee": "guanlish…  │
│ 74a4723a-fd86-4700…  │ -I/tmp/wx/include/…  │ [0.49969104, 0.701…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/267", "title": "build errors with wxsqlite3", "creator": "howff", "created_at": "2014-11-06T11:43:47Z", "comments": 1, "state": "closed", "labels": [], "assignee": "guanlish…  │
│ ed116182-f3d4-4795…  │ In file included f…  │ [1.181249, 0.69745…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/267", "title": "build errors with wxsqlite3", "creator": "howff", "created_at": "2014-11-06T11:43:47Z", "comments": 1, "state": "closed", "labels": [], "assignee": "guanlish…  │
│ ab5f9bf3-54e5-4e2e…  │ ../lib/wxsqlite3/s…  │ [1.0540159, 0.3316…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/267", "title": "build errors with wxsqlite3", "creator": "howff", "created_at": "2014-11-06T11:43:47Z", "comments": 1, "state": "closed", "labels": [], "assignee": "guanlish…  │
│ 19c20522-12dc-4379…  │ ../lib/wxsqlite3/s…  │ [1.1983867, 0.8891…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/267", "title": "build errors with wxsqlite3", "creator": "howff", "created_at": "2014-11-06T11:43:47Z", "comments": 1, "state": "closed", "labels": [], "assignee": "guanlish…  │
│ 37eb40b5-237c-4db1…  │ I tried an older r…  │ [0.49104393, 0.446…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/267", "title": "build errors with wxsqlite3", "creator": "howff", "created_at": "2014-11-06T11:43:47Z", "comments": 1, "state": "closed", "labels": [], "assignee": "guanlish…  │
│ fd957a6a-264e-4102…  │ Hi,\n\nI tried to …  │ [-0.23018059, 0.19…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/266", "title": "error: cannot convert 'const wxString' to 'const char*' for argument '2' to 'void", "creator": "jeancf", "created_at": "2014-11-05T13:53:57Z", "comments": 15…  │
│ ddf9b615-e035-40c8…  │ # gcc -v\nUsing bu…  │ [0.61500555, 1.437…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/266", "title": "error: cannot convert 'const wxString' to 'const char*' for argument '2' to 'void", "creator": "jeancf", "created_at": "2014-11-05T13:53:57Z", "comments": 15…  │
│ 55025176-23e9-408f…  │ Configured with: .…  │ [0.6909208, 1.3932…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/266", "title": "error: cannot convert 'const wxString' to 'const char*' for argument '2' to 'void", "creator": "jeancf", "created_at": "2014-11-05T13:53:57Z", "comments": 15…  │
│ 26ab740b-a53e-4ccc…  │ --with-system-zlib…  │ [0.58594024, 0.361…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/266", "title": "error: cannot convert 'const wxString' to 'const char*' for argument '2' to 'void", "creator": "jeancf", "created_at": "2014-11-05T13:53:57Z", "comments": 15…  │
│ 3bb3a317-498d-493a…  │ Thread model: posi…  │ [0.3381843, 0.5102…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/266", "title": "error: cannot convert 'const wxString' to 'const char*' for argument '2' to 'void", "creator": "jeancf", "created_at": "2014-11-05T13:53:57Z", "comments": 15…  │
│ 988a53c3-ad35-42c7…  │ When opening a dat…  │ [0.7069199, 0.6275…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/256", "title": "assertion failed (datetime)", "creator": "howff", "created_at": "2014-10-31T13:02:34Z", "comments": 6, "state": "closed", "labels": ["bug"], "assignee": "gua…  │
│ b5859c79-009e-4b48…  │ BACKTRACE:\n[1] wx…  │ [0.48446056, -0.02…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/256", "title": "assertion failed (datetime)", "creator": "howff", "created_at": "2014-10-31T13:02:34Z", "comments": 6, "state": "closed", "labels": ["bug"], "assignee": "gua…  │
│ e83a762a-3187-48cb…  │ There is a problem…  │ [1.4988081, 1.3917…  │ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/182", "title": "Transaction report filter", "creator": "Joker2k", "created_at": "2014-08-22T10:47:56Z", "comments": 0, "state": "closed", "labels": ["bug", "fixed"], "assign…  │
├──────────────────────┴──────────────────────┴──────────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 10096 rows (40 shown)                                                                                                                                                                                                                                                                                       4 columns │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
D select metadata, count(*) from vectorstore group by 1 order by 2 desc limit 10;
┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┬──────────────┐
│                                                                                                                                                metadata                                                                                                                                                │ count_star() │
│                                                                                                                                                varchar                                                                                                                                                 │    int64     │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────────────┤
│ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/5253", "title": "trash icon is missing", "creator": "vomikan", "created_at": "2022-10-30T10:05:31Z", "comments": 3, "state": "closed", "labels": ["bug", "solution found", "win"], "assignee": "vomikan", "milestone": null, "locke…  │          471 │
│ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/2405", "title": "Crash if app killed in tray", "creator": "vomikan", "created_at": "2020-04-22T20:08:36Z", "comments": 3, "state": "closed", "labels": ["bug", "mac"], "assignee": "whalley", "milestone": null, "locked": false, "…  │          162 │
│ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/3367", "title": "Crashing while clicking on the reports section entries", "creator": "MartinX3", "created_at": "2021-05-03T09:23:25Z", "comments": 5, "state": "closed", "labels": ["bug", "duplicate"], "assignee": "vomikan", "mi…  │          149 │
│ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/6397", "title": "crash on start", "creator": "pepebassan", "created_at": "2023-12-28T10:16:24Z", "comments": 5, "state": "closed", "labels": ["bug", "fixed", "mac"], "assignee": "whalley", "milestone": "v1.7.0", "locked": false…  │          144 │
│ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/1440", "title": "OSX : Cannot run application - MMEX quit unexpectedly", "creator": "ahmadsyamim", "created_at": "2018-02-13T03:10:19Z", "comments": 2, "state": "closed", "labels": ["outdated", "mac"], "assignee": null, "milest…  │          139 │
│ {"source": "source_documents/moneymanagerex/docs/en_US/index.html"}                                                                                                                                                                                                                                    │          130 │
│ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/2399", "title": "Constant crashing with a Debug report window", "creator": "feimosi", "created_at": "2020-04-20T11:05:21Z", "comments": 10, "state": "closed", "labels": ["bug", "duplicate", "linux"], "assignee": null, "mileston…  │          129 │
│ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/1811", "title": "\"Budget Setup\" crash", "creator": "ovari", "created_at": "2018-09-07T12:33:54Z", "comments": 5, "state": "closed", "labels": ["outdated", "linux"], "assignee": null, "milestone": null, "locked": false, "numbe…  │          119 │
│ {"url": "https://github.com/moneymanagerex/moneymanagerex/issues/3437", "title": "Run MMEX 1.5.1 on Mac OS High Sierra 10.13.6", "creator": "filiperivelli", "created_at": "2021-05-13T21:12:20Z", "comments": 4, "state": "closed", "labels": ["fixed", "mac"], "assignee": "whalley", "milestone":…  │          113 │
│ {"url": "https://github.com/moneymanagerex/android-money-manager-ex/issues/1225", "title": "Payees report crashes app on Android 8.1", "creator": "heitkergm", "created_at": "2018-04-03T01:15:41Z", "comments": 2, "state": "closed", "labels": ["reports"], "assignee": null, "milestone": null, "…  │          111 │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴──────────────┤
│ 10 rows                                                                                                                                                                                                                                                                                                     2 columns │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
  
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
* `Duckdb` as vector database
* `LangChain` as the application framework 
