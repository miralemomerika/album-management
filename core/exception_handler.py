from fastapi import HTTPException
from fastapi.responses import JSONResponse
from schemas.common import (
    InternalServerErrorResponse,
    BadRequestResponse,
    ResponseStatus,
    StandardResponse,
)


def http_exception_handler(request, exc: HTTPException):
    if 400 <= exc.status_code < 500:
        response = BadRequestResponse(
            status=ResponseStatus.ERROR, description=exc.detail
        )
    elif exc.status_code >= 500:
        response = InternalServerErrorResponse()
    else:
        response = StandardResponse(
            status=ResponseStatus.ERROR,
            description="Our team has been notified about this issue. Please try again later.",
        )
    return JSONResponse(
        status_code=exc.status_code, content=response.model_dump()
    )
