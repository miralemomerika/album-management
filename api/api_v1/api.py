from fastapi import APIRouter

from api.api_v1.endpoints import (
    users,
    auth,
    user_status,
    payment_info,
    bc_detail,
    distributor,
    album,
    song,
    music_service,
)

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(
    user_status.router, prefix="/user-status", tags=["user-status"]
)
api_router.include_router(
    payment_info.router, prefix="/payment-info", tags=["payment-info"]
)
api_router.include_router(
    bc_detail.router,
    prefix="/browser-connection",
    tags=["browser-connection-detail"],
)
api_router.include_router(
    distributor.router,
    prefix="/distributor",
    tags=["distributor"],
)
api_router.include_router(
    album.router,
    prefix="/album",
    tags=["album"],
)
api_router.include_router(
    song.router,
    prefix="/song",
    tags=["song"],
)
api_router.include_router(
    music_service.router,
    prefix="/music-service",
    tags=["music-service"],
)
