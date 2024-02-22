from fastapi import APIRouter, Depends, HTTPException, status
from api.deps import get_db, CurrentAdminUser
from schemas.song import (
    SongCreate,
    SongUpdate,
    SongRead,
)
from typing import Any
from sqlalchemy.orm import Session
from crud.crud_song import crud_song
from crud.crud_album import crud_album
from schemas.common import SuccessResponse

router = APIRouter()


@router.get("/", response_model=SuccessResponse)
def get_all_songs(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db)
) -> Any:
    """
    Get all songs.
    """
    songs = crud_song.get_all(db=db)
    return SuccessResponse(
        description="Songs retrieved successfully",
        data=[SongRead.model_validate(song).model_dump() for song in songs],
    )


@router.get("/{song_id}", response_model=SuccessResponse)
def get_song_by_id(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db), song_id: int
) -> Any:
    """
    Get song by ID.
    """
    song = crud_song.get_by_id(db=db, obj_id=song_id)
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Song not found",
        )
    return SuccessResponse(
        description="Song retrieved successfully",
        data=SongRead.model_validate(song).model_dump(),
    )


@router.post("/", response_model=SuccessResponse)
def create_song(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    song_in: SongCreate,
) -> Any:
    """
    Create new song.
    """
    if getattr(song_in, "album_id"):
        album = crud_album.get_by_id(db=db, obj_id=song_in.album_id)
        if not album:
            raise HTTPException(
                status_code=400,
                detail=f"The album with id `{song_in.album_id}` doesn't exist.",
            )

    crud_song.create(db=db, obj_in=song_in)
    return SuccessResponse(
        description="Song created successfully",
    )


@router.put("/{song_id}", response_model=SuccessResponse)
def update_song(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    song_id: int,
    song_in: SongUpdate,
) -> Any:
    """
    Update a song.
    """
    song_db = crud_song.get_by_id(db=db, obj_id=song_id)
    if not song_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Song not found",
        )
    if getattr(song_in, "album_id"):
        album = crud_album.get_by_id(db=db, obj_id=song_in.album_id)
        if not album:
            raise HTTPException(
                status_code=400,
                detail=f"The album with id `{song_in.album_id}` doesn't exist.",
            )

    song = crud_song.update(db=db, db_obj=song_db, obj_in=song_in)
    return SuccessResponse(
        description="Song updated successfully",
        data=SongRead.model_validate(song).model_dump(),
    )


@router.delete("/{song_id}", response_model=SuccessResponse)
def delete_song(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db), song_id: int
) -> Any:
    """
    Delete a song.
    """
    song = crud_song.get_by_id(db=db, obj_id=song_id)
    if not song:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Song not found",
        )
    song = crud_song.remove(db=db, id=song_id)
    return SuccessResponse(
        description="Song deleted successfully",
        data=SongRead.model_validate(song).model_dump(),
    )
