# Neo4j GenAI Workshop

Please see [`genai-workshop.ipynb`](genai-workshop.ipynb) which serves as the self-contained workshop. 

The other companion notebooks contain code for staging data, building the Neo4j Graph, and providing easy access to demos:
1. [`data-prep.ipynb`](data-prep.ipynb) stages the workshop data, sampling and formatting data sourced from the [H&M Personalized Fashion Recommendations Dataset](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data).
2. [`data-load.ipynb`](data-load.ipynb) loads the staged data into Neo4j, performs text embedding, and creates a vector index.
3. [`genai-example-app-only.ipynb`](genai-example-app-only.ipynb) is a copy of [`genai-workshop.ipynb`](genai-workshop.ipynb)  that contains only the final section: the demo LLM GraphRAG app for content generation. It assumes you have already run [`genai-workshop.ipynb`](genai-workshop.ipynb), and exists only for instructor demo purposes.