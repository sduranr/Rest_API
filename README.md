## PROYECTO EJEMPLO - MARKDOWN 
Crear el enviroment Opción 1: con VsCode Opción 2: con consola Agregar las siguientes dependencias en requirements.txt fastapi uvicorn pydantic Ejecutar pip install -r requirements.txt En el archivo main.py ´´´bash from fastapi import FastAPI

app = FastAPI()

@app.get("/") def read_root(): return {"message": "Hello World"}

@app.get("/sample/api") def read_sample(): return {"message": "This is the sample API endpoint"} ´´´

Para ejecutar el servidor:

uvicorn src.main:app --reload