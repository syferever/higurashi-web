from fastapi import APIRouter, Depends, Path, Query, status, Request
from fastapi.responses import HTMLResponse

from src.depends import Templates

router: APIRouter = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def index(templates: Templates, request: Request):
    return templates.TemplateResponse(
        request=request, name="index.jinja", context={"title": "Rika mi mi nipah"}
    )
