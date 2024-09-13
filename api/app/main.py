from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from lib.session import Session, SessionRequest, ChatRequest

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions: dict = {} #should be stored in some db

@app.post("/chat")
def initialize(response: Response, request: SessionRequest):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"

    session = Session(request.embeddingFunction, request.chromaCollection, request.chatModel)
    sessions.update({session.sessionId: session})

    return {session.sessionId}

@app.post("/chat/{sessionId}")
def chat(chatRequest: ChatRequest, sessionId: str, response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"

    session = sessions[sessionId]
    chats = session.chats
    data = session.ask_llm(chatRequest.chat, chats)

    return data
