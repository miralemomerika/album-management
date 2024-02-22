from fastapi import APIRouter, Depends, HTTPException, status
from api.deps import get_db, CurrentAdminUser
from schemas.album import (
    AlbumCreate,
    AlbumUpdate,
    AlbumRead,
)
from typing import Any
from sqlalchemy.orm import Session
from crud.crud_album import crud_album
from crud.crud_distributor import crud_distributor
from crud.crud_music_service import crud_music_service
from schemas.common import SuccessResponse

router = APIRouter()


@router.get("/", response_model=SuccessResponse)
def get_all_albums(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db)
) -> Any:
    """
    Get all albums.
    """
    albums = crud_album.get_all(db=db)
    return SuccessResponse(
        description="Albums retrieved successfully",
        data=[
            AlbumRead.model_validate(album).model_dump() for album in albums
        ],
    )


@router.get("/{album_id}", response_model=SuccessResponse)
def get_album_by_id(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db), album_id: int
) -> Any:
    """
    Get album by ID.
    """
    album = crud_album.get_by_id(db=db, obj_id=album_id)
    if not album:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Album not found",
        )
    return SuccessResponse(
        description="Album retrieved successfully",
        data=AlbumRead.model_validate(album).model_dump(),
    )


@router.post("/", response_model=SuccessResponse)
def create_album(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    album_in: AlbumCreate,
) -> Any:
    """
    Create new album.
    """
    if getattr(album_in, "distributor_id"):
        dist = crud_distributor.get_by_id(
            db=db, obj_id=album_in.distributor_id
        )
        if not dist:
            raise HTTPException(
                status_code=400,
                detail=f"The distributor with id `{album_in.distributor_id}` doesn't exist.",
            )

    if getattr(album_in, "music_services_id"):
        music_service = crud_music_service.get_by_id(
            db=db, obj_id=album_in.music_services_id
        )
        if not music_service:
            raise HTTPException(
                status_code=400,
                detail=f"The music service with id `{album_in.music_services_id}` doesn't exist.",
            )

    crud_album.create(db=db, obj_in=album_in)
    return SuccessResponse(
        description="Album created successfully",
    )


@router.put("/{album_id}", response_model=SuccessResponse)
def update_album(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    album_id: int,
    album_in: AlbumUpdate,
) -> Any:
    """
    Update an album.
    """
    album_db = crud_album.get_by_id(db=db, obj_id=album_id)
    if not album_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Album not found",
        )
    if getattr(album_in, "distributor_id"):
        dist = crud_distributor.get_by_id(
            db=db, obj_id=album_in.distributor_id
        )
        if not dist:
            raise HTTPException(
                status_code=400,
                detail=f"The distributor with id `{album_in.distributor_id}` doesn't exist.",
            )

    if getattr(album_in, "music_services_id"):
        music_service = crud_music_service.get_by_id(
            db=db, obj_id=album_in.music_services_id
        )
        if not music_service:
            raise HTTPException(
                status_code=400,
                detail=f"The music service with id `{album_in.music_services_id}` doesn't exist.",
            )

    album = crud_album.update(db=db, db_obj=album_db, obj_in=album_in)
    return SuccessResponse(
        description="Album updated successfully",
        data=AlbumRead.model_validate(album).model_dump(),
    )


@router.delete("/{album_id}", response_model=SuccessResponse)
def delete_album(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db), album_id: int
) -> Any:
    """
    Delete an album.
    """
    album = crud_album.get_by_id(db=db, obj_id=album_id)
    if not album:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Album not found",
        )
    album = crud_album.remove(db=db, id=album_id)
    return SuccessResponse(
        description="Album deleted successfully",
        data=AlbumRead.model_validate(album).model_dump(),
    )
