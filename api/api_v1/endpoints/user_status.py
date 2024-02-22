from fastapi import APIRouter, Depends, HTTPException, status
from api.deps import get_db, CurrentAdminUser
from schemas.user_status import (
    UserStatusCreate,
    UserStatusUpdate,
    UserStatusRead,
)
from typing import Any
from sqlalchemy.orm import Session
from crud.crud_user_status import crud_user_status
from crud.crud_user import crud_user
from schemas.common import SuccessResponse

router = APIRouter()


@router.get("/", response_model=SuccessResponse)
def get_all_user_statuses(
    *, admin: CurrentAdminUser, db: Session = Depends(get_db)
) -> Any:
    """
    Get all user statuses.
    """
    statuses = crud_user_status.get_all(db=db)
    return SuccessResponse(
        description="User statuses retrieved successfully",
        data=[
            UserStatusRead.model_validate(user_status).model_dump()
            for user_status in statuses
        ],
    )


@router.get("/{user_status_id}", response_model=SuccessResponse)
def get_user_status_by_id(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    user_status_id: int,
) -> Any:
    """
    Get user status by ID.
    """
    status = crud_user_status.get_by_id(db=db, obj_id=user_status_id)
    if not status:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User status not found",
        )
    return SuccessResponse(
        description="User status retrieved successfully",
        data=UserStatusRead.model_validate(status).model_dump(),
    )


@router.post("/", response_model=SuccessResponse)
def create_user_status(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    user_status_in: UserStatusCreate,
) -> Any:
    """
    Create new user status.
    """
    if getattr(user_status_in, "user_id", None):
        user = crud_user.get_by_id(db=db, obj_id=user_status_in.user_id)
        if not user:
            raise HTTPException(
                status_code=400,
                detail=f"The user with id `{user_status_in.user_id}` doesn't exist.",
            )

    crud_user_status.create(db=db, obj_in=user_status_in)
    return SuccessResponse(
        description="User status created successfully",
    )


@router.put("/{user_status_id}", response_model=SuccessResponse)
def update_user_status(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    user_status_id: int,
    user_status_in: UserStatusUpdate,
) -> Any:
    """
    Update a user status.
    """
    user_status = crud_user_status.get_by_id(db=db, obj_id=user_status_id)
    if not user_status:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User status not found",
        )
    if getattr(user_status_in, "user_id"):
        user = crud_user.get_by_id(db=db, obj_id=user_status_in.user_id)
        if not user:
            raise HTTPException(
                status_code=400,
                detail=f"The user with id `{user_status_in.user_id}` doesn't exist.",
            )
    user_status = crud_user_status.update(
        db=db, db_obj=user_status, obj_in=user_status_in
    )
    return SuccessResponse(
        description="User status updated successfully",
        data=UserStatusRead.model_validate(user_status).model_dump(),
    )


@router.delete("/{user_status_id}", response_model=SuccessResponse)
def delete_user_status(
    *,
    admin: CurrentAdminUser,
    db: Session = Depends(get_db),
    user_status_id: int,
) -> Any:
    """
    Delete a user status.
    """
    user_status = crud_user_status.get_by_id(db=db, obj_id=user_status_id)
    if not user_status:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User status not found",
        )
    user_status = crud_user_status.remove(db=db, id=user_status_id)
    return SuccessResponse(
        description="User status deleted successfully",
        data=UserStatusRead.model_validate(user_status).model_dump(),
    )
