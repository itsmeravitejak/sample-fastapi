from fastapi import FastAPI

app = FastAPI()


@app.post("/items/", status_code=200)
async def create_item(name: str):
    return {"name": name}

@app.get("/items")
async def list_item():
    return [{"name":"Item1"},
            {"name":"Item2"}]