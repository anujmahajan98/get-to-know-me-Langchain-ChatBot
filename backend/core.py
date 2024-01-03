import os
from typing import Any, Dict, List
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Pinecone
import pinecone

from dotenv import load_dotenv

from consts import INDEX_NAME
load_dotenv()

pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment=os.environ.get("PINECONE_ENVIRONMENT_REGION"),
)

def run_llm(query, chat_history):
    embeddings = OpenAIEmbeddings()
    docSearch = Pinecone.from_existing_index(index_name = INDEX_NAME, embedding = embeddings)
    chat = ChatOpenAI(verbose = True, temperature = 0)
    
    qa = ConversationalRetrievalChain.from_llm(llm = chat, retriever = docSearch.as_retriever(), return_source_documents = True)

    return qa({"question" : query, "chat_history" : chat_history})


