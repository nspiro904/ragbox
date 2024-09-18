import "./create.scss"

export default function create() {

  async function handleSubmit(e: SubmitEvent) {
    e.preventDefault();
    const data = new FormData(e.target);
    console.log("hi");
    
    const modelRequest = {
      name: data.get("name"),
      baseModel: data.get("baseModel"),
      systemPrompt: data.get("systemPrompt")
    }

    //move this uri
    const response = await fetch( "http://cannabot-api:8000/model/new",{
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(modelRequest)
    });
    console.log(response);
    
  }
  return (
  <div>
    <h1>Create New Model</h1>
    
    <form onSubmit={handleSubmit} >

      <label>
        Name 
      <input type="text" name="name"/>
      </label>

      <label>
        Base Model 
      <input type="text" name="baseModel"/>
      </label>

      <label>
        System Prompt 
      <textarea rows="15" cols="20" name="systemPrompt"/>
      </label>

      <button class="button" type="submit">Create</button>
    </form>
  </div>
  )
}