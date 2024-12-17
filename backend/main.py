from fastapi import FastAPI, Query
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
import pinecone

app = FastAPI()

# Initialize Pinecone and OpenAI Embeddings
pinecone.init(api_key="YOUR_API_KEY", environment="gcp-starter")
embeddings = OpenAIEmbeddings()
vectorstore = Pinecone("knowledge-base", embeddings)

# Initialize LLM and Retrieval Chain
llm = ChatOpenAI(model="gpt-4")
qa_chain = RetrievalQA.from_chain_type(llm, retriever=vectorstore.as_retriever())

@app.post("/query/")
def answer_question(query: str = Query(..., description="Your question to the agent")):
    result = qa_chain.run(query)
    return {"answer": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)