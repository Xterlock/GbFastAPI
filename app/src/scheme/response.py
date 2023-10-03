from pydantic import BaseModel


class StatusOKResponse(BaseModel):
    status: int
    detail: str = "ok"


class IDResponse(StatusOKResponse):
    id: int
    status: int
