# 🚀 GraphRAG Workshops: Supercharge Your AI with Knowledge Graphs

[![Neo4j](https://img.shields.io/badge/Neo4j-5.0+-blue.svg)](https://neo4j.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

Welcome to the ultimate hands-on learning experience for **GraphRAG (Graph-based Retrieval-Augmented Generation)**! This repository contains two comprehensive workshops that will transform how you think about AI and knowledge representation.

🎯 **What is GraphRAG?** Imagine combining the structured reasoning power of knowledge graphs with the natural language capabilities of large language models. That's GraphRAG - a revolutionary approach that grounds AI responses in connected, contextualized data for more accurate, explainable, and powerful AI applications.

## 🎓 Workshops Overview

### 1. 👥 **[Talent Intelligence Workshop](talent)**

#### Transform HR and talent management with AI-powered insights

**🔍 What You'll Build:**

- A sophisticated talent intelligence system that understands skills, people, and their interconnections
- An AI agent capable of answering complex queries like "Find data scientists with machine learning experience similar to John's skillset"
- Advanced analytics to identify skill gaps, team compositions, and career progression paths

**📚 Learning Journey:**

- **Module 1**: Graph Fundamentals - Build your first knowledge graph from employee data
- **Module 2**: Unstructured Data Magic - Extract insights from resumes, job descriptions, and reviews
- **Module 3**: GraphRAG Agent - Create an intelligent talent assistant

**💡 Real-world Applications:**

- Talent acquisition and matching
- Skills gap analysis
- Team formation optimization
- Career development planning

### 2. 🛍️ **[Customers & Products Workshop](customers-and-products)**

#### Revolutionize e-commerce with personalized AI experiences

**🔍 What You'll Build:**

- A personalized marketing content generator using real H&M fashion retail data
- Advanced recommendation systems that understand customer behavior patterns
- Multi-modal retrieval strategies combining collaborative filtering, content-based recommendations, and graph analytics

**📚 Learning Experience:**

- **Complete Workshop**: [`genai-workshop.ipynb`](customers-and-products/genai-workshop.ipynb) - Your comprehensive learning journey
- **Follow-Along**: [`genai-workshop-w-outputs.ipynb`](customers-and-products/genai-workshop-w-outputs.ipynb) - Reference with outputs
- **Quick Demo**: [`genai-example-app-only.ipynb`](customers-and-products/genai-example-app-only.ipynb) - See the final application
- **Data Pipeline**: [`data-prep.ipynb`](customers-and-products/data-prep.ipynb) & [`data-load.ipynb`](customers-and-products/data-load.ipynb) - Behind-the-scenes data processing

**💡 Real-world Applications:**

- Personalized product recommendations
- Dynamic marketing content generation
- Customer behavior analysis
- Inventory optimization

## 🚀 Quick Start Guide

### Prerequisites

- 🐍 Python 3.8+
- 🗄️ Neo4j AuraDS account (free tier available)
- 🤖 OpenAI API key
- 📓 Jupyter notebook environment

### Option 1: 🌐 Online Jupyter Server (Recommended for Workshops)

Perfect for live workshops and quick exploration:

**Talent Workshop:**

- [Module 1: Graph Basics](https://raw.githubusercontent.com/neo4j-product-examples/genai-workshop/refs/heads/main/talent/module_01_graph_basics.ipynb)
- [Module 2: Unstructured Data](https://raw.githubusercontent.com/neo4j-product-examples/genai-workshop/refs/heads/main/talent/module_02_unstructured_data.ipynb)
- [Module 3: GraphRAG Agent](https://raw.githubusercontent.com/neo4j-product-examples/genai-workshop/refs/heads/main/talent/module_03_graphrag_agent.ipynb)

### Option 2: 💻 Local Development Setup

```bash
# Clone the repository
git clone https://github.com/neo4j-product-examples/genai-workshop.git
cd genai-workshop

# Set up your environment
cp customers-and-products/ws.env.template .env
# Edit .env with your credentials

# Install dependencies (done within notebooks)
jupyter notebook
```

### Option 3: ☁️ Cloud Deployment

Ready to deploy? Check out our Azure deployment guides in each workshop folder!

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Graph Database** | Neo4j AuraDS | Store and query connected data |
| **AI/ML** | OpenAI GPT-4 | Natural language understanding |
| **Vector Search** | Neo4j Vector Index | Semantic similarity search |
| **Orchestration** | LangChain | Chain AI components |
| **Data Processing** | Python + Pandas | Data manipulation |
| **Visualization** | Neo4j Browser | Interactive graph exploration |

## 🎯 Learning Outcomes

After completing these workshops, you'll master:

**📊 Graph Database Skills:**

- Design and implement knowledge graphs
- Write advanced Cypher queries
- Optimize graph performance

**🤖 AI Integration:**

- Build RAG applications with graph enhancement
- Implement vector similarity search
- Create intelligent AI agents

**🔄 GraphRAG Patterns:**

- Multi-hop reasoning
- Hybrid retrieval strategies
- Context-aware generation

**🚀 Production Deployment:**

- Scale GraphRAG applications
- Monitor and optimize performance
- Implement security best practices

## 🤝 Contributing to the Project

We ❤️ contributions! Whether you're fixing bugs, adding features, or sharing new ideas, your input makes this project better for everyone.

### 🌟 Ways to Contribute

#### 🐛 **Code Contributions**

- **Bug Fixes**: Found an issue? Submit a fix!
- **Performance Optimizations**: Make queries faster, reduce memory usage
- **New Features**: Add advanced GraphRAG techniques or integrations
- **Code Quality**: Improve error handling, add type hints, enhance documentation

#### 📚 **Content & Documentation**

- **New Workshops**: Create domain-specific workshops (healthcare, finance, education)
- **Advanced Tutorials**: Share complex GraphRAG patterns and techniques
- **Use Case Studies**: Document real-world implementations
- **Translation**: Help make content accessible in multiple languages

#### 🧪 **Testing & Quality Assurance**

- **Environment Testing**: Test on different Python/Neo4j versions
- **Notebook Validation**: Ensure all cells execute successfully
- **Performance Benchmarking**: Compare different approaches
- **Documentation Review**: Improve clarity and fix errors

#### 🎨 **Community & Outreach**

- **Blog Posts**: Write about your GraphRAG experiences
- **Video Tutorials**: Create step-by-step guides
- **Conference Talks**: Present at meetups and conferences
- **Social Media**: Share your projects and learnings

### 📋 Contribution Guidelines

#### **Before You Start**

1. 🔍 Check existing [issues](https://github.com/neo4j-product-examples/genai-workshop/issues) and [PRs](https://github.com/neo4j-product-examples/genai-workshop/pulls)
2. 💬 Join our [Discord community](https://discord.gg/neo4j) to discuss ideas
3. 📖 Read our [Code of Conduct](CODE_OF_CONDUCT.md)

#### **Making Changes**

1. **🍴 Fork & Clone**: Create your own fork and clone it locally
2. **🌿 Create Branch**: Use descriptive branch names (`feature/advanced-retrieval`, `fix/memory-leak`)
3. **✨ Make Changes**: Follow existing code style and patterns
4. **🧹 Clean Outputs**: If editing `genai-workshop.ipynb`, clear all outputs before committing
5. **✅ Test**: Ensure all notebooks run successfully from start to finish
6. **📝 Document**: Update README or add docstrings for new features

#### **Submitting Changes**

1. **📤 Push Branch**: Push your changes to your fork
2. **🔄 Create PR**: Submit a pull request with:
   - Clear, descriptive title
   - Detailed description of changes
   - Screenshots/examples if applicable
   - Link to related issues
3. **🔄 Respond to Reviews**: Address feedback promptly and thoughtfully

#### **Special Notes**

- 🚫 **Don't edit** `genai-workshop-w-outputs.ipynb` - it's auto-generated by GitHub Actions
- ✅ **Do test** your changes on both workshops before submitting
- 📸 **Include screenshots** for UI/visualization changes
- 🔗 **Reference issues** in your commit messages (`fixes #123`)

### 🏆 Recognition

Contributors are recognized in our:

- 📜 Contributors section (coming soon!)
- 🎉 Release notes for significant contributions
- 💫 Special shout-outs in community updates

## 📞 Community & Support

- 💬 **Discord**: [Join our community](https://discord.gg/neo4j)
- 🐛 **Issues**: [Report bugs or request features](https://github.com/neo4j-product-examples/genai-workshop/issues)
- 📧 **Discussions**: [Ask questions and share ideas](https://github.com/neo4j-product-examples/genai-workshop/discussions)
- 📖 **Documentation**: [Neo4j Developer Guides](https://neo4j.com/developer/)

---

**Ready to revolutionize your AI applications?** 🚀 Start with either workshop and join the GraphRAG revolution!


3. **[Financial Documents](financial_documents)**  
Learn how to ingest complex, unstructured financial documents (like 10-K filings) into a Neo4j knowledge graph. This workshop covers PDF parsing, data chunking, and building a GraphRAG pipeline to perform semantic search and answer complex questions about financial data and sets you up to understand GraphRAG across structured and unstructured data.



