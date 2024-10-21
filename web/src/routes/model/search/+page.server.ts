export async function load() {    
  const response = await fetch('http://ragbox-api-1:8000/model/list');

  const data = await response.json();
  const {models} = data;
  
  return {models}; 
}