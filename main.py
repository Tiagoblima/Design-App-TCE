from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request, "id": 200})


@app.get("/analise_1.html", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("analise_1.html",
                                      {"request": request, "id": 200})


if __name__ == '__main__':
    app.setup()
