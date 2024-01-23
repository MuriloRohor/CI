from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.routes.FilialRouter import router as router_filial

app = FastAPI()


app.include_router(router_filial)


if __name__ == "__main__":
    uvicorn.run(app="main:app",host="localhost", reload=True, port=8000)