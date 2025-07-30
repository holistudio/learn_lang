# learn_lang
learning LangChain and LangGraph

## Getting started

After creating virtual environment:

```
pip install -r requirements.txt
```

```
pip install -qU "langchain[google-genai]"
```

```
pip install langchain-core langgraph>0.2.28
```

`.env` file:

```
GOOGLE_API_KEY=(your Gemini API Key here)
LANGSMITH_API_KEY=(your LangSmith API Key here)
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=default (or LangSmith project name)
```

