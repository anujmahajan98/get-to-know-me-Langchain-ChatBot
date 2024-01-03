import os

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv

from consts import INDEX_NAME

load_dotenv()

pinecone.init(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment=os.environ.get("PINECONE_ENVIRONMENT_REGION"),
)

def ingestDataFromPdfIntoPinecone():
    print('Reading Data from PDF')
    pdf_path = "/Users/anujmahajan/Desktop/Anuj Documents/Resume/PDF/Amazon/Anuj Mahajan - IUB MS CS - CV.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=30, separators=["\n\n", "\n", " ", ""]
    )
    documents = text_splitter.split_documents(documents=documents)

    print(f"Going to insert {len(documents)} to Pinecone")
    embeddings = OpenAIEmbeddings()
    Pinecone.from_documents(documents, embeddings, index_name=INDEX_NAME)
    print("****** Added to Pinecone vectorstore vectors")

if __name__ == "__main__":
    ingestDataFromPdfIntoPinecone()