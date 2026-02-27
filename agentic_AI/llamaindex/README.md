Uses LlamaIndex for:
- sync/async streaming and non-streaming query, chat [X]
- RAG (TODO)
- Agentic AI (TODO)

Steps:
1. Initialize virtual env using uv: `uv init`
2. Manage dependencies: `uv add llama-index-llms-openai llama-index-llms-openai llama-index-llms-google-genai jupyterlab python-dotenv`
3. Confirm the libraries: `uv tree --depth 1`
llamaindex v0.1.0
├── jupyterlab v4.5.5
├── llama-index-embeddings-openai v0.5.1
├── llama-index-llms-google-genai v0.8.7
├── llama-index-llms-openai v0.6.21
└── python-dotenv v1.2.1
4. To try notebook using Jupyterlab: `uv run jupyter lab`
5. Execute: `uv run llamaindex_main.py`

External resources:
- Local model: `docker model run ai/smollm2`
- %env OPENAI_API_KEY=<refer OpenAI API key for project 'ai-sandbox'>
- %env GOOGLE_API_KEY=<refer Gemini_API key from Google AI Studio project "ai-sandbox">



