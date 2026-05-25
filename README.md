# Generative AI and LangChain Advanced Exploration Toolkit

## Project Overview
This repository serves as a modular blueprint and experimental workbench for building production-ready Retrieval-Augmented Generation (RAG) pipelines and advanced Language Model (LLM) workflows. The codebase focuses on mastering the crucial phases of any Generative AI architecture: document ingestion, precision chunking strategies, vector database management, and structured response orchestration using the LangChain framework.

The primary objective of this toolkit is to demonstrate how unstructured corporate or private data (such as PDFs, CSVs, and plain text) can be efficiently processed, indexed, and retrieved to minimize LLM hallucinations and optimize context-window constraints.

---

## Core Project Architecture
The project is strictly organized into decoupled, production-like modules. Each directory isolates a specific responsibility within the GenAI engineering lifecycle:

### 1. Document Loaders (`Document_loaders/`)
Responsible for raw data ingestion from varied file formats into standardized LangChain Document schemas, capturing both raw text content and vital source metadata.
* `text_loader.py`: Ingests raw text files and integrates an LLM chain for automatic post-load summarization.
* `pdf_loader.py`: Handles complex PDF structure processing, keeping page-level metadata intact.
* `csv_loader.py` & `webbase_loader.py`: Extends ingestion pipelines to structured tabular data and live web scraping interfaces.
* `directory_loader.py`: Orchestrates multi-file bulk uploads from local directories utilizing recursive pattern matching.

### 2. Advanced Text Splitters (`Text_splitters/`)
Focuses on chunking large datasets to fit token restrictions while maintaining structural and contextual semantic cohesion.
* `length_based.py`: Demonstrates basic character-count splitting barriers.
* `text_structure_based.py`: Utilizes recursive character analysis to avoid breaking sentences across paragraph bounds.
* `python_code_splitting.py`: Custom syntax-aware splitter that respects Python class and function indentations to keep code fragments executable.
* `markdown_splitting.py`: Sections documentation organically based on Markdown heading hierarchies (H1, H2, H3).
* `semantic_meaning_based.py`: The most advanced chunking approach, leveraging OpenAI embedding distances and statistical standard deviation thresholds to divide text purely when the topic shifts.

### 3. Vector Storage and CRUD Operations (`Vector_stores/`)
Manages persistent semantic indexation, storage, and precise high-speed retrieval of high-dimensional data arrays.
* `chroma.py`: A comprehensive guide to ChromaDB infrastructure showcasing deep vector operations: converting documents to embeddings, data persistence, multi-attribute metadata filtering, runtime data updates, and vector removal.

### 4. Enterprise Components (`Chains/`, `Retrievers/`, `Structured_output/`, `Prompts/`, `Output_parser/`)
* `Chains/`: Demonstrates LangChain Expression Language (LCEL) routing including Sequential, Parallel, and Conditional chain execution.
* `Retrievers/`: Implements sophisticated filtering algorithms like Maximal Marginal Relevance (MMR), Multi-Query expansion, and Contextual Compression to isolate only high-relevance chunks.
* `Structured_output/`: Enforces rigorous schema control using Pydantic validation frameworks and TypeDict models to ensure predictable JSON outputs from unstructured model completions.

---

## Technology Stack
* Framework Core: LangChain, LangChain-Community, LangChain-Experimental
* Vector Database: ChromaDB
* Underlying Models: OpenAI API (GPT models and text-embedding-ada-002)
* Configuration: Python-dotenv

---

## Installation and Setup Instructions

### 1. Prerequisites
Ensure you have Python 3.10 or higher installed on your local environment.

### 2. Clone the Repository
Execute the following commands in your terminal to clone the repository and navigate to the project root directory:
```bash
git clone [https://github.com/00jangidmahesh-web/Generative-AI-Advanced-Toolkit.git](https://github.com/00jangidmahesh-web/Generative-AI-Advanced-Toolkit.git)
cd Generative-AI-Main
