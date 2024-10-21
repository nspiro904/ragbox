import {error} from '@sveltejs/kit'
import {API_URL} from '$env/static/private'


export async function load( {params}) {
  const {name} = params;
    
  const response = await fetch(`${API_URL}/model/${name}`);

  if(response.status === 404)
    error(404, {
      message: 'Model not found'
      }
    );
    
  const responseData = await response.json();
  
  const {details, system} = responseData; 
  return {details, system} 
}


export const actions = {
  default: async ({request, url}) => {

    const modelName = url.pathname.split('/')[2]; //i feel like there's a better way to do this 
    const data = await request.formData();

    const baseModel = data.get('base');
    const systemPrompt = data.get('systemPrompt');

    const response = await fetch(`${API_URL}/model/${modelName}`,
      {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify( {
          modelName,
          baseModel,
          systemPrompt
        })
      });

    if(response.status === 400)
      error(400, {
        message: 'Invalid model settings'
        }
      );
        
    const responseData = await response.json();

    return {responseData};
  }
}