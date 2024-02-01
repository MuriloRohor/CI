from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routes.FilialRouter import router as router_filial
from routes.UserRouter import router as router_user

app = FastAPI()


app.include_router(router_filial)
app.include_router(router_user)


if __name__ == "__main__":
    uvicorn.run(app="main:app",host="localhost", reload=True, port=8000)