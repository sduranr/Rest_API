from typing import Dict
from fastapi import FastAPI
from src.message_service import MessageService

app = FastAPI()
my_service = MessageService()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/api/message")
def send_message(message: dict):
    my_service.add_message(message)
    print(message)
    return {"message": "Message added successfully"}

@app.get("/api/message")
def read_messages():
    return my_service.get_messages()

# Nuevo endpoint PUT
@app.put("/api/message/{index}")
def update_message(index: int, new_message: dict):
    messages = my_service.get_messages()
    if index < 0 or index >= len(messages):
        return {"error": "Index out of range"}
    
    my_service.messages[index] = new_message
    return {"message": f"Message at index {index} updated successfully"}