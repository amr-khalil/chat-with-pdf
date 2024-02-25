import os
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPEN_API_KEY"))
