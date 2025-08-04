# :file_folder: RAG AI Assistant

---

## Project Name

**Repository:** `rag-ai-assistant`

## Description

RAG AI Assistant is a modular Retrieval-Augmented Generation (RAG) system designed for advanced document-based question answering and information retrieval. The assistant leverages a vector database (PostgreSQL with pgvector) to store and search document embeddings, enabling efficient and context-aware responses. It supports multiple chat and embedding models, with a flexible architecture for integrating new model families.

A key component of the project is a document conversion pipeline that processes DOCX and PDF files through cleaning, conversion, enrichment, and export steps. This pipeline prepares documents for embedding and retrieval, but the main focus is on the AI assistant's ability to answer questions and interact with users based on the ingested knowledge.

## Technologies Used

- Python (3.12.3)
- PostgreSQL (with pgvector extension)
- OpenAI models (chat & embedding)
- Document processing libraries (e.g., python-docx, docx, docling, unstructured, bs4, xml.etree.ElementTree)
- Utility and system libraries (argparse, base64, json, os, re, time, pathlib)
- Concurrency and functional tools (concurrent.futures.ThreadPoolExecutor, functools.partial)
- Type hints (typing)
- OpenAI API (openai, tenacity)

## Main Classes

## Features

- RAG-based AI assistant for document Q&A
- Vector database storage and semantic search (PostgreSQL + pgvector)
- Modular model integration (multiple chat/embedding models via class methods)
- Configurable chunking and overlap for document embeddings
- Multi-step document conversion pipeline (cleaning, conversion, enrichment, export)
- Automatic summarization of images and tables using LLM models (e. g. OpenAI API)

## Installation

1. Install PostgreSQL and pgvector extension
2. Set up Python environment and install dependencies
3. Configure OpenAI API keys and database connection

```bash
# Example
pip install -r requirements.txt
# Set up PostgreSQL and pgvector
```

## Usage

1. Ingest DOCX or TXT documents using the conversion pipeline
2. Generate and store embeddings in the vector database
3. Interact with the AI assistant via chat interface for document-based Q&A
4. Extend with new chat or embedding models as needed

## Screenshots

## License

MIT License
