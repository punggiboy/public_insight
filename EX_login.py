from fastapi import FastAPI

app = FastAPI()
users = {"test": "1234"}

@app.get("/login")
def login(username: str, password: str):
    return {"message": "Login Success"} if users.get(username) == password else {"error": "Invalid Credentials"}
