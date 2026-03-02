from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Jarvis Server Online 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
