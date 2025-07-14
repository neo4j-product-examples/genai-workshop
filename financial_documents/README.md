# Neo4j GraphRAG Workshop

This repository contains all code, data, and notebooks for the Neo4j GraphRAG workshop. It provides a step-by-step guide to building a Retrieval-Augmented Generation (RAG) system using Neo4j, OpenAI, LangChain, and real-world financial filings.

---

## 📖 Project Overview
- Ingest and model company, filing, and holdings data as a knowledge graph in Neo4j
- Run retrieval-augmented queries and semantic search over filings and financial data
- Use Jupyter notebooks for hands-on experimentation

---

## 📂 Project Structure
- `01_PDF_Loader_for_Neo4j_GraphRAG.ipynb` — Loads PDF and CSV data into Neo4j, builds the graph, and creates vector embeddings
- `02_Retreivers_notebook.ipynb` — Interactive notebook for querying the graph, running RAG workflows, and experimenting with retrieval
- `03_Neo4j_agent_notebook.ipynb` — (Optional) Agent-based exploration and advanced workflows
- `data/` — Contains:
    - `Asset_Manager_Holdings.csv`, `Company_Filings.csv`: Sample data files
    - `form10k-sample/`: Example 10-K filings for graph ingestion
- `Additional_Info/` — (Optional) Additional scripts and explained notebooks
- `.env.sample` — Template for required environment variables

---

## 🛠️ Setup Instructions
1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables:**
   - Copy `.env.sample` to `.env` and fill in:
     - `OPENAI_API_KEY`
     - `NEO4J_URI`, `NEO4J_USERNAME`, `NEO4J_PASSWORD`
4. **Start Neo4j AuraDB** (see workshop materials for connection details)
5. **Run the loader notebook** (`01_PDF_Loader_for_Neo4j_GraphRAG.ipynb`) to ingest data
6. **Open `02_Retreivers_notebook.ipynb`** to run retrievals and explore the graph

---

## 📊 Data Files
- All sample data used in the workshop is in the `data/` directory
- You may add or replace files in `form10k-sample/` as needed for your experiments

---

## 📝 Notes
- **Never commit secrets** — `.env` is in `.gitignore`
- Use Jupyter or VS Code for interactive exploration
- All notebooks are designed to be run step-by-step as described in the workshop

---

## 📚 Resources
- [Neo4j AuraDB](https://console.neo4j.io/)
- [OpenAI API](https://platform.openai.com/)
- [LangChain Docs](https://python.langchain.com/docs/)
- [Neo4j Python Driver](https://neo4j.com/docs/api/python-driver/current/)

---

For questions or help, open an issue in this repo.
