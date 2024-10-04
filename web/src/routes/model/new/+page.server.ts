export const actions = {
  default: async ({request}) => {

    const data = await request.formData();

    const name = data.get('name');
    const baseModel = data.get('base');
    const systemPrompt = data.get('systemPrompt');


    const response = await fetch("http://ragbox-api-1:8000/model/new",
      {
        method: "POST",
        headers: {
        "Content-Type": "application/json",

        },
        body: JSON.stringify( {
          name,
          baseModel,
          systemPrompt
        })
      });
    const responseData = await response.json();

    return {responseData};
  }
}