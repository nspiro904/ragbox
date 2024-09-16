from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from lib.session import Session, SessionRequest, ChatRequest
from lib.ollama import _createModel, CreateModelRequest, _getModelInfo, UpdateModelRequest, _deleteModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#will be stored in pb, waiting for patch to python pb sdk that will resolve httpx dependency conflicts
sessions: dict = {} 

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

@app.post("/model/new")
def newModel(response: Response, createModelRequest: CreateModelRequest):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"

    data = _createModel(createModelRequest.name, createModelRequest.baseModel, createModelRequest.systemPrompt)
    return {data["status"]}

@app.get("/model/{modelName}")
def getModel(response: Response, modelName: str):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"

    data = _getModelInfo(modelName)
    return data

@app.post("/model/{modelName}")
def updateModel(response: Response, modelName: str, updateModelRequest: UpdateModelRequest):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"

    data = _createModel(modelName, updateModelRequest.baseModel, updateModelRequest.systemPrompt)
    return data

@app.delete("/model/{modelName}")
def deleteModel(response: Response, modelName: str):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    
    data = _deleteModel(modelName)
    return data