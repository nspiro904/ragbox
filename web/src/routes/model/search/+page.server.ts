import {API_URL} from '$env/static/private'

export async function load() {    
  const response = await fetch(`${API_URL}/model/list`);

  const data = await response.json();
  const {models} = data;
  
  return {models}; 
}

export const actions = {
  default: async () => {
    
    return {};
  }
}

