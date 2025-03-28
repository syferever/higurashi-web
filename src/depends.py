from typing import AsyncGenerator
from fastapi.templating import Jinja2Templates


async def Templates() -> AsyncGenerator[Jinja2Templates, None]:
    templates = Jinja2Templates(directory="templates")
    yield templates
