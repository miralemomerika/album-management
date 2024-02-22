from fastapi import FastAPI
from api.api_v1.api import api_router
from core.config import settings
from fastapi import HTTPException
from core.exception_handler import http_exception_handler
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.add_exception_handler(HTTPException, http_exception_handler)

app.include_router(api_router, prefix=settings.API_V1_STR)
