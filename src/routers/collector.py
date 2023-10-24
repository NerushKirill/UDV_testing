from fastapi import APIRouter, Request, Form
from fastapi.responses import JSONResponse

from ..core.collect import collect_data


router = APIRouter(
    prefix="/collect",
    tags=["collect"],
    responses={404: {"description": "Not found"}},
)


@router.post('/')
async def collect(request: Request,
                  ip: str = Form(...),
                  port: int = Form(...),
                  username: str = Form(...),
                  password: str = Form(...)):
    data = collect_data(ip, port, username, password)

    return JSONResponse(content=data)
