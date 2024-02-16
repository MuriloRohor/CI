from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routes.FilialRouter import router as router_filial
from routes.UserRouter import router as router_user
from routes.RootRouter import router as router_root
from routes.CorrespondeciaInternaRouter import router as router_ci

app = FastAPI()

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")

app.include_router(router_filial)
app.include_router(router_user)
app.include_router(router_ci)
app.include_router(router_root)



if __name__ == "__main__":
    uvicorn.run(app="main:app",host="localhost", port=8000)