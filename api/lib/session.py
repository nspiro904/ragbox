from pydantic import BaseModel
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
from lib.ollama import ollama
import secrets
import chromadb


chroma_client = chromadb.HttpClient(host='chroma', port=8000)

class Session():
    embeddingFunction: chromadb.utils.embedding_functions.SentenceTransformerEmbeddingFunction
    chromaCollection: chromadb.api.models.Collection.Collection
    chatModel: str
    sessionId: str 
    chats: list = []
    
    def __init__(self, embeddingModel, chromaCollection, chatModel):    
        self.embeddingFunction = SentenceTransformerEmbeddingFunction(model_name=embeddingModel, device="cuda")
        self.chromaCollection = chroma_client.get_or_create_collection(name=chromaCollection, embedding_function=self.embeddingFunction)
        self.chatModel = chatModel
        self.sessionId = secrets.token_urlsafe(16)

    def query_chroma(self, question, max_distance=1.5):
        result_count =20
        result = self.chromaCollection.query(
        query_texts=[question], # Chroma will embed this for you
        n_results=result_count # how many results to return
        )
        ids, = result.get('ids')
        distances, = result.get('distances')
        documents, = result.get('documents')
        contexts=[]
        for i in range(result_count):
            if distances[i] <= max_distance:
                contexts.append({
                    "id": ids[i],
                    "distance": distances[i],
                    "document": documents[i],
                    })
        return contexts
    
    #query indicates whether the llm should search for documents for context

    def ask_llm(self, question, query=False):
        if query:
            docs = self.query_chroma(question)
            self.chats.append(
            {
            'role': 'user',
            'content': f'Information: {docs}. Question: {question}'
            })
        else:
            self.chats.append(
            {
            'role': 'user',
            'content': f'Question: {question}',
            })

        response = ollama.chat(model=self.chatModel, messages=self.chats)
        self.chats.append(response['message'])
        return response['message'] 


class SessionRequest(BaseModel):
    embeddingFunction: str
    chromaCollection: str
    chatModel: str

class ChatRequest(BaseModel):
    chat: str