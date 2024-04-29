from typing import Union

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.status import HTTP_200_OK
from .api.item_routes import router as item_router


app = FastAPI()
app.include_router(item_router)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/data/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    # Mock data to pass to the template
    data = {"id": id, "name": "The great item", "description": "This is a great item."}
    # Use the templates object to render the specified template with context data
    return templates.TemplateResponse("item.html", {"request": request, "data": data})
