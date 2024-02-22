from fastapi import APIRouter, Depends, HTTPException, status
from api.deps import get_db, CurrentAdminUser
from schemas.music_service import (
    MusicServiceCreate,
    MusicServiceUpdate,
    MusicServiceRead,
)
from typing import Any
from sqlalchemy.orm import Session
from crud.crud_music_service import crud_music_service
from crud.crud_user import crud_user
from schemas.common import SuccessResponse

router = APIRouter()


@router.get("/", response_model=SuccessResponse)
def get_all_music_services(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db)
) -> Any:
    """
    Get all music services.
    """
    services = crud_music_service.get_all(db=db)
    return SuccessResponse(
        description="Music services retrieved successfully",
        data=[
            MusicServiceRead.model_validate(service).model_dump()
            for service in services
        ],
    )


@router.get("/{service_id}", response_model=SuccessResponse)
def get_mservice_by_id(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db), service_id: int
) -> Any:
    """
    Get music service by ID.
    """
    service = crud_music_service.get_by_id(db=db, obj_id=service_id)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Music service not found",
        )
    return SuccessResponse(
        description="Music service retrieved successfully",
        data=MusicServiceRead.model_validate(service).model_dump(),
    )


@router.post("/", response_model=SuccessResponse)
def create_mservice(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    mservice_in: MusicServiceCreate,
) -> Any:
    """
    Create new music service.
    """
    if getattr(mservice_in, "user_id"):
        user = crud_user.get_by_id(db=db, obj_id=mservice_in.user_id)
        if not user:
            raise HTTPException(
                status_code=400,
                detail=f"The user with id `{mservice_in.user_id}` doesn't exist.",
            )

    crud_music_service.create(db=db, obj_in=mservice_in)
    return SuccessResponse(
        description="Music service created successfully",
    )


@router.put("/{service_id}", response_model=SuccessResponse)
def update_mservice(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    service_id: int,
    mservice_in: MusicServiceUpdate,
) -> Any:
    """
    Update a music service.
    """
    service_db = crud_music_service.get_by_id(db=db, obj_id=service_id)
    if not service_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Music service not found",
        )
    if getattr(mservice_in, "user_id"):
        user = crud_user.get_by_id(db=db, obj_id=mservice_in.user_id)
        if not user:
            raise HTTPException(
                status_code=400,
                detail=f"The user with id `{mservice_in.user_id}` doesn't exist.",
            )

    service = crud_music_service.update(
        db=db, db_obj=service_db, obj_in=mservice_in
    )
    return SuccessResponse(
        description="Music service updated successfully",
        data=MusicServiceRead.model_validate(service).model_dump(),
    )


@router.delete("/{service_id}", response_model=SuccessResponse)
def delete_album(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db), service_id: int
) -> Any:
    """
    Delete a music service.
    """
    service = crud_music_service.get_by_id(db=db, obj_id=service_id)
    if not service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Music service not found",
        )
    service = crud_music_service.remove(db=db, id=service_id)
    return SuccessResponse(
        description="Music service deleted successfully",
        data=MusicServiceRead.model_validate(service).model_dump(),
    )
