from typing import Annotated
from fastapi import APIRouter, Depends, Path, Query, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.depends import Templates

router: APIRouter = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(
    templates: Annotated[Jinja2Templates, Depends(Templates)], request: Request
):
    return templates.TemplateResponse(
        request=request, name="index.jinja", context={"title": "Rika mi mi nipah"}
    )
