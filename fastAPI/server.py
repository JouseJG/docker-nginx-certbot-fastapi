from fastapi import FastAPI

app = FastAPI()

@app.get("/", status_code=200)
async def hello():
    return {"msg": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0")