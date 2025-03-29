from pathlib import Path
from typing import Annotated, AsyncIterator

from fastapi import Depends
from fastapi.templating import Jinja2Templates


async def get_templates() -> AsyncIterator[Jinja2Templates]:
    templates = Jinja2Templates(directory=Path(__file__).parent / "templates")
    yield templates


Templates = Annotated[Jinja2Templates, Depends(get_templates)]
