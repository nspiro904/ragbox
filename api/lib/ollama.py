from ollama import Client
from pydantic import BaseModel

ollama = Client(host='ollama-ollama-1')
    
class CreateModelRequest(BaseModel):
    name: str
    baseModel: str
    systemPrompt: str
  
class UpdateModelRequest(BaseModel):
    baseModel: str = None
    systemPrompt: str = None


def _createModel(modelName: str, baseModel: str, systemPrompt: str ):
  
  modelfile = f'''
  FROM {baseModel}
  SYSTEM {systemPrompt}
  '''
  response = ollama.create(model=modelName, modelfile=modelfile)

  return response

def _getModelInfo(modelName: str):
  response = ollama.show(modelName)
  return response

def _deleteModel(modelName: str):
  response = ollama.delete(modelName)
  return response

def _getModelList():
  response = ollama.list()
  return response