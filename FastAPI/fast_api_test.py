from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates/", auto_reload=True)


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        "item.html", context={"request": request, "id": id}
    )


@app.get("/")
async def index(request: Request):

    return templates.TemplateResponse(
        "index.html", context={"request": request, "result": "HELLO"}
    )
