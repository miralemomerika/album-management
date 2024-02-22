from typing import Union
from pydantic import BaseModel
from enum import Enum


class ResponseStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"


class StandardResponse(BaseModel):
    status: ResponseStatus
    description: str
    data: Union[dict, list] = {}


class SuccessResponse(StandardResponse):
    status: ResponseStatus = ResponseStatus.SUCCESS


class BadRequestResponse(StandardResponse):
    status: ResponseStatus = ResponseStatus.ERROR


class InternalServerErrorResponse(StandardResponse):
    status: ResponseStatus = ResponseStatus.ERROR
    description: str = "Something went wrong on the server"


class WarningResponse(StandardResponse):
    status: ResponseStatus = ResponseStatus.WARNING
    title: str = "Warning"
