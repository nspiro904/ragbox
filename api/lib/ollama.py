from ollama import Client
from pydantic import BaseModel

ollama = Client(host='ollama-ollama-1')
    
class CreateModelRequest(BaseModel):
    name: str
    baseModel: str
    systemPrompt: str


def createModel(modelName: str, baseModel: str, systemPrompt: str ):
  
  modelfile = f'''
  FROM {baseModel}
  SYSTEM {systemPrompt}
  '''

  response = ollama.create(model=modelName, modelfile=modelfile)

  return response
